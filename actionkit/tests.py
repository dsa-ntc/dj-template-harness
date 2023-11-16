from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse


class RecurringUpdateViewTestCase(TestCase):
    def test_recurring_update_view(self):
        url = reverse("recurring-update")
        response = self.client.get(url)
        assert response.status_code == HTTPStatus.OK
        self.assertContains(response, "<h2>Page Title</h2>")
