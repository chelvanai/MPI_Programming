# import numpy as np
#
# a = np.array([[2,1],[4,3]])
# b = np.array([[1,3],[5,7]])
#
# print(np.dot(a,b))


# A = [[2, 1],
#      [4, 3]]
#
# B = [[1, 3],
#      [5, 7]]
#
# result = [[0, 0],
#           [0, 0, ]]
#
# # iterating by row of A
# for i in range(len(A)):
#
#     # iterating by coloum by B
#     for j in range(len(B[0])):
#
#         # iterating by rows of B
#         for k in range(len(B)):
#             result[i][j] += A[i][k] * B[k][j]
#
# for r in result:
#     print(r)


from mpi4py import MPI

comm = MPI.COMM_WORLD

rank = comm.Get_rank()
size = comm.Get_size()

A = [[2, 1],
     [4, 3]]

B = [[1, 3],
     [5, 7]]

