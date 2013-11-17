from django.shortcuts import render
import account.views
import edmuser.forms


class SignUpView(account.views.SignupView):
    form_class = edmuser.forms.SignupForm

    def create_user(self, form, commit=True, **kwargs):
        names = {
            'first_name': form.cleaned_data.get('first_name'),
            'last_name': form.cleaned_data.get('last_name')
        }
        kwargs = dict(kwargs.items() + names.items())
        return super(SignUpView, self).create_user(form, commit, **kwargs)

