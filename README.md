# mpi_demos
Demonstration of basic MPI functions with `mpi4py`

## Scripts 
> - boiler_plate.py  &rarr; template for MPI scripts; `MPI.Initialize` is automatically called when one imports `mpi4py`; `MPI.Finalize` is called by default in the python codes, but is added here just for demonstration
> - hello_world.py &rarr;  a simple send - receive operation parallely
> - broadcast.py &rarr; communicating a dataset/dictionary that exists only on master (rank = 0) to all others processes; also try `MPI.Barrier`
> - integrate/trapezoidal.py &rarr; script for the trapezoidal calculation for a given function `func`, within `[a,b]` with `n` points 
> - integrate/mpi_integrate_send_recv.py &rarr; parallely compute the trapezoidal integral and communicate by send/receive operation for final estimate
> - integrate/mpi_integrate_reduce.py &arr; improve the send/receive operation in `integrate/mpi_integrate_send_recv.py` file by using `MPI.Reduce`

## Creating a virtual environment
We recommend creating a virtual environment for the purpose of the demonstrations in this workshop. You can either create a conda virtual env or a native python one.
If you have conda installed, use [^conda_venv]:
```
conda create -n <venv_name> python=3.10
## follow onscreen intructions to download necessary packages (if needed)
conda activate <venv_name> 
```
Use `conda deactivate` to move out of the virtual environment.

If you only have python and not the conda environment (requires python version >=3.6), then try [^python_venv]: 
```
python -m venv <venv_name>
source ./<venv_name>/bin/activate
```
Type `deactivate` to come out of the virtual environment

## Installing `mpi4py` inside the virtual environment [^mpi4py]
Use either:
```
pip install --upgrade pip
pip install mpi4py
```
or,
```
conda install -c conda-forge mpi4py
```

## Instructions

- In `hello_world.py` Add a simple send - receive operation, where all ranks send a message to rank 0
- In `broadcast.py`, create a dataset/dictionary that exists only on rank = 0 and broadcast that to all other

- In `integrate` folder, go through the script for the trapezoidal calculation in file `trapezoidal.py`, then move to file `mpi_integrate_send_recv.py` for parallel computation
- Update the file `mpi_integrate_reduce.py` to use `MPI.Reduce`


[^python_venv]: https://docs.python.org/3/library/venv.html
[^conda_venv]: https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html
[^mpi4py]: https://mpi4py.readthedocs.io/en/stable/
