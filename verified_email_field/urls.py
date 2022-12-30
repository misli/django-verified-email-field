from django.conf.urls import url

from . import views

app_name = "verified-email-field"

urlpatterns = [
    url(r"^send/(?P<fieldsetup_id>[^/]+)/$", views.send, name="send"),
]
