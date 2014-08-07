# -*- coding: utf-8 -*-

# (The MIT License)
#
# Copyright (c) 2014 Kura
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the 'Software'), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import requests

from .exceptions import YargException, YargHTTPError
from .package import json2package


def get(package_name, pypi_server="https://pypi.python.org/pypi/"):
    """
    Constructs a request to the PyPI server and returns a :class:`Package <Package>`.

    :param package_name: case sensitive name of the package on the PyPI server.
    :param pypi_server: (option) URL to the PyPI server.

    Usage:

        >>> import yarg
        >>> package = yarg.get('yarg')
        <Package yarg>
    """
    if not pypi_server.endswith("/"):
        pypi_server = pypi_server + "/"
    try:
        response = requests.get("{0}{1}/json".format(pypi_server,
                                                     package_name))
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        if e.status_code == 404:
            raise YargHTTPError(msg="404 Package not found")
    return json2package(response.content)
