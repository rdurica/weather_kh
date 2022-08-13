# Weather in Kutná Hora
[![Python 3.10](https://img.shields.io/badge/python-3.1O-blue.svg)](https://www.python.org/downloads/release/python-310/)
[![Django](https://img.shields.io/badge/django-4.1-blue.svg)](https://www.djangoproject.com/)
[![GitHub license](https://badgen.net/github/license/Naereen/Strapdown.js)](https://github.com/Naereen/StrapDown.js/blob/master/LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Summary
Django application which shows actual weather and forecast for Kutná Hora. Openweather API provide weather information.

## Screens
Actual weather:
![Screenshot 2022-08-13 at 22 40 17](https://user-images.githubusercontent.com/16089770/184510088-7dce230d-233d-4b2e-a81e-a2bdf9947980.png)

Forecast:
![Screenshot 2022-08-13 at 22 40 41](https://user-images.githubusercontent.com/16089770/184510091-ddc6e546-e906-410e-b83b-5629c7a6928f.png)

## Web
Production ready application is available at [weatherkh.robbyte.net](https://weatherkh.robbyte.net)

## Installation
Example docker-compose file. For production use change volumes, keys and setup correct docker network
```yml
version: '3'

services:
  weather-kh:
    image: docker.robbyte.net/weather-kh:0.2.6
    container_name: weather-kh
    ports:
      - 8000:8000
    volumes:
      - /app/weather-kh/logs/:/var/log/
      - /app/weather-kh/static:/app/static
    environment:
      - DEBUG=False
      - SECRET_KEY=top-secret-key
      - WEATHER_API_KEY=your-api-key
    restart: always
```

## License
This project is licensed under the terms of the MIT license.