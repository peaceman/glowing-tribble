from django.conf import settings
from django.contrib.auth.models import User
from django.http.request import HttpRequest
from edmuser.models import UserSession, UserSessionVisitedUrls


class UserIpAddressMiddleware(object):
    def process_request(self, request):
        """
        Checks request for configured header field, to modify the request object
        :param HttpRequest request: incoming request
        """
        header_field = getattr(settings, 'IP_USER_HEADER_FIELD', '').upper().replace('-', '_')
        request.user_ip = request.META['REMOTE_ADDR']

        if header_field in request.META:
            request.user_ip = request.META['REMOTE_ADDR'] = request.META[header_field]


class UserSessionMiddleware(object):
    def process_request(self, request):
        print 'user is authenticated', request.user.is_authenticated()
        if request.user.is_authenticated():
            request.user_session = request.user.usersession_set.latest()


class UserUrlTrackerMiddleware(object):
    def process_request(self, request):
        if hasattr(request, 'user_session'):
            UserSessionVisitedUrls(url=request.build_absolute_uri(), session=request.user_session).save()
