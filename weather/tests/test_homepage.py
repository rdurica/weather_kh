from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse


class TestHomepageView(TestCase):
    def test_homepage_available(self):
        response = self.client.get(reverse("weather:home"))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, "Hi")
