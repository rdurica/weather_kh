from django.views import generic

from weather.errors.weather_error import WeatherError
from weather.services.weather_api import WeatherApiService

# Create your views here.


class HomePage(generic.ListView):
    template_name: str = "weather/index.html"
    context_object_name = "data"

    def get_context_data(self, **kwargs):
        data, error_message = None, None
        try:
            data = WeatherApiService.get_weather_data()
        except WeatherError as e:
            error_message = str(e)

        context = {"data": data, "error_message": error_message}
        return context

    def get_queryset(self):
        return None
