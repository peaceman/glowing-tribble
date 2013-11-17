from django.contrib.auth.signals import user_logged_in
from edmuser.models import *

user_logged_in.connect(UserSession.create_from_login_signal)