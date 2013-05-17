#!/usr/bin/env python

from setuptools import setup, find_packages, Command
import os
import sys


class TestCommand(Command):
    description = "run self-tests"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        ret = os.system('python test.py')
        if ret != 0:
            sys.exit(-1)

setup(
    name='pcss',
    version='0.0.1',
    author='Senko Rasic',
    author_email='senko.rasic@goodcode.io',
    description='Python CSS preprocessor',
    license='MIT',
    url='https://github.com/senko/pcss.git',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    packages=find_packages(),
    install_requires=[],
    cmdclass={
        'test': TestCommand
    }
)
