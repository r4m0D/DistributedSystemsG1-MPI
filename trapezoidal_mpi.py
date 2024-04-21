from mpi4py import MPI
import numpy as np

def f(x):
    # Function to integrate: f(x) = x^2
    return x ** 2

def trapezoidal_rule(a, b, n, rank, size):
    # Calculate the local integral using the trapezoidal rule
    h = (b - a) / n
    local_n = n // size
    local_a = a + rank * local_n * h
    local_b = local_a + local_n * h

    print(f"Rank {rank}: Calculating from {local_a} to {local_b}")

    local_integral = (f(local_a) + f(local_b)) / 2.0
    for i in range(1, local_n):
        x = local_a + i * h
        local_integral += f(x)
    local_integral *= h
    return local_integral

def main():
    # Initialize MPI
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank() # Rank of the current process
    size = comm.Get_size() # Total number of processes

	# Define the integral limits and the number of trapezoids
    a = 0.0
    b = 1.0
    n = 10000  # Number of trapezoids

    local_integral = trapezoidal_rule(a, b, n, rank, size)
    total_integral = comm.reduce(local_integral, op=MPI.SUM, root=0)

	# Print the result
    if rank == 0:
        print(f"The integral of x^2 from {a} to {b} is approximately {total_integral}")

if __name__ == "__main__":
    main()