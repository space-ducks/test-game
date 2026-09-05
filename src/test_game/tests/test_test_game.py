import pytest
from pytest import approx, raises
from contextlib import nullcontext as NoError

import test_game

def test_import():
    # Verify the package can be imported.
    assert test_game