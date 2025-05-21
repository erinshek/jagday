from setuptools import setup, find_packages
from jagday import __version__

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="jagday",
    version=__version__,
    author="Jules",
    description="A CLI tool to display running server processes.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/user/jagday",
    packages=find_packages(),
    install_requires=["psutil"],
    entry_points={
        "console_scripts": [
            "jps=jagday.cli:main_cli"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6', # Adding a python_requires for good practice
)
