"""Pytest configuration for the test-suite."""

from __future__ import annotations

import sys
from pathlib import Path

# Ensure the example module lives only under ``tests/`` while remaining importable.
# The tests import ``besteffort.yourmodule`` which in turn needs the original
# ``yourmodule`` module to be discoverable on ``sys.path``.
_TESTS_DIR = Path(__file__).parent
if str(_TESTS_DIR) not in sys.path:
    sys.path.insert(0, str(_TESTS_DIR))
