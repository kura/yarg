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


try:
    import simplejson as json
except ImportError:
    import json

from collections import namedtuple

from .release import Release


class Package(object):

    def __init__(self, pypi_dict):
        self._package = pypi_dict['info']
        self._releases = pypi_dict['releases']

    def __repr__(self):
        return "<Package {0}>".format(self.name)

    @property
    def name(self):
        return self._package['name']

    @property
    def pypi_url(self):
        return self._package['info']['url']

    @property
    def summary(self):
        return self._package['summary']

    @property
    def description(self):
        return self._package['description']

    @property
    def homepage(self):
        if self._package['home_page'] == "":
            return None
        return self._package['home_page']

    @property
    def bugtracker(self):
        if self._package['bugtrack_url'] == "":
            return None
        return self._package['bugtrack_url']

    @property
    def docs(self):
        if self._package['docs_url'] == "":
            return None
        return self._package['docs_url']

    @property
    def version(self):
        return self._package['version']

    @property
    def author(self):
        author = namedtuple('Author', 'name email')
        return author(name=self._package['author'],
                      email=self._package['author_email'])

    @property
    def maintainer(self):
        maintainer = namedtuple('Maintainer', 'name email')
        return author(name=self._package['maintainer'],
                      email=self._package['maintainer_email'])

    @property
    def license(self):
        return self._package['license']

    @property
    def license_from_classifier(self):
        if len(self.classifiers) > 0:
            for c in self.classifiers:
                if c.startswith("License"):
                    return c.split(" :: ")[-1]

    @property
    def downloads(self):
        _downloads = self._package['downloads']
        downloads = namedtuple('Downloads', 'day week month')
        return downloads(day=_downloads['last_day'],
                         week=_downloads['last_week'],
                         month=_downloads['last_month'])

    @property
    def classifiers(self):
        return self._package['classifiers']

    @property
    def release_ids(self):
        r = [k for k in self._releases.keys() if len(self._releases[k]) > 0 ]
        return sorted(r)

    def release(self, release_id):
        if release_id not in self.release_ids:
            raise
        return [Release(r, self._releases[r]) for r in self.release_ids]


def json2package(json_content):
    return Package(json.loads(json_content))
