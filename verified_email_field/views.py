from __future__ import unicode_literals

from django.http import (
    HttpResponse, HttpResponseBadRequest, HttpResponseNotFound,
)
from django.views.decorators.http import require_POST

from .fieldsetup import fieldsetups
from .forms import SendForm
from .utils import send_code


@require_POST
def send(request, fieldsetup_id):
    try:
        fieldsetup = fieldsetups[fieldsetup_id]
    except KeyError:
        return HttpResponseNotFound()
    form = SendForm(data=request.POST)
    if not form.is_valid():
        return HttpResponseBadRequest()
    send_code(form.cleaned_data['email'], fieldsetup)
    return HttpResponse()
