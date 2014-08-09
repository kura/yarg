import unittest

from yarg import HTTPError


class TestHTTPError(unittest.TestCase):

    def setUp(self):
        self.error = HTTPError(status_code=300,
                               reason="Test")

    def test_repr(self):
        self.assertEqual('300 Test', self.error.__repr__())

    def test_str(self):
        self.assertEqual('300 Test', self.error.__str__())
