import time
from numba import jit


@jit
def loop(num_steps):
    step = 1.0 / num_steps
    sum = 0
    for i in range(num_steps):
        x = (i + 0.5) * step
        sum = sum + 4.0 / (1.0 + x * x)
    return sum


def pi_with_jit(num_steps):
    start = time.time()

    sum = loop(num_steps)
    pi = sum / num_steps
    end = time.time()

    print("Pi with %d steps is %f in %f secs" % (num_steps, pi, end - start))


def pi_find(num_steps):
    start = time.time()
    step = 1.0 / num_steps
    sum = 0
    for i in range(num_steps):
        x = (i + 0.5) * step
        sum = sum + 4.0 / (1.0 + x * x)

    pi = sum / num_steps
    end = time.time()

    print("Pi with %d steps is %f in %f secs" % (num_steps, pi, end - start))


pi_with_jit(100000000)
