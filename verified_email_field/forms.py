from __future__ import unicode_literals

from django import forms
from django.core.exceptions import ValidationError
from django.forms.fields import CharField, EmailField, MultiValueField
from django.utils.translation import ugettext_lazy as _

from .fieldsetup import VerifiedEmailFieldSetup, fieldsetups
from .utils import get_code, send_code
from .widgets import VerifiedEmailWidget


class SendForm(forms.Form):
    email = EmailField()


class VerificationCodeField(CharField):
    default_error_messages = {
        'invalid': _('Enter a valid verification code.'),
    }

    def __init__(self, length, **kwargs):
        kwargs['max_length'] = kwargs['min_length'] = length
        kwargs['required'] = False
        super(VerificationCodeField, self).__init__(**kwargs)


class VerifiedEmailField(MultiValueField):

    def __init__(self, required=True, fieldsetup_id=None, max_length=None,
                 email_label=_('e-mail'), send_label=_('send verification code'), code_label=_('verification code'),
                 **kwargs):
        self.fieldsetup_id = fieldsetup_id or str(hash(self))
        self.fieldsetup = fieldsetups.setdefault(self.fieldsetup_id, VerifiedEmailFieldSetup(**kwargs))
        self.widget = VerifiedEmailWidget(
            send_label=send_label,
            fieldsetup_id=self.fieldsetup_id,
            email_attrs={'placeholder': email_label},
            code_attrs={'placeholder': code_label},
        )
        super(VerifiedEmailField, self).__init__((
            EmailField(label=email_label, required=required),
            VerificationCodeField(label=code_label, length=self.fieldsetup.code_length),
        ), require_all_fields=False, **kwargs)

    def clean(self, value):
        email = self.fields[0].clean(value[0])
        code = self.fields[1].clean(value[1])
        valid_code = get_code(email, self.fieldsetup)
        if email:
            if not valid_code:
                send_code(email, self.fieldsetup)
                raise ValidationError(_('The verification code has been sent to your email.'))
            else:
                if not code:
                    raise ValidationError(_('Enter verification code.'))
                elif code != valid_code:
                    raise ValidationError(_("The verification code doesn't match."))
        return email
