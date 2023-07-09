from mpi4py import MPI

comm  = MPI.COMM_WORLD
prank = comm.Get_rank()
size  = comm.Get_size()

# create a dummy dictionary for only rank=0

# broadcast the dictionary to all other ranks

# print broadcasted data received by all ranks

# NOTE:don't forget to flush stdout for immediate display

if MPI.Is_initialized():
   MPI.Finalize()
