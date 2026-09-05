from contextlib import nullcontext as NoError

import pytest
from pytest import approx, raises

from test_game.load_asset import _conv_int, load_textures, lookup_texture


@pytest.mark.parametrize(
    "val, expected_result", [("1", NoError(approx(1))), (2.0, NoError(approx(2))), ("a", raises(ValueError))]
)
def test_conv_int(val, expected_result):
    with expected_result as e:
        assert _conv_int(val) == e


def test_load_textures():
    assert load_textures()


@pytest.mark.parametrize(
    "pack, name, expected_result",
    [
        ("bg_elements", "castle.png", NoError()),
        ("bg_elemets", "castle.png", raises(LookupError)),
        ("bg_elements", "cast.png", raises(LookupError)),
    ],
)
def test_lookup_texture(pack, name, expected_result):
    textures = load_textures()
    with expected_result:
        assert lookup_texture(textures, pack, name)
