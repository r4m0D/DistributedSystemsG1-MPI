from mpi4py import MPI
import socket

def f(x):
    return x**2

def trapezoidal_rule(a, b, n):
    h = (b - a) / n
    integral = (f(a) + f(b)) / 2.0
    for i in range(1, n):
        x = a + i * h
        integral += f(x)
    return integral * h

def read_input(filename, rank):
    with open(filename, 'r') as file:
        for i, line in enumerate(file):
            if i == rank:
                a, b, n = map(float, line.split())
                return a, b, int(n)
    return None  

if __name__ == "__main__":
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    processor_name = MPI.Get_processor_name()

    try:
        ip_address = socket.gethostbyname(processor_name)
    except socket.gaierror:
        ip_address = "IP not found"

    a, b, n = read_input("input.txt", int(ip_address.split('.')[-1])%4)

    local_n = n // size
    local_a = a + rank * local_n * (b - a) / n
    local_b = local_a + local_n * (b - a) / n

    if rank == size - 1:
        local_b = b

    print(f"Node {rank} is processing from {local_a} to {local_b} with {local_n} trapezoids.")

    local_integral = trapezoidal_rule(local_a, local_b, local_n)
    total_integral = comm.reduce(local_integral, op=MPI.SUM, root=0)

    if rank == 0:
        print("Total integral is:", total_integral)
