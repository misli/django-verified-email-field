from __future__ import unicode_literals

from datetime import timedelta
from random import randint

from django.core.cache import cache
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.utils.timezone import now


def get_code(email, fieldsetup):
    try:
        expiration_time, code = cache.get(fieldsetup.cache_prefix + email)
    except:
        return None
    return code if expiration_time >= now() else None


def send_code(email, fieldsetup):
    # create code and expiration time
    context = dict(fieldsetup.mail_context)
    context['code'] = (get_code(email, fieldsetup) or
                       str(randint(10 ** (fieldsetup.code_length - 1), 10 ** fieldsetup.code_length - 1)))
    context['expiration_time'] = now() + timedelta(0, fieldsetup.code_ttl)
    # store code and expiration time in cache
    cache.set(fieldsetup.cache_prefix + email, (context['expiration_time'], context['code']))
    # create message
    msg = EmailMultiAlternatives(
        subject=fieldsetup.mail_subject,
        body=get_template(fieldsetup.mail_template_txt).render(context),
        from_email=fieldsetup.mail_from,
        to=[email],
        headers={'X-Mailer': fieldsetup.mail_mailer},
    )
    msg.attach_alternative(get_template(fieldsetup.mail_template_html).render(context), 'text/html')
    msg.send()
