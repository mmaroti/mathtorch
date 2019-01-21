#!/usr/bin/env python
#
# Copyright (C) 2019, Miklos Maroti
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from setuptools import setup

setup(
    name='mathtorch',
    version='0.1',
    packages=['mathtorch'],
    license='GPL 3',
    long_description=open('README.md').read(),
    # do not list standard packages
    install_requires=[
        'numpy',
        'pytorch',
    ],
    entry_points={
        'console_scripts': [
            'mathtorch = mathtorch.__main__:run'
        ]
    }
)
