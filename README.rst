yarg(1) -- A semi hard Cornish cheese, also queries PyPI
========================================================

Yarg is a PyPI client.

.. code-block:: python

    >>> import yarg
    >>> package = yarg.get("yarg")
    >>> package.name
    u'yarg'
    >>> package.author
    Author(name=u'Kura', email=u'kura@kura.io')

Full documentation is at <http://yarg.readthedocs.org>.
