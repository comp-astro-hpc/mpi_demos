from mpi4py import MPI

comm  = MPI.COMM_WORLD
prank = comm.Get_rank()
size  = comm.Get_size()

# create a dummy dictionary for only rank=0
if prank==0:
   data = {'nums': [1, 2.5, 3.5],
          'alph': ('a', 'ad', 'bcv')
         }
else:
   data = None
print("Before bcast rank %d : "%prank, data, flush=True)
# broadcast the dictionary to all other ranks
data = comm.bcast(data, root=0)
print("After Bcast %d:  "%prank, data, flush=True)
# print broadcasted data received by all ranks

# NOTE:don't forget to flush stdout for immediate display
if MPI.Is_initialized():
   MPI.Finalize()
