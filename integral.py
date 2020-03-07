# Code to calculate a simple integral using the trapezoidal method using ony a single core
# Process takes about 20 seconds to complete

from decimal import *
from time import time

def f(x):
	return x*x


# a is upper limit of integration and b is lower limit of integration
# n is number of trapeziums in which the area under the curve is divided

def Trap_integrate(a, b, n):
	h = Decimal(b-a)/Decimal(n)
	print(h)
	integral = (f(a) + f(b))/2
	x = a

	for i in range(1, int(n)):
		x = x + h
		integral = integral + f(x)

	integral = integral * h
	return integral


start = time()
fintegral = Trap_integrate(0, 2, 100000)
end = time()

print("The integral is: " + str(fintegral))
print("Total time taken is: " + str(end-start))
