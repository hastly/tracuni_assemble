#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

requirements = [
]

setup_requirements = [
]

test_requirements = [
]

setup(
    author="Konstantin Gonciarou",
    author_email="konstantin.goncharov@inplat.ru",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: System :: Logging",
        "Natural Language :: Russian",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Operating System :: POSIX :: Linux",
    ],
    description="Convenient library to plug in tracer to incoming and "
                "outgoing points and extract data from there",
    entry_points={
    },
    install_requires=requirements,
    setup_requires=setup_requirements,
    tests_require=test_requirements,
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='jaeger zipkin tracer',
    name='tracuni',
    packages=find_packages(),
    python_requires='>=3.5.3',
    test_suite='tests',
    url='https://github.com/hastly/tracuni_assemble',
    version='0.3.9',
    zip_safe=False,
)
