"""
* Integration.py
*
* Description:
* This program shows different intregration techniques using python.
* First, the program uses numerical integration techniques from scipy.
* Given a bounded range on the interval [a, b], the program computed the
* integral for the function f(x).
*
* The program then calculates the integral through a simulation technique.
* This method draws I random values of x between the integral limits and evaluates
* the integration function at every random value for x. Then, the fumction values
* are summed and the average is calculated to arrive at an average function value
* over the integration interval. This value is multiplied by the length of the
* integration interval to derive an estimate for the integration value.
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as sci

# Define function f(x)
def f(x):
    return np.sin(x) + 0.5 * x

# Graph the function
x = np.linspace(0, 10)
y = f(x)
plt.plot(x, y, c='b', linewidth=2)
plt.show()

# Numerical Integration Techniques ---------------------------------
a = 0.5 # Starting value for linspace sequence
b = 9.5 # End value for linspace sequence

# Fixed-order Gaussian quadrature
fixedQuad = sci.fixed_quad(f, a, b)[0]
print(f'Fixed-Order Gaussian Quadrature: {fixedQuad}')

# Derived from the Fortran QUADPACK to compute a definite integral
quad = sci.quad(f, a, b)[0]
print(f'QUADPACK: {quad}')

# Romberg Integration
romberg = sci.romberg(f, a, b)
print(f'Romberg: {romberg}')

# Create a sequence of evenly spacedd numbers
# start = 0.5
# end = 9.5
# number of samples = 25
xi = np.linspace(0.5, 9.5, 25)

# Composize trapeziodal rule
trapz = sci.trapz(f(xi), xi)
print(f'Composite Trapeziodal Rule: {trapz}')

# Composite Simpson's rule
simps = sci.simps(f(xi), xi)
print(f'Composite Simpsons Rule: {simps}')

# Integration by Simulation ----------------------------------------
a = 0.5
b = 9.5

print('\nIntegration by Simulation')
for i in range(1, 20):
    np.random.seed(1000)

    # Create a set of random values (increased at every itteration)
    x = np.random.random(i * 10) * (b - a) + a

    # Estimate the integral by calculating the average function value
    # Then multiply by the integration interval range
    estimate = np.mean(f(x)) * (b - a)

    print(estimate)