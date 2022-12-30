from django import forms
from django.forms.widgets import EmailInput, MultiWidget, TextInput
from django.templatetags.static import static


class VerifiedEmailWidget(MultiWidget):
    template_name = "verified_email_field/field.html"

    def __init__(self, attrs=None, email_attrs=None, code_attrs=None, **context):
        self.context = context
        widgets = (EmailInput(attrs=email_attrs), TextInput(attrs=code_attrs))
        super(VerifiedEmailWidget, self).__init__(widgets, attrs)

    @property
    def media(self):
        return forms.Media(js=[static("verified_email_field/send.js")])

    def decompress(self, value):
        if value:
            return [value, None]
        return [None, None]

    def get_context(self, name, value, attrs):
        context = super(VerifiedEmailWidget, self).get_context(name, value, attrs)
        context.update(self.context)
        return context
