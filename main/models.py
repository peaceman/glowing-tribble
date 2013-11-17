from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from taggit.managers import TaggableManager
from edm.models import SoftDeletionModel


class UserAgent(models.Model):
    value = models.TextField()


class UserSession(models.Model):
    user = models.ForeignKey(User)
    ip_address = models.GenericIPAddressField()
    user_agent = models.ForeignKey(UserAgent)
    created_at = models.DateTimeField(auto_now_add=True)


class UserSessionVisitedUrls(models.Model):
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    session = models.ForeignKey(UserSession)


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
    compatible_plugins = models.ManyToManyField(MusicPlugins)
    compatible_banks = models.ManyToManyField(MusicBanks)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Purchase(models.Model):
    STATE_PENDING = 1
    STATE_FAILED = 2
    STATE_COMPLETED = 3

    STATES = (
        (STATE_PENDING, _('Pending')),
        (STATE_FAILED, _('Failed')),
        (STATE_COMPLETED, _('Completed'))
    )

    user = models.ForeignKey(User)
    project_file_version = models.ForeignKey(ProjectFileVersion)
    state = models.PositiveSmallIntegerField(choices=STATES, default=STATE_PENDING)
    session = models.ForeignKey(UserSession)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)