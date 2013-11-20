from account.forms import LoginUsernameForm
import account.views
import edmuser.forms
from edmuser.forms import SignupForm


class LoginView(account.views.LoginView):
    template_name = 'account/login_signup.html'

    def render_to_response(self, context, **response_kwargs):
        forms = dict(signup_form=edmuser.forms.SignupForm, login_form=self.get_form(self.get_form_class()))
        context = dict(context.items() + forms.items())
        return super(LoginView, self).render_to_response(context, **response_kwargs)


class SignUpView(account.views.SignupView):
    form_class = edmuser.forms.SignupForm
    template_name = 'account/login_signup.html'

    def render_to_response(self, context, **response_kwargs):
        forms = dict(signup_form=self.get_form(self.get_form_class()), login_form=LoginUsernameForm)
        context = dict(context.items() + forms.items())
        return super(SignUpView, self).render_to_response(context, **response_kwargs)

    def create_user(self, form, commit=True, **kwargs):
        names = {
            'first_name': form.cleaned_data.get('first_name'),
            'last_name': form.cleaned_data.get('last_name')
        }
        kwargs = dict(kwargs.items() + names.items())
        return super(SignUpView, self).create_user(form, commit, **kwargs)

