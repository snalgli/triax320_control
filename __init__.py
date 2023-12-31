#
# This file is a placeholder which makes Python
# recognize this folder as an importable package.
#
# tkb

"""
Experimental control utilities for the Wang lab.

When writing a script to control your experiment (or working
interactively using the interpreter), use :mod:`wanglib` to make
instrument control and data gathering easy.

Obtaining and Installing
++++++++++++++++++++++++

:mod:`wanglib` is hosted on Github_. Follow the instructions there on how
best to install the package and its dependencies.

.. _Github: https://github.com/baldwint/wanglib

"""

# This is a code library - not a set of miscellaneous experimental routines.  
# Functions included in :mod:`wanglib` should be generally useful somehow,
# rather than being specific to any given experimental setup.

from . import instruments as instruments
from .instruments.spex750m import triax320 as triax320