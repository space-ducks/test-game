# Usage

To use Test Game in a project:

```python
import test_game
```

## Common Commands

Powershell commands:

| Command | Function |
| --- | ---|
| `uv sync` | Install/update dependencies into `.venv` |
| `uv add <package>` | Add a new dependency |
| `just docs-serve` | Preview docs locally at http://localhost:8000 |
| `just test` | Run unit tests |
| `just check-and-fix` | Auto-format and fix lint issues |

Git Bash commands:

|Command|Function|
|---|---|
|`git checkout <branch>`|Selects a branch to use|
|`git pull`|Pulls updates from GitHub repository to local device|
|`git merge <source> <dest>`|Merge one branch into another|