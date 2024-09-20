# hypofuzz-pytest-version

Minimal reproduction of https://github.com/Zac-HD/hypofuzz/issues/35

## How to run this example

With hatch:

```console
hatch run hypothesis fuzz
```

Alternatively, with vanilla Python:

```bash
# Setup
python -m venv .venv
source .venv/bin/activate
pip install -e .

# Run
hypothesis fuzz
```

You should see output similar to the following:

```console
=================================================== test session starts ====================================================
platform darwin -- Python 3.12.4, pytest-8.3.3, pluggy-1.5.0
rootdir: /Users/jcj/src/hypofuzz-pytest-version
configfile: pyproject.toml
plugins: dash-2.18.1, hypothesis-6.112.1
collected 1 item

<Dir hypofuzz-pytest-version>
  <Package tests>
    <Module test_anything.py>
      <Function test_anything>
INTERNALERROR> Traceback (most recent call last):
INTERNALERROR>   File ".../site-packages/_pytest/main.py", line 283, in wrap_session
...
INTERNALERROR>   File ".../site-packages/hypofuzz/interface.py", line 40, in pytest_collection_finish
INTERNALERROR>     all_autouse = set(manager._getautousenames(item.nodeid))
INTERNALERROR>                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
INTERNALERROR>   File ".../site-packages/_pytest/fixtures.py", line 1528, in _getautousenames
INTERNALERROR>     for parentnode in node.listchain():
INTERNALERROR>                       ^^^^^^^^^^^^^^
INTERNALERROR> AttributeError: 'str' object has no attribute 'listchain'

================================================ 1 test collected in 0.04s =================================================

Exiting because pytest returned exit code 3
```

## License

`hypofuzz-pytest-version` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
