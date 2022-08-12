import os
from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse


class TestHomepageView(TestCase):
    def setUp(self) -> None:
        from django.conf import settings

        settings.SECRET_KEY = "test"

    def test_homepage_available(self):
        response = self.client.get(reverse("weather:home"))
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_homepage_no_data(self):
        response = self.client.get(reverse("weather:home"))
        self.assertContains(response, "Communication error. Please, try again later.")
