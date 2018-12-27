from setuptools import setup, find_packages

setup_requires = [
    ]

install_requires = [
    "pdfminer.six==20181108"
    "pandas==0.23.4"
    "numpy==1.15.1"

    ]

dependency_links = [
    ]

setup(
    name='refparsekr',
    version='0.1',
    description='refernecs parsing in Korean',
    author='hskimim',
    author_email='hskimim8855@gmail.com',
    packages=["CA"],
    include_package_data=True,
    install_requires=install_requires,
    setup_requires=setup_requires,
    dependency_links=dependency_links,
    # scripts=['manage.py'],
    entry_points={
        'console_scripts': [
            ],
        "egg_info.writers": [
                "foo_bar.txt = setuptools.command.egg_info:write_arg",
            ],
        },
    )
