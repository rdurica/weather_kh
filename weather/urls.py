from django.urls import path

from weather.views import HomePage

app_name: str = "weather"
urlpatterns = [
    path("", HomePage.as_view(), name="home"),
]
