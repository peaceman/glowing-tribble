from django.contrib.auth.models import User
from django.db import models

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