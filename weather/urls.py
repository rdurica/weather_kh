from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.urls import path
from django.views.decorators.cache import cache_page

from weather.views import HomePage

CACHE_TTL = getattr(settings, "CACHE_TTL", DEFAULT_TIMEOUT)

app_name: str = "weather"
urlpatterns = [
    path("", cache_page(CACHE_TTL)(HomePage.as_view()), name="home"),
]
