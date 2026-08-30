# Setup
Follow these instructions to set up the project. Assumes VS Code as the IDE.

## Software Installations
If not already installed, the following software.

- Python: https://www.python.org/downloads/.
- Git: https://git-scm.com/install/windows.
- VS Code: https://code.visualstudio.com/download.

## VS Code Setup
Once installed, open VS Code. Navigate to the Source Control menu on the left sidebar and select `Clone Repository`. Sign in with your GitHub credentials (make an account as needed) and make a local clone of the `test-game` repository.

Open a Git Bash terminal and use the following commands to set up your identity. This is required to make commits through VS Code.
- `$ git config --global user.name "John Doe"`
- `$ git config --global user.email johndoe@example.com`

## Python Setup
In VS Code, navigate to the Extensions menu and install the Python extension. This will add Python language support to VS Code. It is also recommended to install the autoDocstring extension for writing docstrings (use numpy format).

Open a Powershell or CMD terminal, and enter the following commands.
- `python -m venv .venv`: This creates a virtual environment to install project dependencies in. Use an up-to-date version of Python as the base for the virtual environment.
- `pip install -e .`: This installs the `test-game` project and its dependencies.

# Development
Development work should be done on separate branches from the `main` branch. Each developer should have their own development branch, with sub-branches dedicated to developing indivdual features.

- `randy-dev`
- `noah-dev`

When merging, merge and delete sub-branches, but merge and preserve developer branches. **All** files should be documented and tested before being moved to the main branch.

## Documentation
To document files, use the command `python docs/build_docs.py` in a terminal. This will automatically create html files under `docs/build` based on the docstrings in indivudal modules. Open any one of the html files in VS Code's integrated browser to view documentation.

## Testing
The `pytest` module will be used for unit tests. Test files should include "test" somewhere in their name for pytest to recognize them. `@pytest.mark.parameterize()` can be used to parameterize test inputs, reducing clutter.