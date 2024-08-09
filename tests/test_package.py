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
        self.assertEqual('<Package yarg>', self.package.__repr__())

    def test_name(self):
        self.assertEqual('yarg', self.package.name)

    def test_pypi_url(self):
        self.assertEqual('http://pypi.python.org/pypi/yarg',
                          self.package.pypi_url)

    def test_summary(self):
        self.assertEqual('This is the short summary.', self.package.summary)

    def test_description(self):
        self.assertEqual('This is the long description.',
                          self.package.description)

    def test_homepage(self):
        self.assertEqual('https://kura.io/yarg/',
                          self.package.homepage)

    def test_bugtracker(self):
        self.assertEqual('https://github.com/kura/yarg/issues',
                          self.package.bugtracker)

    def test_docs(self):
        self.assertEqual('http://yarg.readthedocs.org/',
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
        self.assertEqual('MIT',
                          self.package.license)

    def test_license_from_classifiers(self):
        self.assertEqual('MIT License',
                          self.package.license_from_classifiers)

    def test_downloads(self):
        downloads = namedtuple('Downloads', 'day week month')
        self.assertEqual(downloads(day=34001, week=72700, month=510000),
                          self.package.downloads)

    def test_classifiers(self):
        self.assertEqual(['Development Status :: 5 - Production/Stable',
                          'Intended Audience :: Developers',
                          'License :: OSI Approved :: MIT License',
                          'Programming Language :: Python',
                          'Programming Language :: Python :: 2.6',
                          'Programming Language :: Python :: 2.7',
                          'Programming Language :: Python :: 3',
                          'Programming Language :: Python :: 3.1',
                          'Programming Language :: Python :: 3.2',
                          'Programming Language :: Python :: 3.3',
                          'Programming Language :: Python :: Implementation :: CPython',
                          'Programming Language :: Python :: Implementation :: PyPy'],
                         self.package.classifiers)

    def test_release_ids(self):
        self.assertEqual(['0.0.0', '0.0.2', '0.0.15'],
                          self.package.release_ids)

    def test_latest_release_id(self):
        self.assertEqual('0.0.15', self.package.latest_release_id)

    def test_has_wheel(self):
        self.assertEqual(True, self.package.has_wheel)

    def test_has_egg(self):
        self.assertEqual(False, self.package.has_egg)

    def test_has_source(self):
        self.assertEqual(True, self.package.has_source)

    def test_python_versions(self):
        self.assertEqual(['2.6', '2.7', '3.1', '3.2', '3.3'],
                          self.package.python_versions)

    def test_python_implementations(self):
        self.assertEqual(['CPython', 'PyPy'],
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
        self.assertEqual('0.0.0', self.package.latest_release_id)

    def test_has_wheel(self):
        self.assertEqual(False, self.package.has_wheel)

    def test_has_egg(self):
        self.assertEqual(True, self.package.has_egg)

    def test_has_source(self):
        self.assertEqual(False, self.package.has_source)
