from django.contrib import admin
from edmuser.models import *

admin.site.register(UserSession)
admin.site.register(UserSessionVisitedUrls)
admin.site.register(UserAgent)
