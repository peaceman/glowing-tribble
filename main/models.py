from django.db import models
from django.contrib.auth.models import User


class MusicSoftwareManager(models.Manager):
    def get_queryset(self):
        return super(MusicSoftwareManager, self).get_queryset().filter(is_active=True)


class MusicSoftware(models.Model):
    name = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, db_column='created_by')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = MusicSoftwareManager()
