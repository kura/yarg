.. Yarg documentation master file

Yarg: A PyPI client
===================

.. image:: http://img.shields.io/travis/kura/yarg.svg?style=flat

.. image:: http://img.shields.io/coveralls/kura/yarg.svg?style=flat

.. image:: https://pypip.in/version/yarg/badge.svg?style=flat

.. image:: https://pypip.in/download/yarg/badge.svg?style=flat

.. image:: https://pypip.in/py_versions/yarg/badge.svg?style=flat

.. image:: https://pypip.in/implementation/yarg/badge.svg?style=flat

.. image:: https://pypip.in/status/yarg/badge.svg?style=flat

.. image:: https://pypip.in/wheel/yarg/badge.svg?style=flat

.. image:: https://pypip.in/license/yarg/badge.svg?style=flat

yarg(1) -- A semi hard Cornish cheese, also queries PyPI.
Built on top of `requests
<http://docs.python-requests.org/en/latest/>`_, it's
easy to use and makes sense.

.. code-block:: python

    >>> import yarg
    >>> package = yarg.get("yarg")
    >>> package.name
    u'yarg'
    >>> package.author
    Author(name=u'Kura', email=u'kura@kura.io')

Yarg documentation
------------------

.. toctree::
   :maxdepth: 2

   intro
   api

Changelog
---------

.. toctree::
    :maxdepth: 2

    changelog

Contributors
------------

.. toctree::
    :maxdepth: 2

    contributors.rst

Help
----

.. toctree::
    :maxdepth: 2

    faq
