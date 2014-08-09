Release History
===============

0.1.4 (2014-08-09)
------------------

API changes
~~~~~~~~~~~

 - New :meth:`yarg.newest_packages` for querying new packages
   from the PyPI RSS feed.
 - New :meth:`yarg.latest_updated_packages` for querying
   the latest updated packages from the PyPI RSS feed.

Other
~~~~~

- Additional test coverage
- Additional documentation coverage

0.1.2 (2014-08-08)
------------------

Bug fixes
~~~~~~~~~

- :meth:`yarg.get` will now raise an Exception for errors **including**
  300 and above. Previously only raised for above 300.
- Fix an issue on Python 3.X and PyPy3 where
  :class:`yarg.exceptions.HTTPError` was using a method that was
  removed in Python 3.
- Added dictionary key lookups for `home_page`, `bugtrack_url`
  and `docs_url`. Caused `KeyError` exceptions if they were not
  returned by PyPI.

Other
~~~~~

- More test coverage.

0.1.1 (2014-08-08)
------------------

API changes
~~~~~~~~~~~

- New :class:`yarg.package.Package` property `has_wheel`.
- New :class:`yarg.package.Package` property `has_egg`.
- New :class:`yarg.package.Package` property `has_source`.
- New :class:`yarg.package.Package` property `python_versions`.
- New :class:`yarg.package.Package` property `python_implementations`.
- Added :class:`yarg.exceptions.HTTPError` to :module:`yarg.__init__` for easier access.
- Added :meth:`yarg.package.json2package` to :module:`yarg.__init__` to expose it for use.

0.1.0 (2014-08-08)
------------------

- Initial release
