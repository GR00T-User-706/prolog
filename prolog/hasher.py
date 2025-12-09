import hashlib
from pathlib import Path

def hash_file(path: Path) -> str:
    hasher = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hasher.update(chunk)
    return hasher.hexdigest()

def hash_path(path: Path) -> str:
    if path.is_file():
        return hash_file(path)
    else:
        hasher = hashlib.sha256()
        for sub in sorted(path.rglob("*")):
            if sub.is_file():
                hasher.update(hash_file(sub).encode())
        return hasher.hexdigest()
