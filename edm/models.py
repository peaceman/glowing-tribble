from django.db import models
from django.db.models.query import QuerySet
from south.modelsinspector import add_introspection_rules

add_introspection_rules([], ["^edm\.models\.LiveField"])

class LiveField(models.Field):
    '''Similar to a BooleanField, but stores False as NULL.'''
    description = 'Soft-deletion status'
    __metaclass__ = models.SubfieldBase

    def __init__(self, **kwargs):
        super(LiveField, self).__init__(default=True, null=True)

    def get_internal_type(self):
        # Create DB column as though for a NullBooleanField
        return 'NullBooleanField'

    def get_prep_value(self, value):
        # Convert in-Python value to value we'll store in DB
        if value:
            return 1
        return None

    def to_python(self, value):
        # Misleading name, since type coercion also occurs when
        # assigning a value to the field in Python
        return bool(value)

    def get_prep_lookup(self, lookup_type, value):
        # Filters with .alive=False won't work, so
        # raise a helpful exception instead.
        if lookup_type == 'exact' and not value:
            msg = ("%(model)s doesn't support filters with "
                   "%(field)s=False. Use a filter with "
                   "%(field)s=None or an exclude with "
                   "%(field)s=True instead.")
            raise TypeError(msg % {
                'model': self.model.__name__,
                'field': self.name
            })

        return super(LiveField, self).get_prep_lookup(lookup_type, value)


class SoftDeletionQuerySet(QuerySet):
    def delete(self):
        # Bulk delete bypasses individual objects' delete methods.
        return super(SoftDeletionQuerySet, self).update(alive=False)

    def hard_delete(self):
        return super(SoftDeletionQuerySet, self).delete()

    def alive(self):
        return self.filter(alive=True)

    def dead(self):
        return self.exclude(alive=True)


class SoftDeletionManager(models.Manager):
    def __init__(self, *args, **kwargs):
        self.alive_only = kwargs.pop('alive_only', True)
        super(SoftDeletionManager, self).__init__(*args, **kwargs)

    def get_queryset(self):
        if self.alive_only:
            return SoftDeletionQuerySet(self.model).filter(alive=True)
        return SoftDeletionQuerySet(self.model)

    def hard_delete(self):
        return self.get_queryset().hard_delete()


class SoftDeletionModel(models.Model):
    alive = LiveField()

    objects = SoftDeletionManager()
    all_objects = SoftDeletionManager(alive_only=False)

    class Meta:
        abstract = True

    def delete(self, using=None):
        self.alive = False
        self.save()

    def hard_delete(self):
        super(SoftDeletionModel, self).delete()