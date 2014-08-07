import requests

from .exceptions import YargException, YargHTTPError
from .package import jsonpackage


def get(package, pypi="https://pypi.python.org/pypi/"):
    if not pypi.endswith("/"):
        pypi = pypip + "/"
    try:
        response = requests.get("{0}{1}/json".format(pypi, package))
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        if e.status_code == 404:
            raise YargHTTPError(msg="404 Package not found")
    return jsonpackage(response.content)
