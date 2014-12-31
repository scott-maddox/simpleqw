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

# std lib imports
from setuptools import setup
from glob import glob
import os

# third party imports
from Cython.Build import cythonize

# read in __version__
exec(open('src/simpleqw/version.py').read())

# Change to the src directory, so that `setup.py build_ext --inplace`
# works properly.
os.chdir('src')

cython_modules = []
cython_modules += glob(os.path.join('*.pyx'))
cython_modules += glob(os.path.join('*', '*.pyx'))
cython_modules += glob(os.path.join('*', '*', '*.pyx'))
print 'Cython modules:', cython_modules

setup(
    name='SimpleQW',
    version=__version__,  # read from version.py
    description='simple quantum well computations',
    long_description=open('../README.rst').read(),
    url='http://scott-maddox.github.io/simpleqw',
    author='Scott J. Maddox',
    author_email='smaddox@utexas.edu',
    license='AGPLv3',
    packages=['simpleqw',
              'simpleqw.tests',
              'simpleqw.examples',],
    package_dir={'simpleqw': 'simpleqw'},
    test_suite='simpleqw.tests',
    zip_safe=True,
    use_2to3=True,
    ext_modules=cythonize(cython_modules),
)

print 'Done.'