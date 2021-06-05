from distutils.core import setup

from setuptools import find_packages

setup(
    name='super-duper-carnival',
    version='0.1.0',
    author="Aditya Misra",
    packages=find_packages(),
    long_description=open('README.md').read(),
    python_requires=">=3.7",
)