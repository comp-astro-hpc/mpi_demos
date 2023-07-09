from mpi4py import MPI
import numpy as np

comm=MPI.COMM_WORLD
prank = comm.Get_rank()
size = comm.Get_size()

nghost = 1
nint_glob = 6

nint_loc = 3
ntot_loc = nint_loc + 2*nghost
domain_local = np.zeros(ntot_loc, dtype=np.int32)

if (prank==0):
    domain_glob = np.arange(nint_glob, dtype=np.int32)
    # domain_glob[0] = 1
    # domain_glob[4] = 1
    domain_local[nghost:nghost+nint_loc] = domain_glob[:(nint_glob//2)]
    print("The initial field is ", domain_glob, flush=True)
    for pid in range(1,size):
        comm.Send(domain_glob[pid*(nint_glob//2):(pid+1)*(nint_glob//2)],
                  dest=pid)
else:
    data = np.zeros(nint_loc, dtype=np.int32)

    comm.Recv(data, source=0)
    domain_local[nghost:nghost+nint_loc] = data[:]

#print(f"rank {prank}: {domain_local[:nghost]}{domain_local[nghost:-nghost]}{domain_local[-nghost:]}", flush=True)
if prank==0: dummy = input()
comm.Barrier()
while(True):
    comm.Send(domain_local[nghost:2*nghost], dest=not(prank), tag=0)
    comm.Send(domain_local[nint_loc+nghost-1:nint_loc+nghost], dest=not(prank), tag=1)
    comm.Recv(domain_local[-nghost:], source=not(prank), tag=0)
    comm.Recv(domain_local[:nghost], source=not(prank), tag=1)
    
    print(f"rank {prank}: {domain_local[:nghost]}{domain_local[nghost:-nghost]}{domain_local[-nghost:]}", flush=True)
    for i in range(domain_local.shape[0]-2*nghost, 0, -1):
        domain_local[i] = domain_local[i-1]
    
    comm.Barrier()   
    if (prank!=0):
        comm.Send(domain_local[nghost:nint_loc+nghost], dest=0, tag=prank)
    else:
        for pid in range(size):
            if (pid!=0):
                comm.Recv(domain_glob[pid*(nint_glob//2):(pid+1)*(nint_glob//2)], source=not(prank), tag=not(prank))
            else:
                domain_glob[pid*(nint_glob//2):(pid+1)*(nint_glob//2)] = domain_local[nghost:nint_loc+nghost]
    if (prank==0): 
         print(f"Entire field: {domain_glob}", flush=True)
         dummy = input()
    comm.Barrier()
    if (prank==0):
        if (dummy.strip()=='q'): comm.Abort()

if MPI.Is_initialized():
   #MPI.COMM_WORLD.Barrier()
   MPI.Finalize()
 
