import json
from pathlib import Path


def load_inventory(db_path: Path) -> dict:
    """Load JSON inventory safely."""
    if not db_path.exists():
        return {"projects": []}
    try:
        with open(db_path, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("[!] Corrupted inventory file. Reinitializing...")
        return {"projects": []}


def save_inventory(db_path: Path, data: dict):
    """Write JSON inventory safely."""
    db_path.parent.mkdir(parents=True, exist_ok=True)
    with open(db_path, "w") as f:
        json.dump(data, f, indent=4)
