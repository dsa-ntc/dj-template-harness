"""URL Configuration for ActionKit app.

In Django, URL configuration maps templates to views.
"""

from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path("", TemplateView.as_view(template_name="index.html"), name="actionkit"),
    path(
        "recurring-update/",
        TemplateView.as_view(template_name="recurring_update.html"),
        name="recurring_update",
    ),
]
