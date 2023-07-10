from mpi4py import MPI

comm  = MPI.COMM_WORLD
prank = comm.Get_rank()
size  = comm.Get_size()

data = None
if prank == 0:
    data = {'a': 7, 'b': 3.14}
    comm.send(data, dest=1, tag=11)
elif prank == 1:
    data = comm.recv(source=0, tag=11)
print("Rank %d has"%prank, data)

if MPI.Is_initialized():
   MPI.Finalize()
 
