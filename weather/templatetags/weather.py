from datetime import datetime as dt

from django import template

register = template.Library()


def unix_ts(timestamp):
    try:
        import locale

        locale.setlocale(locale.LC_ALL, "cs_CZ")
        return dt.utcfromtimestamp(timestamp).strftime("%A")
    except (TypeError, ValueError):
        return None


def kmh(ms):
    try:
        return float(ms) / 0.27777777777778
    except (TypeError, ValueError):
        return None


def weather_icon(icon_code):
    return _get_icon_url(icon_code)


def weather_icon_small(icon_code):
    return _get_icon_url(icon_code, 2)


def _get_icon_url(icon_code, size=4):
    return f"https://openweathermap.org/img/wn/{icon_code}@{size}x.png"


register.filter(unix_ts)
register.filter(kmh)
register.filter(weather_icon)
register.filter(weather_icon_small)
