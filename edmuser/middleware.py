from django.conf import settings
from django.http.request import HttpRequest

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
