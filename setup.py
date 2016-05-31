#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


__version__ = "0.1"


class PyTest(TestCommand):

    user_options = [('cov-html=', None, 'Generate junit html report')]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.cov = None
        self.pytest_args = ['--cov', 'calculator', '--cov-report', 'term-missing']
        self.cov_html = False

    def finalize_options(self):
        TestCommand.finalize_options(self)
        if self.cov_html:
            self.pytest_args.extend(['--cov-report', 'html'])

    def run_tests(self):
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


setup(
    name='calculator example',
    packages=find_packages(),
    version=__version__,
    description='Python project to demonstrate Test Driven Development and Pair Programming',
    long_description=open('README.md').read(),
    author='Jonas Jurczok',
    author_email='jonas.jurczok@zalando.de',
    url='https://github.com/JonasJurczok/calculator_example',
    license='MIT License',
    # install_requires=['requests'],
    tests_require=['pytest-cov', 'pytest'],
    extras_require={
        'tests': ['flake8'],
    },
    cmdclass={'test': PyTest},
    test_suite='tests',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
    ],
)