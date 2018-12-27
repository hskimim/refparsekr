# -*- coding: utf-8 -*-

import sys

from setuptools import find_packages, setup
from setuptools.command.test import test

setup_requires = [
    ]

install_requires = [
    'pandas==0.23.4',
    'numpy==1.15.1',
    'pdfminer.six==20181108'
    ]

dependency_links = [
    ]


setup(
    name='parsing_the_references',
    version='0.1',
    license='GNU GENERAL PUBLIC LICENSE',
    author='hskimim',
    author_email='hskimim8855@gmail.com',
    url='https://github.com/hskimim/refparsekr',
    description='Parse the references line by line',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    classifiers=[],
)
