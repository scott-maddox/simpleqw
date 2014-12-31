#!/bin/sh
#
#   Copyright (c) 2014, Scott J Maddox
#
#   This file is part of SimpleQW.
#
#   SimpleQW is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as
#   published by the Free Software Foundation, either version 3 of the
#   License, or (at your option) any later version.
#
#   SimpleQW is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Affero General Public License for more details.
#
#   You should have received a copy of the GNU Affero General Public
#   License along with SimpleQW.  If not, see
#   <http://www.gnu.org/licenses/>.
#
#######################################################################

# Clean out existing build and venv files
rm -rf build
rm -rf dist
rm -rf venv

# Activate a clean virtualenv
virtualenv venv --no-site-packages
source venv/bin/activate

# Install cython
pip install cython nose

# Test setup.py install
python setup.py install
python setup.py test
python -m unittest simpleqw.tests.test_finite_well_1d

# Deactivate the virtual python environment
deactivate
