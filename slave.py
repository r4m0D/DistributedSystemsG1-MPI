from mpi4py import MPI

def f(x):
    return x**2

def trapezoidal_rule(a, b, n):
    h = (b - a) / n
    integral = (f(a) + f(b)) / 2.0
    for i in range(1, n):
        x = a + i * h
        integral += f(x)
    return integral * h

def main():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()
    
    # Only rank 0 will handle the distribution and collection of results
    if rank == 0:
        # Assuming the number of intervals is provided or calculated
        a, b, n = 0.0, 1.0, 1000
        results = []
        for i in range(1, size):
            # Calculate local range for each slave
            local_n = n // (size - 1)
            local_a = a + (i - 1) * local_n * (b - a) / n
            local_b = local_a + local_n * (b - a) / n
            comm.send((local_a, local_b, local_n), dest=i, tag=77)
        for i in range(1, size):
            result = comm.recv(source=i, tag=77)
            results.append(result)
        total_integral = sum(results)
        print(f"The result of the integral of x^2 from {a} to {b} is {total_integral}")
    else:
        local_a, local_b, local_n = comm.recv(source=0, tag=77)
        local_integral = trapezoidal_rule(local_a, local_b, local_n)
        comm.send(local_integral, dest=0, tag=77)

if __name__ == "__main__":
    main()