from __future__ import unicode_literals

from django.db import models

from . import forms
from .fieldsetup import VerifiedEmailFieldSetup


class VerifiedEmailField(models.EmailField):

    def __init__(self, *args, **kwargs):
        self.formfield_kwargs = {
            'form_class': forms.VerifiedEmailField,
        }
        for field in VerifiedEmailFieldSetup._fields + ('fieldsetup_id',):
            if field in kwargs:
                self.formfield_kwargs[field] = kwargs.pop(field)
        super(VerifiedEmailField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        for k, v in self.formfield_kwargs.items():
            kwargs.setdefault(k, v)
        return super(VerifiedEmailField, self).formfield(**kwargs)
