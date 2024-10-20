import os

import requests

from weather.services.openweather_exceptions import (
    OpenWeatherServerError,
    OpenWeatherSubscriptionError,
    OpenWeatherRequestError,
    OpenWeatherKeyError,
    OpenWeatherUnknownError
)

LOCATION_LIMIT = 5

class OpenWeatherService:
    API_KEY = os.getenv('OPENWEATHER_API_KEY')
    API_ERROR_CODES_EXCEPTIONS = {
        400: OpenWeatherRequestError,
        401: OpenWeatherKeyError,
        404: OpenWeatherRequestError,
        429: OpenWeatherSubscriptionError,
        500: OpenWeatherServerError,
        502: OpenWeatherServerError,
        503: OpenWeatherServerError,
        504: OpenWeatherServerError,
    }

    def get_locations_by_name(self, name):
        response = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={name}'
                            f'&limit={LOCATION_LIMIT}&appid={self.API_KEY}')

        content = response.json()

        if response.status_code // 100 == 2:
            return content

        raise self.API_ERROR_CODES_EXCEPTIONS.get(response.status_code, OpenWeatherUnknownError(content.get('message')))