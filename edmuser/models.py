from django.contrib.auth.models import User
from django.db import models
from django_extensions.db.fields import CreationDateTimeField


class UserAgent(models.Model):
    value = models.TextField()
    created_at = CreationDateTimeField()


class UserSession(models.Model):
    user = models.ForeignKey(User)
    ip_address = models.GenericIPAddressField()
    user_agent = models.ForeignKey(UserAgent)
    created_at = CreationDateTimeField()

    class Meta:
        get_latest_by = 'created_at'

    @classmethod
    def create_from_login_signal(cls, **kwargs):
        user_agent, user_agent_created = UserAgent.objects.get_or_create(
            value=kwargs['request'].META.get('HTTP_USER_AGENT', ''))
        cls(user=kwargs['user'],
            ip_address=kwargs['request'].user_ip,
            user_agent=user_agent).save()


class UserSessionVisitedUrl(models.Model):
    url = models.URLField()
    created_at = CreationDateTimeField()
    session = models.ForeignKey(UserSession)