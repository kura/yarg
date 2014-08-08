Release History
===============

0.1.2 (2014-08-08)
------------------

Bug fixes
~~~~~~~~~

- `yarg.get` will now raise an Exception for errors **including**
  300 and above. Previously on raised for above 300.
- Fix an issue on Python 3.X and PyPy3 where `HTTPError` was using
  a method that was removed in Python 3.
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

- New `Package` property `has_wheel`.
- New `Package` property `has_egg`.
- New `Package` property `has_source`.
- New `Package` property `python_versions`.
- New `Package` property `python_implementations`.
- Added `HTTPError` to `yarg.__init__` for easier access.
- Added `json2package` to `yarg.__init__` to expose it for use.

0.1.0 (2014-08-08)
------------------

- Initial release
