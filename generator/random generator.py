import numpy as np
# all values do not need to be stored in memory
def my_random_generator():
    for _ in range(10):
        x=np.random.randn()
        yield x

