#!/usr/bin/env python
#
# python-android
# Copyright (C) 2010 Chris Soyars
#
# This progream is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the license, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


__version__ = '1.0.2'

from setuptools import setup, find_packages

setup (
       name='python-android',
       version=__version__,
       author='Chris Soyars',
       author_email='python@ctso.me',
       description='A collection of Android tools written in Python.',
       url='http://github.com/ctso/python-android',
       license="GNU GPL",
       classifiers=[
            'Development Status :: 2 - Pre-Alpha',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: GNU General Public License (GPL)',
            'Topic :: Software Development :: Libraries',
        ],

       packages=find_packages('src'),
       package_dir={'':'src'},

       install_requires=[],

       entry_points={
            'console_scripts':[
                "bootinfo = android.command:main",
            ]
       },
)
