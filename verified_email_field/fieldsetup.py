from __future__ import unicode_literals

from collections import namedtuple

from . import settings


class VerifiedEmailFieldSetup(namedtuple('VerifiedEmailFieldSetup', (
        'cache_prefix', 'code_length', 'code_ttl', 'mail_from', 'mail_subject',
        'mail_template_txt', 'mail_template_html', 'mail_context', 'mail_mailer'))):
    def __new__(
            cls, cache_prefix=settings.CACHE_PREFIX,
            code_length=settings.CODE_LENGTH, code_ttl=settings.CODE_TTL,
            mail_from=settings.MAIL_FROM, mail_subject=settings.MAIL_SUBJECT,
            mail_template_txt=settings.MAIL_TEMPLATE_TXT, mail_template_html=settings.MAIL_TEMPLATE_HTML,
            mail_context=None, mail_mailer=settings.MAIL_MAILER, **kwargs):
        return super(VerifiedEmailFieldSetup, cls).__new__(
            cls, cache_prefix=cache_prefix,
            code_length=code_length, code_ttl=code_ttl,
            mail_from=mail_from, mail_subject=mail_subject,
            mail_template_txt=mail_template_txt, mail_template_html=mail_template_html,
            mail_context=mail_context or {}, mail_mailer=mail_mailer,
        )


fieldsetups = {}
