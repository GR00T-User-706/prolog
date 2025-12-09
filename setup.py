from setuptools import setup, find_packages
from pathlib import Path

README = (Path(__file__).parent / "README.md").read_text()

setup(
    name="prolog",
    version="1.0.0",
    author="YourName",
    author_email="you@example.com",
    description="Prolog – A unified project catalog CLI/TUI/GUI for managing creative chaos.",
    long_description=README,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        "textual",
        "rich"
    ],
    entry_points={
        "console_scripts": [
            "prolog = prolog.main:main"
        ]
    },
    python_requires=">=3.9",
)
