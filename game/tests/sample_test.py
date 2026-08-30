import pytest
from pytest import approx, raises
from contextlib import nullcontext as NoError

from ..source.sample import sample_function

@pytest.mark.parametrize("a, b, expected_result", [
    (1, 2, NoError(approx(3.0))),
    (0, 0, NoError(approx(0.0))),
    (0.001, 0, NoError(approx(0.001, abs=1e-3))),
    ("a", 2, raises(TypeError)),
])

def test_sample_function(a, b, expected_result):
    with expected_result as e:
        assert sample_function(a, b) == e