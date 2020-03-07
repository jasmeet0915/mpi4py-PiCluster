from mpi4py import MPI
from decimal import *
from time import time

def f(s):
	return s*s

a = 0
b = 2
n = 100000
dest = 0
total = -1
h = Decimal(b-a)/Decimal(n)

def Trap_integrate(p, q, ntraps):
	integral = (f(p) + f(q))/2
	x = p

	for i in range(1, int(ntraps)):
		x = x + h
		integral = integral + f(x)

	return integral*h


comm = MPI.COMM_WORLD
my_rank = comm.Get_rank()
size = comm.Get_size()


local_n = n/size
local_a = a + my_rank*local_n*h
local_b = local_a + local_n*h

fintegral = Trap_integrate(local_a, local_b, local_n)

if my_rank == 0:
	total = fintegral
	for process in range(1, size):
		integral = comm.recv(source=process)
		total = total + integral
	print("Integral is: " + str(total))

else:
	comm.send(fintegral, dest=dest)



