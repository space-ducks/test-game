# docs/build_docs.py
import subprocess
from pathlib import Path

DOCS_DIR = Path(__file__).resolve().parent   # .../test-game/docs, no matter where you run this from
REPO_ROOT = DOCS_DIR.parent                   # .../test-game

def main():
    subprocess.run(
        [
            "sphinx-apidoc",
            "-o", str(DOCS_DIR / "source" / "api"),
            str(REPO_ROOT / "game"),
            "-f",
            str(REPO_ROOT / "game" / "tests"),
        ],
        check=True,
    )
    subprocess.run(
        ["sphinx-build", "-M", "html", str(DOCS_DIR / "source"), str(DOCS_DIR / "build")],
        check=True,
    )

if __name__ == "__main__":
    main()