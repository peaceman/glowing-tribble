from django.db import models
from django.utils.translation import ugettext_lazy as _, ugettext_lazy


class Review(models.Model):
    WAITING = 1
    RUNNING = 2
    FINISHED = 3
    STATES = (
        (WAITING, _('Waiting')),
        (RUNNING, _('Running')),
        (FINISHED, _('Finished')),
    )

    state = models.PositiveSmallIntegerField(choices=STATES, default=WAITING, db_index=True)
    result = models.NullBooleanField(default=None)
    result_reasoning = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ReviewableModelManager(models.Manager):
    def get_queryset(self):
        return super(ReviewableModelManager, self).get_queryset().filter(reviewed=True)