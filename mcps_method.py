#!/usr/bin/env python3

"""Methods of solving differential equations.

For Magnetic Cloak Particle Simulation.

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

# Custom modules.
import mcps_prompt as prompt

# ======================================================================
# Euler method.
# ======================================================================

def Eul_step(f, h, t, y):
    """Euler method.

    One step of Euler method for the numerical approximation of the
    solution to a differential equation.
    
    Parameters:
    -----------
    f : function
        Differential equation.
    h : float
        Step size.
    t : float
        Time or timelike parameter.
    y : np.array
    
    Returns
    -------
    tp : float
        Updated value of parameter t.
    yp : np.array
        Updated value of parameter y.
    """
    yp = y + h*f(t, y)
    tp = t + h
    return tp, yp

# ======================================================================
# Fourth order Runge-Kutta method.
# ======================================================================

def RK4_step(f, h, t, y):
    """Fourth order Runge-Kutta method.

    One step of fourth order Runge-Kutta method (RK4) for the numerical
    approximation of the solution to a differential equation.
    
    Parameters:
    -----------
    f : function
        Differential equation.
    h : float
        Step size.
    t : float
        Time or timelike parameter.
    y : np.array
    
    Returns
    -------
    tp : float
        Updated value of parameter t.
    yp : np.array
        Updated value of parameter y.
    """
    k1 = f(t,         y)
    k2 = f(t + 0.5*h, y + 0.5*h*k1)
    k3 = f(t + 0.5*h, y + 0.5*h*k2)
    k4 = f(t + h,     y + h*k)
    tp = t + h
    yp = y + h*(k1 + 2*(k2 + k3) + k4)/6
    return tp, yp

# ======================================================================
# Method dictionary.
# ======================================================================

dictionary = {'Eul' : Eul_step,
              'RK4' : RK4_step}
