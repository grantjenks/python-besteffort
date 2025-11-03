# python-besteffort

Best-effort execution of Python modules by rewriting their bytecode at import
time so that every statement executes inside a ``contextlib.suppress`` block.

## Usage

```python
import besteffort  # installs the importer on sys.meta_path

# ``yourmodule`` is an example module shipped with the project. Importing it through
# ``besteffort`` returns a wrapped version where each statement is guarded by
# ``contextlib.suppress(Exception)``.
from besteffort import yourmodule

yourmodule.example("G")
```

The wrapped module behaves as if ``with suppress(Exception):`` surrounded each
statement. Lines that raise simply fail closed and execution continues.

### Decorating a single function

```python
from besteffort import besteffort


@besteffort
def fragile(value: int) -> int:
    print("before divide")
    value /= 0
    print("after divide")
    return value


fragile(10)
```

Only the decorated function is rewritten, allowing the rest of the module to
run normally. Use ``@besteffort`` as the innermost decorator when stacking it
with others.

## Limitations

* Only rewrites Python source (``.py``). Built-ins and C extensions cannot be
  transformed.
* Top-level module code is not wrapped; if a module raises at import time,
  importing via ``besteffort`` will still fail.
* Relative imports from the instrumented module work by setting
  ``__package__`` to the original package; absolute imports inside the module
  load the normal (unmodified) dependencies.
