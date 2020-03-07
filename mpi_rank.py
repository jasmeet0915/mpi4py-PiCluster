from mpi4py import MPI

comm = MPI.COMM_WORLD
my_rank = comm.Get_rank()
cluster_size = comm.Get_size()
processor_name = MPI.Get_processor_name()

print("hello my rank is: " + str(my_rank))
print("size of the cluster is:" + str(cluster_size))
print("this process is running on: "  + str(processor_name))
