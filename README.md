# mpi_demos
Demonstration of basic MPI functions with `mpi4py`

## Scripts 
> - boiler_plate.py  &rarr; basic structure of the scripts; MPI.Initialize is automatically called when one imports `mpi4py`;MPI.Finalize is automatically called in the python codes, but added here for demonstration
> - hello_world.py &rarr; we will try a simple send - receive operation parallely over here
> - broadcast.py &rarr; a data that exists only on master rank = 0 is to be broadcasted to all others; also try Barrier
> - integrate/trapezoidal.py &rarr; script for simple trapezoidal calculation
> - integrate/mpi_integrate.py &rarr; parallely compute the trapezoidal integral and communication for final estimate

