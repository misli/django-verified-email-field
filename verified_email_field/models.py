from __future__ import unicode_literals

from django.db import models

from . import forms


class VerifiedEmailField(models.EmailField):

    def formfield(self, **kwargs):
        defaults = {
            'form_class': forms.VerifiedEmailField,
        }
        defaults.update(kwargs)
        return super(VerifiedEmailField, self).formfield(**defaults)
