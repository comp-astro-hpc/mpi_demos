from mpi4py import MPI

comm  = MPI.COMM_WORLD
prank = comm.Get_rank()
size  = comm.Get_size()

# write your code
if prank!=0:
   msg="Hello from %d"%(prank)
   comm.send(msg, dest=0)
else:
   for pid in range(1, size):
      msg = comm.recv(source=pid)
      print("PID =0 received %d"%pid, msg)


if MPI.Is_initialized():
   MPI.Finalize()
 
