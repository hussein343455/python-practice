import  numpy as np

# Create a new array from which we will select elements
a = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])

# Create an array of indices
b = np.array([0, 2, 0, 1])
print(a[np.arange(4), b])  # equivalent toa [[0 ,1 ,2 ,3 ], [0, 2, 0, 1]]  Prints "[ 1  6  7 11]"
# Mutate one element from each row of a using the indices in b
a[np.arange(4), b] += 10# add 10 to only [ 1  6  7 11] in a
print(a)