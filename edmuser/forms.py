import account.forms
from crispy_forms.bootstrap import StrictButton
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout


class SignupForm(account.forms.SignupForm):
    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        #self.helper = FormHelper(self)
        #self.helper.form_class = 'form-horizontal'
        #self.helper.label_class = 'col-lg-2'
        #self.helper.field_class = 'col-lg-8'
        ##self.helper.layout = Layout('username', 'password', 'password_confirm', 'email', StrictButton('Register', css_class='btn-default'),)
        #self.helper.layout.extend([
        #    Submit('register', 'Register'),
        #    StrictButton('Register')
        #])