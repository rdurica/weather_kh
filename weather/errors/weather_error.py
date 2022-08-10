class WeatherError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__("Communication error. Please, try again later")
