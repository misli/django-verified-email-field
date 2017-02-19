from __future__ import unicode_literals

from django import forms
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.backends import ModelBackend
from django.utils.translation import ugettext_lazy as _

from .forms import VerifiedEmailField


__all__ = ['EmailAuthenticationForm', 'VerifiedEmailBackend']


class EmailAuthenticationForm(forms.Form):
    """
    Form for authenticating users by verified email.
    """
    email = VerifiedEmailField(_('E-mail'))

    error_messages = {
        'error': _('''User with given e-mail couldn't neither be found nor created.'''),
    }

    def clean(self):
        email = self.cleaned_data.get('email')

        if email:
            self.user = authenticate(verified_email=email)

            if self.user is None:
                raise forms.ValidationError(
                    self.error_messages['error'],
                    code='error',
                )
        return self.cleaned_data

    # following methods make this form be drop in replacement for
    # Django's AuthenticationForm

    def __init__(self, request=None, *args, **kwargs):
        super(EmailAuthenticationForm, self).__init__(*args, **kwargs)

    def get_user_id(self):
        return self.user and self.user.id

    def get_user(self):
        return self.user


class VerifiedEmailBackend(ModelBackend):
    """
    Authenticates against settings.AUTH_USER_MODEL using verified email.
    Fails if there are two active users with given email.
    Fails to create new user if there already is user with given email as username.
    """

    def authenticate(self, verified_email=None, **kwargs):
        if verified_email:
            UserModel = get_user_model()
            try:
                return (
                    UserModel.objects.filter(email=verified_email, is_active=True).last() or
                    UserModel.objects.create_user(username=verified_email, email=verified_email)
                )
            except:
                pass
