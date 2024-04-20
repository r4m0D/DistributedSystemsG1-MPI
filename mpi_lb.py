from mpi4py import MPI

def f(x):
    """ Function to integrate, x^2 in this case. """
    return x**2

def trapezoidal_rule(a, b, n):
    """ Calculate the integral of a function f from a to b with n intervals using the trapezoidal rule. """
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

    a, b, n = 0.0, 1.0, 1000  # Total intervals and range for integration

    if rank == 0:
        # Master node
        results = []
        total_workers = size - 1
        part_sizes = [n // total_workers + (1 if i < n % total_workers else 0) for i in range(total_workers)]
        current_a = a
        for i in range(1, size):
            local_n = part_sizes[i - 1]
            local_a = current_a
            local_b = current_a + local_n * (b - a) / n
            comm.send((local_a, local_b, local_n), dest=i, tag=77)
            print(f"Master sending to slave {i}: Start={local_a}, End={local_b}, Intervals={local_n}")
            current_a = local_b
        for i in range(1, size):
            result = comm.recv(source=i, tag=77)
            results.append(result)
            print(f"Master received from slave {i}: Result={result}")
        total_integral = sum(results)
        print(f"The final result of the integral of x^2 from {a} to {b} is {total_integral}")
    else:
        # Slave nodes
        local_a, local_b, local_n = comm.recv(source=0, tag=77)
        print(f"Slave {rank} received: Start={local_a}, End={local_b}, Intervals={local_n}")
        local_integral = trapezoidal_rule(local_a, local_b, local_n)
        comm.send(local_integral, dest=0, tag=77)
        print(f"Slave {rank} sent back result: {local_integral}")

if __name__ == "__main__":
    main()