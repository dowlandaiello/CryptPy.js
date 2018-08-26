from setuptools import setup, find_packages
from os import path
from io import open

here = path.abspath(path.dirname(__file__))

# Fetch long description from README
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

