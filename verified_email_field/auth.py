from django import forms
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db import transaction
from django.utils.crypto import get_random_string
from django.utils.translation import gettext_lazy as _

from . import settings
from .forms import VerifiedEmailField

__all__ = ["EmailAuthenticationForm", "VerifiedEmailBackend"]


class EmailAuthenticationForm(forms.Form):
    """
    Form for authenticating users by verified email.
    """

    email = VerifiedEmailField(
        _("E-mail"), fieldsetup_id="verified_email_field.EmailAuthenticationForm"
    )

    error_messages = {
        "error": _("""User with given e-mail couldn't neither be found nor created."""),
    }

    def clean(self):
        email = self.cleaned_data.get("email")

        if email:
            self.user = authenticate(verified_email=email)

            if self.user is None:
                raise forms.ValidationError(
                    self.error_messages["error"],
                    code="error",
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

    def authenticate(self, request, verified_email: str):
        UserModel = get_user_model()
        user = UserModel.objects.filter(email=verified_email, is_active=True).last()
        if user:
            return user
        if settings.CREATE_USER:
            chars = "abcdefghijklmnopqrstuvwxyz0123456789"
            prefix = verified_email.split("@")[0]
            for suffix in [
                "",
                "_" + get_random_string(3, chars),
                "_" + get_random_string(5, chars),
                "_" + get_random_string(10, chars),
            ]:
                username = prefix + suffix
                try:
                    with transaction.atomic():
                        return UserModel.objects.create_user(
                            username=username, email=verified_email
                        )
                except Exception:
                    pass
