# setup.py
from setuptools import setup, find_packages
import pathlib

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text(encoding="utf-8")

setup(
    name="my-tail",
    version="0.1.1",
    description="A small implementation of Unix tail (supports -n and -f) implemented with Click",
    long_description=README,
    long_description_content_type="text/markdown",
    author="Олесь Прокопів",
    packages=find_packages(exclude=("tests",)),
    include_package_data=True,
    install_requires=[
        "click>=8.0"
    ],
    entry_points={
        "console_scripts": [
            "my-tail = my_tail.cli:cli",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
