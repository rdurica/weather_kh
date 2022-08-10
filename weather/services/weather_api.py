from http import HTTPStatus
from os import environ as env

import requests
from weather.errors.weather_error import WeatherError


class WeatherApiService:
    API_URL = "https://api.openweathermap.org/data/2.5/onecall"
    API_PARAMS = f"?lat=49.952431&lon=15.268654&lang=cz&exclude=hourly,minutely&units=metric&appid={env.get('WEATHER_API_KEY')}"

    def get_weather_data():
        response = requests.get(
            WeatherApiService.API_URL + WeatherApiService.API_PARAMS
        )

        if response.status_code != HTTPStatus.OK:
            raise WeatherError()

        return response.json
