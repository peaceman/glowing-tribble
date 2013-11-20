from django.conf.urls import patterns, include, url
from django.contrib import admin
import edmuser.views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'edm.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'main.views.home', name='home'),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^account/signup/$', edmuser.views.SignUpView.as_view(), name='account_signup'),
    url(r'^account/login/$', edmuser.views.LoginView.as_view(), name='account_login'),
    url(r'^account/', include('account.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
