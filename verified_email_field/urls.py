from __future__ import unicode_literals

from django.conf.urls import url

from . import views

app_name = 'verified-email-field'

urlpatterns = [
    url(r'^send/(?P<fieldsetup_id>\w+)/$', views.send, name='send'),
]
