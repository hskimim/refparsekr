from setuptools import find_packages, setup
from setuptools.command.test import test


setup_requires = [
    ]

requirements = ['setuptools', 'numpy', 'pandas']


setup(
    name='refparsekr',
    version='0.1',
    description='references parsing in korean',
    author='hskimim',
    author_email='hskimim8855@gmail.com',
    include_package_data=True,
    install_requires=requirements,    
    setup_requires=setup_requires,
    classifiers=[],
    
)
