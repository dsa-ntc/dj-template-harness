from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path(
        "recurring-update/",
        TemplateView.as_view(template_name="recurring_update.html"),
        name="recurring_update",
    ),
]
