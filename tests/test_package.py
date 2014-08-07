from collections import namedtuple
import json
import os
import unittest

from yarg.package import json2package


class TestPackage(unittest.TestCase):

    def setUp(self):
        package = os.path.join(os.path.dirname(__file__),
                               'package.json')
        self.json = json.loads(open(package).read())
        self.package = json2package(open(package).read())

    def test_name(self):
        self.assertEquals(u'yarg', self.package.name)

    def test_pypi_url(self):
        self.assertEquals(u'http://pypi.python.org/pypi/yarg',
                          self.package.pypi_url)

    def test_summary(self):
        self.assertEquals(u'This is the short summary.', self.package.summary)

    def test_description(self):
        self.assertEquals(u'This is the long description.',
                          self.package.description)

    def test_homepage(self):
        self.assertEquals(u'https://kura.io/yarg/',
                          self.package.homepage)

    def test_bugtracker(self):
        self.assertEquals(u'https://github.com/kura/yarg/issues',
                          self.package.bugtracker)

    def test_docs(self):
        self.assertEquals(u'http://yarg.readthedocs.org/',
                          self.package.docs)

    def test_author(self):
        author = namedtuple('Author', 'name email')
        self.assertEquals(author(name='Kura', email='kura@kura.io'),
                          self.package.author)

    def test_maintainer(self):
        maintainer = namedtuple('Maintainer', 'name email')
        self.assertEquals(maintainer(name='Kura', email='kura@kura.io'),
                          self.package.maintainer)

    def test_license(self):
        self.assertEquals(u'MIT',
                          self.package.license)

    def test_license_from_classifiers(self):
        self.assertEquals(u'MIT License',
                          self.package.license_from_classifiers)

    def test_downloads(self):
        downloads = namedtuple('Downloads', 'day week month')
        self.assertEquals(downloads(day=34001, week=72700, month=510000),
                          self.package.downloads)

    def test_classifiers(self):
        self.assertEquals([u'Development Status :: 5 - Production/Stable',
                          u'Intended Audience :: Developers',
                          u'License :: OSI Approved :: MIT License',
                          u'Programming Language :: Python',
                          u'Programming Language :: Python :: 2.6',
                          u'Programming Language :: Python :: 2.7',
                          u'Programming Language :: Python :: 3',
                          u'Programming Language :: Python :: 3.1',
                          u'Programming Language :: Python :: 3.2',
                          u'Programming Language :: Python :: 3.3',
                          u'Programming Language :: Python :: Implementation :: CPython',
                          u'Programming Language :: Python :: Implementation :: PyPy'],
                         self.package.classifiers)

    def test_release_ids(self):
        self.assertEquals([u'0.0.0', u'0.0.2'], self.package.release_ids)

    def test_latest_release_id(self):
        self.assertEquals(u'0.0.2', self.package.latest_release_id)
