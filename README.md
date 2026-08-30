# Setup
Follow these instructions to set up the project. Assumes VS Code as the IDE.

## Software Installations
If not already installed, install the following software.

- Python: https://www.python.org/downloads/
- VS Code: https://code.visualstudio.com/download
- Git: https://git-scm.com/install/windows

## VS Code Setup
Once installed, open VS Code. Navigate to the Source Control menu on the left sidebar and select **Clone Repository**. If the button does not appear, click on the reload link to reload the window. Sign in with your GitHub credentials (make an account if needed) and make a local clone of the `test-game` repository.

Open a Git Bash terminal and use the following commands to set up your identity. This is required to make commits through VS Code.
- `$ git config --global user.name "Your Name"`
- `$ git config --global user.email yourname@gmail.com`

## Python Setup
In VS Code, navigate to the **Extensions** menu and install the **Python** extension. This will add Python language support to VS Code, as well as Pylance for syntax checking and Python Debugger for debugging.

It is also recommended to install the **autoDocstring** extension for writing docstrings (configure it to use the numpy format).

Open a Powershell or CMD terminal, and enter the following commands.
- `python -m venv .venv`
    - This creates a virtual environment to install project dependencies in. Use an up-to-date version of Python as the base for the virtual environment.
- `pip install -e .`
    - This installs the project and its dependencies.

# Development Practices
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
To document files, open a terminal and enter the following command.
- `python docs/build_docs.py`
    - This will automatically create html files under the `docs/build/html` folder based on the docstrings in indivudal modules. Open any one of the html files in VS Code's integrated browser to view documentation.

Sample format of a docstring for a function is listed below.
```python
def sample_function(a: float, b: float) -> float:
    # The r denotes a raw string, which is important for math, file strings, etc. to render correctly in the documentation.
    r"""

    This is a sample function that adds two numbers.

    .. math::

        a + b
    
    .. note::

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
    (0.001, 1, NoEror(approx(0.001, abs=1e-3))),
    ("a", 2, raises(TypeError))
])

def test_sample_function(a, b, expected_result):
    with expected_result as e:
        assert sample_function(a, b) == e
```

# Notes on File Structure
Top-level folder notes:

- `docs` houses all documentation-related files.
    - `docs/build_docs.py` contains a script that automatically generates the appropriate documentation structure and html files based on docstrings in modules.
    - `docs/build/html` holds the html files.
- `game` houses all game development and testing files.
    - `game/source` holds game-development files
- `reference` houses all reference and scope files.

Top-level file notes:
- `.gitignore` tells Source Control which filepaths should not be included in the overall source control management.
- `pyproject.toml` contains information about the project. Any modules used with the project should be documented under the `dependencies` section.
- `README.md` is the document you're currently reading.