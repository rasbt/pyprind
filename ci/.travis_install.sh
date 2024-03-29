#!/bin/bash
# This script is meant to be called by the "install" step defined in
# .travis.yml. See http://docs.travis-ci.com/ for more details.
# The behavior of the script is controlled by environment variabled defined
# in the .travis.yml in the top level folder of the project.

# License: 3-clause BSD

set -e

# Fix the compilers to workaround avoid having the Python 3.4 build
# lookup for g++44 unexpectedly.
export CC=gcc
export CXX=g++

# Deactivate the travis-provided virtual environment and setup a
# conda-based environment instead
deactivate

# Use the miniconda installer for faster download / install of conda
# itself
wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh

bash miniconda.sh -b -p $HOME/miniconda
export PATH="$HOME/miniconda/bin:$PATH"
hash -r
conda config --set always_yes yes --set changeps1 no
conda update -q conda
conda update -q pip
conda info -a

conda create -n testenv --yes python=$PYTHON_VERSION pip nose psutil

conda init bash
source activate testenv

if [[ "$COVERAGE" == "true" ]]; then
    pip install coverage coveralls
fi
