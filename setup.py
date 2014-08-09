import re
from setuptools import setup
from setuptools import find_packages
import sys


version = __import__('yarg').__version__
desc = "A semi hard Cornish cheese, also queries PyPI (PyPI client)"
long_desc = open('README.rst').read() + "\n\n" + open('CHANGES.rst').read()
long_desc = re.sub(r":[a-z]*:", "", long_desc)


setup(name='yarg',
      version=version,
      url="https://yarg.readthedocs.org/",
      author="Kura",
      author_email="kura@kura.io",
      maintainer="Kura",
      maintainer_email="kura@kura.io",
      description=desc,
      long_description=long_desc,
      license='MIT',
      platforms=['linux'],
      packages=find_packages(exclude=["*.tests"]),
      install_requires=['requests', ],
      requires=['requests', ],
      provides=['yarg', ],
      keywords=['pypi', 'client', 'packages'],
      classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Archiving :: Packaging',
      ],
      zip_safe=True,
      )
