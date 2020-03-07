from decimal import *
from time import time

def f(x):
	return x*x



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
