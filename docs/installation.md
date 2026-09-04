# Installation

The source files for Test Game can be downloaded from the [Github repo](https://github.com/space-ducks/test-game).

You can clone the public repository with:

```bash
git clone https://github.com/space-ducks/test-game
```

Once you have a copy of the source, you can install it with:

```bash
cd test-game
uv sync
```

## Common Commands

| Command | Function |
| --- | ---|
| `uv sync` | Install/update dependencies into `.venv` |
| `uv add <package>` | Add a new dependency |
| `just docs-serve` | Preview docs locally at http://localhost:8000 |
| `just test` | Run tests |
| `just fix` | Auto-format and fix lint issues |