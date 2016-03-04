#!/usr/bin/env python3

"""Calculates the path of a particle in a magnetic field.

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
import mcps_UI as UI
import mcps_prompt as prompt

# ======================================================================
# Define main function.
# ======================================================================

def main():
    # Print script name, file name, and version.
    print('\n' + '='*80 + '\n'*2
        + 'Magnetic Cloak Particle Simulation'.center(80, ' ') + '\n'
        + __file__.center(80, ' ') + ('v ' + __version__).center(80, ' ')
        + '\n'*2 + '='*80 + '\n')
    # Prompt user for desired UI.
    key_UI = int(prompt.prompt('Select user interface:', UI.dictionary))
    UI.dictionary[key_UI]()
    return 0

# ======================================================================
# Run main function.
# ======================================================================

main()
