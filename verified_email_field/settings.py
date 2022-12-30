import os

from django.conf import settings
from django.utils.translation import gettext_lazy as _


def _get_setting(name, default):
    attr = f"VERIFIED_EMAIL_{name}"
    return os.environ.get(attr, getattr(settings, attr, default))


CACHE_PREFIX = _get_setting("CACHE_PREFIX", "verified_email_field_")
CODE_LENGTH = int(_get_setting("CODE_LENGTH", 6))
CODE_TTL = int(_get_setting("CODE_TTL", 300))
MAIL_FROM = _get_setting("MAIL_FROM", settings.SERVER_EMAIL)
MAIL_SUBJECT = _get_setting("MAIL_SUBJECT", _("Verification code"))
MAIL_TEMPLATE_TXT = _get_setting("MAIL_TEMPLATE_TXT", "verified_email_field/mail.txt")
MAIL_TEMPLATE_HTML = _get_setting("MAIL_TEMPLATE_TXT", "verified_email_field/mail.html")
MAIL_MAILER = _get_setting(
    "MAIL_MAILER",
    "Django Verified Email Field (https://github.com/misli/django-verified-email-field)",
)
CREATE_USER = bool(_get_setting("CREATE_USER", True))
