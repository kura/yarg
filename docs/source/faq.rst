FAQ
===

Why is my `docs` url empty?
---------------------------

`docs_url` is only available when you're using `pythonhosted.org
<https://pythonhosted.org/>`_.

Why does my `docs` url have an extra slash?
-------------------------------------------

This an issue with PyPI itself, it returns an additional slash inside
the URL to your pythonhosted docs.

.. code-block:: python

    >>> yarg.get('yarg').docs
    u'http://pythonhosted.org//yarg'

Why is my `bugtracker` url empty?
---------------------------------

A: This does not seem to work when being set through setup.py, if you
go to your package on PyPI and click edit, one of the available fields
is called *bugtrack url*.
