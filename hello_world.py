from mpi4py import MPI
import numpy as np

comm  = MPI.COMM_WORLD
prank = comm.Get_rank()
size  = comm.Get_size()

# write your code
data = None
if prank == 0:
    data = np.array([0., 1.2, 3.5])
    print("Rank %d has"%prank, data, flush=True)
    # process zero sends this to all 
    for pid in range(1, size):
       comm.send(data, dest=pid)
else:
    data = comm.recv(source=0)
    print("Rank %d has"%prank, data, flush=True)

if MPI.Is_initialized():
   MPI.Finalize()
 
