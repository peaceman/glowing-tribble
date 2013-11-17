from django.contrib.auth.models import User
from django.db import models


class UserAgent(models.Model):
    value = models.TextField()


class UserSession(models.Model):
    user = models.ForeignKey(User)
    ip_address = models.GenericIPAddressField()
    user_agent = models.ForeignKey(UserAgent)
    created_at = models.DateTimeField(auto_now_add=True)

    @classmethod
    def create_from_login_signal(cls, **kwargs):
        print kwargs
        user_agent, user_agent_created = UserAgent.objects.get_or_create(
            value=kwargs['request'].META.get('HTTP_USER_AGENT', ''))
        cls(user=kwargs['user'],
            ip_address=kwargs['request'].user_ip,
            user_agent=user_agent).save()


class UserSessionVisitedUrls(models.Model):
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    session = models.ForeignKey(UserSession)