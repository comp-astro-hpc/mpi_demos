# mpi_demos
Demonstration of basic MPI functions with `mpi4py`

### Scripts 
> - boiler_plate.py  &rarr; the template for MPI scripts; `MPI.Initialize` is automatically called when one imports `mpi4py`; `MPI.Finalize` is called by default in the python codes, but is added here just for demonstration
> - hello_world.py &rarr;  a simple send/receive operation in parallel
> - broadcast.py &rarr; communicating a dataset/dictionary that exists only on master (rank = 0) to all other processes; also try `MPI.Barrier`
> - integrate/trapezoidal.py &rarr; script for the trapezoidal calculation for a given function `func`, within `[a,b]` with `n` points 
> - integrate/mpi_integrate_send_recv.py &rarr; parallelly compute the trapezoidal integral and communicate by send/receive operation for final estimate
> - integrate/mpi_integrate_reduce.py &arr; improve the send/receive operation in `integrate/mpi_integrate_send_recv.py` file by using `MPI.Reduce`
> - domain_decomp/grid-hopping.py &arr; a simple demonstration of domain decomposition

## Creating a virtual environment
We recommend creating a virtual environment for the purpose of the demonstrations in this workshop. You can either create a conda virtual env or a native python one.
If you have conda installed, use [^conda_venv]:
```
conda create -n <venv_name> python=3.10
## Follow onscreen instructions to download necessary packages (if needed)
conda activate <venv_name> 
```
Use `conda deactivate` to move out of the virtual environment.

If you only have Python and not the conda environment (requires Python version >=3.6), then try [^python_venv]: 
```
python -m venv <venv_name>
source ./<venv_name>/bin/activate
```
Type `deactivate` to come out of the virtual environment.

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
- In the file `hello_world.py` add a simple send/receive operation, where all ranks send a message to rank 0
  Run using :
  ```
  mpirun -n <nproc> hello_world.py
  ```
- In the file `broadcast.py` create a dataset/dictionary that exists only on rank = 0 and broadcast that to all other
  ```
  mpirun -n <nproc> broadcast.py
  ```
- In the `integrate` folder, go through the script for the trapezoidal calculation in file `trapezoidal.py`, then move to file `mpi_integrate_send_recv.py` for parallel computation. Run using :
  ```
  mpirun -n 5 broadcast.py
  ```
- Update the file `mpi_integrate_reduce.py` to use `MPI.Reduce`.

- In the folder `domain_decomp`, the file `grid-hopping.py` demonstrates a simple domain decomposition. Run using :
  ```
  mpirun -n 2 grid-hopping.py
  ```
### Resources
- `mpi4py` documentation: https://mpi4py.readthedocs.io/en/stable/tutorial.html

- `MPI Basics` (for C): https://mpitutorial.com/tutorials/mpi-reduce-and-allreduce/

#### Footnotes
[^python_venv]: https://docs.python.org/3/library/venv.html
[^conda_venv]: https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html
[^mpi4py]: https://mpi4py.readthedocs.io/en/stable/

