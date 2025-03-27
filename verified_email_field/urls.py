from django.urls import path

from . import views

app_name = "verified-email-field"

urlpatterns = [
    path("send/<fieldsetup_id>/", views.send, name="send"),
]
