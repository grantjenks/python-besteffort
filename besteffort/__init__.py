"""Public entry point for the :mod:`besteffort` importer.

Importing :mod:`besteffort` installs the meta path finder that rewrites a
module's abstract syntax tree so that every statement executes inside a
``contextlib.suppress`` block, allowing functions to keep running even when
exceptions occur.
"""

from __future__ import annotations

from . import core as _core


def install() -> None:
    """Install the best-effort importer on :data:`sys.meta_path`."""

    _core.install()


install()

del _core

__all__ = ["install"]
