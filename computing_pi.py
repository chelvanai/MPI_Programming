import time
from mpi4py import MPI

def Pi(num_steps):
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()
    Proc_num_steps=num_steps/size
    Start=rank*Proc_num_steps
    End=(rank+1)*Proc_num_steps
    print ("%d: [%d,%d]"%(rank,Start,End))
    step = 1.0/num_steps
    sum = 0
    for i in range(Start,End):
        x= (i+0.5)*step
        sum = sum + 4.0/(1.0+x*x)

    return sum


if __name__ == '__main__':
    num_steps=100000000
    start = time.time()
    localsum=Pi(num_steps)
    
    localpi = localsum/num_steps
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    pi = comm.reduce(localpi, op=MPI.SUM, root=0)
    end =time.time()
    if rank==0:
        print ("Pi with %d steps is %f in %f secs" %(num_steps, pi, end-start))
