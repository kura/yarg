.. Yarg documentation master file

Yarg: A PyPI client
===================

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
