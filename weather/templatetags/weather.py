from datetime import datetime as dt

from django import template

register = template.Library()


def unix_ts(timestamp):
    try:
        return dt.utcfromtimestamp(timestamp).strftime("%-H:%-M:%-S")
    except (TypeError, ValueError):
        return None


def weather_icon(icon_code):
    return f"https://openweathermap.org/img/wn/{icon_code}@2x.png"


register.filter(unix_ts)
register.filter(weather_icon)
