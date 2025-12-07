import shutil
from pathlib import Path


def safe_move(src: Path, dest: Path):
    """Safely move a file or directory, overwriting only if necessary."""
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.exists():
        print(f"[!] Warning: Destination {dest} exists. Renaming original.")
        dest = dest.with_name(dest.stem + "_dup")
    shutil.move(str(src), str(dest))
