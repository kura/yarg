Testing
=======

Yarg uses the built-in `unittest` framework for Python and uses `pytest` as the
test rig.

Running the tests using the Makefile
------------------------------------

A target has been made available in the project's `Makefile` for running the
test rig, it will install all requirements for testing and run the tests.

.. code-block:: bash

    make test

Running the tests without using the Makefile
--------------------------------------------

.. code-block:: bash

    pip install -r requirements-test.txt
    pytest

Running the tests with tox/detox
--------------------------------

A `tox` configuration is also provided if you'd like to run the test rig
against all the supported Python versions.

You can do this via the `Makefile` target that will install all requirements
and run the tests:

.. code-block:: bash

    make tox

Or you can do it manually:

.. code-block:: bash

    pip install -r requirements.txt -r requirements-test.txt
    detox
