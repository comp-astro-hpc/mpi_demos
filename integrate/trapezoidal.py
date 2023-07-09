import numpy as np

def trapz(func, a, b, n):
    integral = (func(a) + func(b))/2.0
    # n+1 endpoints, but n trapazoids
    for x in np.linspace(a,b,n+1):
        integral += func(x)
    integral = integral * (b-a)/n

    return integral

