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

    def test_repr(self):
        self.assertEqual(u'<Package yarg>', self.package.__repr__())

    def test_name(self):
        self.assertEqual(u'yarg', self.package.name)

    def test_pypi_url(self):
        self.assertEqual(u'http://pypi.python.org/pypi/yarg',
                          self.package.pypi_url)

    def test_summary(self):
        self.assertEqual(u'This is the short summary.', self.package.summary)

    def test_description(self):
        self.assertEqual(u'This is the long description.',
                          self.package.description)

    def test_homepage(self):
        self.assertEqual(u'https://kura.io/yarg/',
                          self.package.homepage)

    def test_bugtracker(self):
        self.assertEqual(u'https://github.com/kura/yarg/issues',
                          self.package.bugtracker)

    def test_docs(self):
        self.assertEqual(u'http://yarg.readthedocs.org/',
                          self.package.docs)

    def test_author(self):
        author = namedtuple('Author', 'name email')
        self.assertEqual(author(name='Kura', email='kura@kura.io'),
                          self.package.author)

    def test_maintainer(self):
        maintainer = namedtuple('Maintainer', 'name email')
        self.assertEqual(maintainer(name='Kura', email='kura@kura.io'),
                          self.package.maintainer)

    def test_license(self):
        self.assertEqual(u'MIT',
                          self.package.license)

    def test_license_from_classifiers(self):
        self.assertEqual(u'MIT License',
                          self.package.license_from_classifiers)

    def test_downloads(self):
        downloads = namedtuple('Downloads', 'day week month')
        self.assertEqual(downloads(day=34001, week=72700, month=510000),
                          self.package.downloads)

    def test_classifiers(self):
        self.assertEqual([u'Development Status :: 5 - Production/Stable',
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
        self.assertEqual([u'0.0.0', u'0.0.2', u'0.0.15'],
                          self.package.release_ids)

    def test_latest_release_id(self):
        self.assertEqual(u'0.0.15', self.package.latest_release_id)

    def test_has_wheel(self):
        self.assertEqual(True, self.package.has_wheel)

    def test_has_egg(self):
        self.assertEqual(False, self.package.has_egg)

    def test_has_source(self):
        self.assertEqual(True, self.package.has_source)

    def test_python_versions(self):
        self.assertEqual([u'2.6', u'2.7', u'3.1', u'3.2', u'3.3'],
                          self.package.python_versions)

    def test_python_implementations(self):
        self.assertEqual([u'CPython', u'PyPy'],
                          self.package.python_implementations)


class TestPackageMissingData(unittest.TestCase):

    def setUp(self):
        package = os.path.join(os.path.dirname(__file__),
                               'package_no_homepage_bugtrack_one_release.json')
        self.json = json.loads(open(package).read())
        self.package = json2package(open(package).read())


    def test_homepage(self):
        self.assertEqual(None, self.package.homepage)

    def test_bugtracker(self):
        self.assertEqual(None, self.package.bugtracker)

    def test_docs(self):
        self.assertEqual(None, self.package.docs)

    def test_latest_release_id(self):
        self.assertEqual(u'0.0.0', self.package.latest_release_id)

    def test_has_wheel(self):
        self.assertEqual(False, self.package.has_wheel)

    def test_has_egg(self):
        self.assertEqual(True, self.package.has_egg)

    def test_has_source(self):
        self.assertEqual(False, self.package.has_source)
