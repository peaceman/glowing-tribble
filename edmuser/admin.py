from django.contrib import admin
from edmuser.models import *

admin.site.register(UserSession)
admin.site.register(UserSessionVisitedUrl)
admin.site.register(UserAgent)
