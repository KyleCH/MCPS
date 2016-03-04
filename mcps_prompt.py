#!/usr/bin/env python3

"""Prompt function for Magnetic Cloak Particle Simulation.

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
# Define prompt function.
# ======================================================================

def prompt(p, opt_dict):
    """Prompt user for input and list all available options.
    
    Parameters
    ----------
    p : str
        Prompt to be printed to terminal.
    opt_dict : dict
        Dictionary containing options.
    
    Returns
    -------
    key : str
        The key for the option selected by the user.
    """
    print(p)
    for k in sorted(opt_dict):
        print('    ' + str(k) + ' : ' + opt_dict[k].__doc__.split('\n', 1)[0])
    key = input('\n>>> ')
    print()
    return key
