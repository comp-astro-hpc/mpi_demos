from mpi4py import MPI
#from mpi4py.MPI import ANY_SOURCE
import numpy as np
from trapezoidal import trapz

comm  = MPI.COMM_WORLD
prank = comm.Get_rank()
size  = comm.Get_size()

# global limits
a = 0.
b = 1.
n = 1000000
# step size
h = (b-a)/n

## parallelize by dividing the range among the processes --------
# local_n is the number of trapezoids each process will calculate
local_n = int(n/size) # NOTE: size must be divisible by n

local_a = a + prank*local_n*h
local_b = local_a + local_n*h

# initializing variables
integral    = np.zeros(1)
recv_buffer = np.zeros(1)

func = lambda x: 4/(1+x*x)

# local computation
integral[0] = trapz(func, local_a, local_b, local_n)

## replace this communication with MPI.Reduce operation
'''
if prank == 0:
    # root node receives local integrals from all other processes 
    # -> evaluates the overall sum
    total = integral[0]
    for i in range(1, size):
        comm.Recv(recv_buffer, i)
        total += recv_buffer[0]
else:
    # all other process send their result 
    comm.Send(integral, dest=0)
'''

# root process prints results
if prank == 0:
        print("With n = %d trapezoids, the estimate of integral from "\
        "%.2f to %.2f is = %.6f" %(n, a, b, total))
