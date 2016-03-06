#!/usr/bin/env python3

"""Differential equations for Magnetic Cloak Particle Simulation.

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

# Third party modules.
import numpy as np

# ======================================================================
# Classical Lorentz force.
# ======================================================================

def Lorentz_c(t, y):
    """Lorentz force on a classical particle."""
    return np.append(
        y[3:6],
        qm * (E(t, y[0:3]) + np.cross(y[3:6], B(t, y[0:3]))))

# ======================================================================
# Relativistic Lorentz force.
# ======================================================================

#def Lorentz_r(t, y):
#    """Lorentz force on a relativistic particle."""
#    return

# ======================================================================
# Lorentz four-force.
# ======================================================================

#def Lorentz_4(t, y)
#    """Lorentz four-force on a particle."""
#    return

# ======================================================================
# Differential equation dictionary.
# ======================================================================

dictionary = {'LorC' : Lorentz_c,
#              'LorR' : Lorentz_r,
              }
