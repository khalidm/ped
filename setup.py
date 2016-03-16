# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='ped',
    version='0.0.1',
    description='Ped package',
    long_description=readme,
    author='Khalid Mahmood',
    author_email='khalid.mahmood@unimelb.edu.au',
    url='https://github.com/khalidm/ped',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

