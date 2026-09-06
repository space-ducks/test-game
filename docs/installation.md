# Installation

The source files for Test Game can be downloaded from the [GitHub repo](https://github.com/space-ducks/test-game).

The repository can be cloned with VS Code. To do so, open VS Code and navigate to the Source Control menu on the left sidebar. Select **Clone Repository**. If the button does not appear, click on the reload link to reload the window. Sign in with your GitHub credentials (make an account if needed) and make a local clone of the `test-game` repository.

## Git Setup
Open a Git Bash terminal and use the following commands to set up your identity. This is required to make commits through VS Code.
```bash
$ gh auth login
$ git config --global user.name "Your Name"
$ git config --global user.email yourname@gmail.com
```

## VS Code Extensions
In VS Code, navigate to the **Extensions** menu and install the **Python** extension.

|Extension|Purpose|
|---|---|
|Python|Adds Python language support (also installs Pylance and Python Debugger)|
|Even Better TOML|Adds TOML language support|
|vscode-just|Adds just language support|
|autoDocstring|Helps write docstrings (use numpy format)|

## Project Setup
Open a Powershell or CMD terminal, and enter `uv sync`. This will create a virtual environment (`.venv`) to install project dependencies in, as well as install the project and all its dependencies.

```bash
cd test-game
uv sync
```