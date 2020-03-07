# Code for sending messages from one process to another which is a fundamental requirement in parallel computing

from mpi4py import MPI

comm = MPI.COMM_WORLD
my_rank = comm.Get_rank()
cluster_size = comm.Get_size()
node = MPI.Get_processor_name()

if my_rank != 0:
	message = "___HI, message from process " + str(my_rank) + " on node " + node
	comm.send(message, dest=0)
else:
	for processor in range(1, cluster_size):
		rmessage = comm.recv(source=processor)
		print("message received by process 0 on " + node + " from process " + str(processor) + " is " + rmessage)
