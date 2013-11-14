from django.db import models
from django.contrib.auth.models import User


class MusicSoftware(models.Model):
    name = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, db_column='created_by')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
