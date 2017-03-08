from __future__ import unicode_literals

from django import forms
from django.core.urlresolvers import reverse
from django.forms.widgets import EmailInput, MultiWidget, TextInput
from django.templatetags.static import static
from django.utils.html import format_html


class VerifiedEmailWidget(MultiWidget):
    def __init__(self, send_label, fieldsetup_id, email_attrs, code_attrs):
        self.send_label = send_label
        self.fieldsetup_id = fieldsetup_id
        widgets = (EmailInput(attrs=email_attrs), TextInput(attrs=code_attrs))
        super(VerifiedEmailWidget, self).__init__(widgets)

    @property
    def media(self):
        return forms.Media(js=[static('verified_email_field/send.js')])

    def decompress(self, value):
        if value:
            raise Exception(value)
        return [None, None]

    def render(self, name, value, attrs=None):
        self.name = name
        if not attrs:
            attrs = {}
        attrs['class'] = attrs['class'] + ' form-control' if 'class' in attrs else 'form-control'
        return super(VerifiedEmailWidget, self).render(name, value, attrs)

    def format_output(self, rendered_widgets):
        return ''.join((
            rendered_widgets[0],
            '<div class="input-group">',
            '<span class="input-group-btn">',
            format_html(
                '<button class="btn btn-default" type="button" '
                'onclick="send_verification_code(\'{}\', \'{}\')">{}</button>',
                self.name,
                reverse('verified-email-field:send', args=(self.fieldsetup_id,)),
                self.send_label,
            ),
            '</span>',
            rendered_widgets[1],
            '</div>',
        ))
