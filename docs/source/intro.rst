Introduction
============

Prerequisites
-------------

Yarg works with Python 2.6.x, 2.7.x, => 3.3, pypy and pypy3.

Installation
------------

There are multiple ways to install Yarg.

As source or as a wheel from PyPI using easy_install or pip:

.. code-block:: bash

    easy_install yarg
    pip install yarg

From the tarball release
------------------------

1. Download the most recent tarball from the `PyPI download
   page <https://pypi.python.org/pypi/yarg>`_
2. Unpack the tarball
3. python setup.py install


Getting started
---------------

Search interface
~~~~~~~~~~~~~~~~

.. code-block:: python

    >>> import yarg
    >>> package = yarg.get("yarg")
    >>> package.name
    'yarg'
    >>> package.author
    Author(name='Kura', email='kura@kura.io')

:meth:`yarg.get` returns an instance of :class:`yarg.package.Package`.

Newest packages interface
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    >>> import yarg
    >>> packages = yarg.newest_packages()
    >>> packages
    [<Package yarg>, <Package gray>, <Package ragy>]
    >>> packages[0].name
    'yarg'
    >>> packages.url
    'http://pypi.python.org/pypi/yarg

:meth:`yarg.newest_packages` returns a list of :class:`yarg.parse.Package`
objects.

Updated packages interface
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    >>> import yarg
    >>> packages = yarg.latest_updated_packages()
    >>> packages
    [<Package yarg>, <Package gray>, <Package ragy>]
    >>> packages[0].name
    'yarg'
    >>> packages[0].version
    '0.1.2'
    >>> packages[0].url
    'http://pypi.python.org/pypi/yarg/0.1.2

:meth:`yarg.latest_updated_packages` returns a list of :class:`yarg.parse.Package`
objects.
