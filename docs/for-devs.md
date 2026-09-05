# For Developers
This section outlines preferred development practices for this project.

## Source Control
The development branch can be changed from the Source Control menu. Each developer should have their own development branch, with sub-branches dedicated to developing indivdual features, as shown below.

- `randy-dev`
    - `feature-dev-1`
- `noah-dev`
    - `feature-dev-2`

To merge a branch, create a Pull Request. Assign all developers to the Pull Request to review it. It is recommended to merge and delete sub-branches, but merge and preserve developer branches.

**All** files should be documented and tested before being merged into the `main` branch.

## Documentation
To document files, open a terminal and enter `just docs-serve`. This will preview docs locally at hhtp://localhost:8000.

Sample format of a docstring for a function is listed below.
```python
def sample_function(a: float, b: float) -> float:
    r"""
    This is a sample function that adds two numbers.

    $$a + b$$
    
    !!! note
        Sample note.
    
    Parameters
    ----------
    a : float
        First number to add.
    b : float
        Second number to add.

    Returns
    -------
    float
        Sum of a and b.
    """
    return a + b
```

## Testing
The `pytest` module will be used for unit tests. Test files should include "test" somewhere in their name for pytest to recognize them. `@pytest.mark.parameterize()` can be used to parameterize test inputs, reducing clutter.

```python
import pytest
from pytest import approx, raises
from contextlib import nullcontext as NoError

# Assume sample function written previously is under game/source as sample.py
from ..source.sample import sample_function

# Parametrize function arguments and expected result
@pytest.mark.parametrize("a, b, expected_result", [
    (1, 2, NoError(approx(3.0))),
    (0.001, 1, NoError(approx(0.001, abs=1e-3))),
    ("a", 2, raises(TypeError))
])

def test_sample_function(a, b, expected_result):
    with expected_result as e:
        assert sample_function(a, b) == e
```

## Notes on File Structure
Top-level folder notes:

- `.github` houses GitHub workflows and templates.
- `docs` houses all documentation-related files.
- `src/test-game` houses all game development files.

Top-level file notes:

- `.editorconfig` gives instructions to `ruff`.
- `.gitignore` tells Source Control which filepaths should not be included in the overall source control management.
- `justfile` gives instructions to `just`.
- `LICENSE` lists the license this project is attributed under.
- `pyproject.toml` contains information about the project.
- `README.md` is the document you're currently reading.
- `SECURITY.md` outlines security measures.
- `zensical.toml` contains `zensical` theme information.