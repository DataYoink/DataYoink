"""A setuptools-based setup module adapted from the Python Packaging Authority"s
sample project.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

import setuptools
import sys
import os 
from os.path import abspath, dirname
from setuptools import setup, find_packages
PACKAGES = find_packages()

src_dir = dirname(abspath(__file__))
requires_path = abspath(pjoin(src_dir, "requirements.txt"))
with open(requires_path) as f:
    REQUIRES = [line.strip('\n') for line in f.readlines()]

# Get the long description from the README file
with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="DataYoink",
    version="1.0.0",
    author="Christina Doy, Doris Hung, Kevin Lee, Kevin Martinez",
    author_email="gskl92@uw.edu",
    description="A plot digitizer for battery discharge plots and dQdV plots from scientific literature",
    long_description=long_description,
    long_description_content_type="text/markdown",
    download_url="https://github.com/DataYoink/DataYoink",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        REQUIRES
    ],
)
