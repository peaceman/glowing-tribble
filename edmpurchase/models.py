from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _
from edmproject.models import ProjectFileVersion
from edmuser.models import UserSession


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