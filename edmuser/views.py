from django.shortcuts import render
import account.views
import edmuser.forms


class SignUpView(account.views.SignupView):
    form_class = edmuser.forms.SignupForm

