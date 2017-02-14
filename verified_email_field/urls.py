from __future__ import unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^send/(?P<fieldsetup_id>\w+)/$', views.send, name='send'),
]
