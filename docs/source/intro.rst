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

.. code-block:: python

    >>> import yarg
    >>> package = yarg.get("yarg")
    >>> package.name
    u'yarg'
    >>> package.author
    Author(name=u'Kura', email=u'kura@kura.io')

:meth:`~yarg.get` returns an instance of :class:`~yarg.package.Package`.
