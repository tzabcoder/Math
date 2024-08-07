/*************************************************************************
 * Numerical Differentiation (Finite Differences)
 *
 * Numerical differentiation is a numerical method for computing the derivative
 * of a function computationally. This program uses the 'Finite Differences'
 * method for the derivative approximation.
 *
 * Further description for the Finite Differences method can be viewed here:
 *
 ************************************************************************/

#include <iostream>
#include <vector>
#include <cmath>
#include <tuple>

/*************************************************************************
 * function ()
 *
 * Represents the function f(x)
 * NOTE: This should be in the form of a polynomial. That is:
 *          x^n + x^n-1 + ... + x^2 + x + a
 *
 * @param[in] x variable of the function
 ************************************************************************/
double function (float x)
{
    // x^2 + 2x - 1
    return std::pow(x, 2) + 2 * x - 1;
}

/*************************************************************************
 * derivative ()
 *
 * This function calculates f'(x) using finite differences approximation.
 *
 * @param[in] x variable (point) to calculate the derivative
 * @param[in] h step size
 * @return f'(x)
 ************************************************************************/
double derivative (float x, float h)
{
    float x1 = x + h;
    double f  = function (x);
    double f1 = function (x1);

    // Calculates [f(x+h) - f(x)] / h
    return (f1 - f) / h;
}

/************************************************************************/
int main ()
{
    float x = 5.0f;
    float h = 0.001f;

    double f_prime  = derivative (x, h);

    std::cout << "Derivative (at x=" << x << "): " << f_prime << std::endl;  // Finite Differences

    return 0;
}
