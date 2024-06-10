"""
* Optimization.py
*
* Description:
* This program implements optimization methods using python.
*
* Global Optimization:
* Global optimization attempts to find the global (absolute) maximia
* or minima of a function or set of functions.
*
* Local Optimization:
* Local optimization finds the optimal solution for a function in a given
* region of the search space, or the global optima if there is no specified
* local maxima or minima.
*
* Constrained Optimization:
* Constrained optimization is an optimization technique that resticts the
* interval on which to use to calculate the maxima/minima of the function.
"""

import numpy as np
import scipy.optimize as sco

def GlobalOptimizationFunction(p):
    x, y = p

    # Define function
    return np.sin(x) + 0.05 * x ** 2 + np.sin(y) + 0.05 * y ** 2

def LocalOptimizationFunction(p):
    x, y = p

    # Define function
    return np.sin(x) + 0.05 * x ** 2 + np.sin(y) + 0.05 * y ** 2

def ConstrainedOptimizationFunction(p):
    s, b, = p

    # Define function
    return -(0.5 * np.sqrt(s * 15 + b * 5) + 0.5 * np.sqrt(s * 5 + b * 12))

# Global optimization
fGlobRange = (-10, 10.1, 0.1) # (low, high, N) where N is the number of interpolation points

globalOpt = sco.brute(GlobalOptimizationFunction, (fGlobRange, fGlobRange), finish=None)
print(globalOpt)

optimizedFunc = GlobalOptimizationFunction(globalOpt)
print(optimizedFunc)

# Local optimization
localOpt = sco.fmin (LocalOptimizationFunction, globalOpt, xtol=0.001, ftol=0.001, maxiter=15, maxfun=20)
print(localOpt)

optimizedFunc = LocalOptimizationFunction(localOpt)
print(optimizedFunc)

# Constrained Optimization
constraints = ({'type' : 'ineq',
                'fun'  : lambda p: 100 - p[0] * 10 - p[1] * 10})

bounds = ((0, 1000), (0, 1000))
result = sco.minimize(ConstrainedOptimizationFunction, [5, 5], method='SLSQP', bounds=bounds, constraints=constraints)

print(result)