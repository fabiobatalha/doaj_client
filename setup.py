#!/usr/bin/env python
import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.rst')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

install_requires = [
    'requests>=2.7.0',
    ]

test_requires = []

setup(
    name="doaj_client",
    version='0.1',
    description="A client library for DOAJ API",
    author="Fabio Batalha",
    author_email="fabiobatalha@gmail.com",
    license="BSD 2-clause",
    keywords='doaj api',
    packages=['doaj'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Operating System :: POSIX :: Linux",
        "Topic :: Library",
        "Topic :: API",
    ],
    dependency_links=[
    ],
    include_package_data=True,
    zip_safe=False,
    setup_requires=["nose>=1.0", "coverage"],
    tests_require=test_requires,
    install_requires=install_requires,
    test_suite="nose.collector",
)