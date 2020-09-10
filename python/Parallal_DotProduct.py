from mpi4py import MPI

comm = MPI.COMM_WORLD

rank = comm.Get_rank()
size = comm.Get_size()

n = 5
v1 = [1, 2, 3, 4, 5]
v2 = [6, 4, 3, 2, 1]
sum = 0

# master task
if rank == 0:
    sum += v1[rank] * v2[rank]
    for i in range(1, size):
        sum += comm.recv(source=i)
    print(sum)

# workers task
else:
    comm.send(v1[rank] * v2[rank], dest=0)


