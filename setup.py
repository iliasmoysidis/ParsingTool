from setuptools import find_packages, setup

setup(
    name='parser',
    packages=find_packages(include=['parser']),
    version='0.1.0',
    description='Parser for Datacellar to extract values and timestamps given a field name',
    author='Me'
)