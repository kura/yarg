from requests.exceptions import HTTPError


class YargException(Exception):
    pass


class YargHTTPError(YargException):

    def __init__(self, *args, **kwargs):
        self.msg = kwargs.pop('msg', None)
