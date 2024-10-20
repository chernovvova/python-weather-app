class OpenWeatherBaseException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class OpenWeatherServerError(OpenWeatherBaseException):
    def __init__(self, message="There was a problem on remote API side", code=None):
        self.message = message
        self.code = code


class OpenWeatherRequestError(OpenWeatherBaseException):
    def __init__(self, message="There is an issue with your request. Please consult remote API docs", code=None):
        self.message = message
        self.code = code


class OpenWeatherKeyError(OpenWeatherBaseException):
    def __init__(self, message="There is an issue with your API key", code=None):
        self.message = message
        self.code = code


class OpenWeatherSubscriptionError(OpenWeatherBaseException):
    def __init__(self, message="There is subscription error. Please consult remote API terms and conditions", code=None):
        self.message = message
        self.code = code


class OpenWeatherUnknownError(OpenWeatherBaseException):
    def __init__(self, message="There was a problem on remote API side", code=None):
        self.message = message
        self.code = code
