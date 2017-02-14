from __future__ import unicode_literals

from django.conf import settings
from django.utils.translation import ugettext_lazy as _

CACHE_PREFIX = getattr(settings, 'VERIFIED_EMAIL_CACHE_PREFIX', 'verified_email_field_')
CODE_LENGTH = int(getattr(settings, 'VERIFIED_EMAIL_CODE_LENGTH', 6))
CODE_TTL = int(getattr(settings, 'VERIFIED_EMAIL_CODE_TTL', 300))
MAIL_FROM = getattr(settings, 'VERIFIED_EMAIL_MAIL_FROM', settings.SERVER_EMAIL)
MAIL_SUBJECT = getattr(settings, 'VERIFIED_EMAIL_MAIL_SUBJECT', _('Verification code'))
MAIL_TEMPLATE_TXT = getattr(settings, 'VERIFIED_EMAIL_MAIL_TEMPLATE_TXT', 'verified_email_field/mail.txt')
MAIL_TEMPLATE_HTML = getattr(settings, 'VERIFIED_EMAIL_MAIL_TEMPLATE_TXT', 'verified_email_field/mail.html')
MAIL_MAILER = getattr(settings, 'VERIFIED_EMAIL_MAIL_MAILER',
                      'Django Verified Email Field (https://github.com/misli/django-verified-email-field)')
