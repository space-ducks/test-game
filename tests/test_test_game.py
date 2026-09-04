"""
Tests for `test_game` package.

Standard Formatting
-------------------

import pytest
from pytest import approx, raises
from contextlib import nullcontext as NoError

import test_game

```python
@python.mark.parametrize("arg1, arg2, expected", [
    (1, 2, NoError(approx(3.0, abs=1))),
    ("a", 2, raises(TypeError))
])

def test_func_name(arg1, arg2, expected):
    with expected as e:
        assert func_name(arg1, arg2) == e

```
"""

import test_game


def test_import():
    """Verify the package can be imported."""
    assert test_game