# Numerical Differentiation
numericalDifferentiation.cpp implements a *Finite Differences* approach to calculating derivatives programatically.

This method is a two point estimation, calculating the slope of the nearby secant line through (x, f(x)) and (x+h, f(x+h)).
h is known as the *step size* and represents a small change in x.

The slope of the secant line is: $(f(x+h)-f(x))/h$

### True Derivative
The true derivative is:
$$\lim_{h\to 0} \(f(x+h)-f(x))/h$$
