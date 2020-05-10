#!/usr/bin/env python3
from setuptools import setup

setup(
    name='esp201 micropyton firmware uploader',
    version='0.0.1',
    author='maekos',
    author_email='maekos@gmail.com',
    description='.',
    url='https://github/maekos/micropython',
    scripts=['bin/esp201'],
    package_dir={'':'.'},
    packages=['.'],
)
