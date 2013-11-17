from django.db import models
from edmreview.models import ReviewableModelManager
from main.models import UserSession


class MusicGenre(models.Model):
    name = models.CharField(max_length=255, unique=True)
    reviewed = models.BooleanField(default=False)
    session = models.ForeignKey(UserSession)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    public_objects = ReviewableModelManager()


class MusicProgram(models.Model):
    name = models.CharField(max_length=255, unique=True)
    reviewed = models.BooleanField(default=False)
    session = models.ForeignKey(UserSession)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    public_objects = ReviewableModelManager()


class MusicPlugins(models.Model):
    name = models.CharField(max_length=255, unique=True)
    software = models.ForeignKey(MusicProgram)
    reviewed = models.BooleanField(default=False)
    session = models.ForeignKey(UserSession)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    public_objects = ReviewableModelManager()


class MusicBanks(models.Model):
    name = models.CharField(max_length=255, unique=True)
    plugin = models.ForeignKey(MusicPlugins)
    reviewed = models.BooleanField(default=False)
    session = models.ForeignKey(UserSession)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    public_objects = ReviewableModelManager()