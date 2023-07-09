from mpi4py import MPI

comm  = MPI.COMM_WORLD
prank = comm.Get_rank()
size  = comm.Get_size()

# write your code

if MPI.Is_initialized():
   MPI.Finalize()
 
