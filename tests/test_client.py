import os
import unittest

from unittest.mock import call, MagicMock, patch

from yarg import get, HTTPError


class GoodResponse:
    status_code = 200
    package = os.path.join(os.path.dirname(__file__),
                           'package.json')
    content = open(package).read()


class BadResponse:
    status_code = 300
    reason = "Mocked"


class TestClient(unittest.TestCase):

    @patch('requests.Session.get', return_value=BadResponse)
    def test_get(self, get_mock):
        # Python 2.6....
        try:
            get("test")
        except HTTPError as e:
            self.assertEqual(300, e.status_code)
            self.assertEqual(e.status_code, e.errno)
            self.assertEqual(e.reason, e.message)

    @patch('requests.Session.get', return_value=GoodResponse)
    def test_end_slash(self, get_mock):
        get("test", pypi_server="https://mock.test.mock/test")
        self.assertEqual(call('https://mock.test.mock/test/test/json'),
                         get_mock.call_args)
