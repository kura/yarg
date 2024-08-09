FAQ
===

My package isn't being found
----------------------------

PyPI is cAsE sEnsItIvE, make sure you're looking for the package with
the correct case.

.. code-block:: python

    >>> yarg.get('Yarg')
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "yarg/client.py", line 52, in get
        reason=response.reason)
    yarg.exceptions.HTTPError: 404 Not Found

    >>> yarg.get('yarg')
    <Package yarg>


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
    'http://pythonhosted.org//yarg'

Why is my `bugtracker` url empty?
---------------------------------

A: This does not seem to work when being set through setup.py, if you
go to your package on PyPI and click edit, one of the available fields
is called *bugtrack url*.
