docker exec mpi-master mpiexec -hosts mpi-node-1,mpi-node-2,mpi-node-3,mpi-node-4 -N 10 python /app/trapezoidal_mpi.py