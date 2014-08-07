try:
    import simplejson as json
except ImportError:
    import json

from collections import namedtuple


class Package(object):

    def __init__(self, content):
        self._package = content['info']
        self._releases = content['releases']

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


class Release(object):

    def __init__(self, release_id, content):
        self._release = content
        self._release['release_id'] = release_id

    def __repr__(self):
        return "<Release {0}>".format(self.release_id)

    @property
    def realise_id(self):
        return self._release['release_id']


def json2package(json_content):
    return Package(json.loads(json_content))
