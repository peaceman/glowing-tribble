from django.contrib.auth.models import User
from django.db import models
from taggit.managers import TaggableManager
from edm.models import SoftDeletionModel
from edmmusic.models import MusicGenre, MusicProgram, MusicPlugin, MusicBank
from edmreview.models import Review
from edmuser.models import UserSession


class ProjectFileCategory(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ProjectFile(SoftDeletionModel):
    category = models.ForeignKey(ProjectFileCategory)
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    author = models.ForeignKey(User, db_column='created_by')


class ProjectFileVersion(models.Model):
    project_file = models.ForeignKey(ProjectFile)
    review = models.OneToOneField(Review, related_name='review_of')
    price = models.DecimalField(max_digits=9, decimal_places=2)
    description = models.TextField()
    bpm = models.PositiveSmallIntegerField()
    session = models.ForeignKey(UserSession)
    tags = TaggableManager()
    genre = models.ForeignKey(MusicGenre)
    compatible_programs = models.ManyToManyField(MusicProgram)
    compatible_plugins = models.ManyToManyField(MusicPlugin)
    compatible_banks = models.ManyToManyField(MusicBank)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)