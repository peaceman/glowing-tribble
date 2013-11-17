from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _, ugettext_lazy
from jsonfield import JSONField
from edmproject.models import ProjectFileVersion
from edmuser.models import UserSession


class UploadedFolderTmpFile(models.Model):
    directory_identifier = models.CharField(max_length=36, db_index=True)
    storage_filename = models.CharField(max_length=36, unique=True)
    original_filename = models.CharField(max_length=255)
    file_size_in_bytes = models.BigIntegerField()
    mime_type = models.CharField(max_length=255, null=True)
    session = models.ForeignKey(UserSession)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class UploadedFile(models.Model):
    TYPE_PREVIEW = 1
    TYPE_ARCHIVE = 2
    TYPE_VIDEO = 3
    TYPE_PICTURE = 4

    TYPES = (
        (TYPE_PREVIEW, _('Preview')),
        (TYPE_ARCHIVE, _('Archive')),
        (TYPE_VIDEO, _('Video')),
        (TYPE_PICTURE, _('Picture'))
    )

    type = models.PositiveSmallIntegerField(choices=TYPES, db_index=True)
    storage_filename = models.CharField(max_length=36, unique=True)
    original_filename = models.CharField(max_length=255)
    file_size_in_bytes = models.BigIntegerField()
    mime_type = models.CharField(max_length=255, default=None)
    meta_data = JSONField()
    session = models.ForeignKey(UserSession)
    uploader = models.ForeignKey(User, db_column='created_by')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    project_file_version = models.ForeignKey(ProjectFileVersion)