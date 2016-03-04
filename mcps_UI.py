#!/usr/bin/env python3

"""User interfaces for Magnetic Cloak Particle Simulation.

This code was written for Python 3 and tested using Python 3.5.0
(64-bit) with Anaconda 2.4.0 (64-bit) on a computer running Ubuntu 14.04
LTS (64-bit).
"""

__author__ = 'Kyle Capobianco-Hogan'
__copyright = 'Copyright 2016'
__credits__ = ['Kyle Capobianco-Hogan']
#__license__
__version__ = '0.0.0'
__maintainer__ = 'Kyle Capobianco-Hogan'
__email__ = 'kylech.git@gmail.com'
__status__ = 'Development'

# ======================================================================
# Import modules.
# ======================================================================

# Standard library modules.

# Third party modules.
#import numpy as np
#import scipy.constants as const

# Custom modules.
#from coordinate_converter import *
import mcps_prompt as prompt
import mcps_method as method

# ======================================================================
# Interminal user interface.
# ======================================================================

def terminal():
    """Terminal based user interface."""
    method_key = prompt.prompt(
        "Select method of solving differential equations:",
        method.dictionary)
    step = method.dictionary[method_key]
    return 0

# ======================================================================
# Batch file processing user interface.
# ======================================================================

def batch():
    """Batch file based user interface."""
    print('The function "batch()" has not been implemented yet.')
    return -1

# ======================================================================
# Graphical user interface.
# ======================================================================

def GUI():
    """Graphical user interface."""
    print('The function "GUI()" has not been implemented yet.')
    return -1

# ======================================================================
# User interface dictionary.
# ======================================================================

dictionary = {0 : terminal,
              1 : batch,
              2 : GUI}
