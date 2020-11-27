import  numpy as np
#-to work with arrays of different shapes smaller array and a larger array
#-we want to use the smaller array multiple times to perform some operation on the larger array.

x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
v = np.array([1, 0, 1])

#y=add  v to each row of the matrix x,
#1
y = np.empty_like(x)    # empty matrix shape = as x
for i in range(4):  #the slow way
    y[i, :] = x[i, :] + v
#2
vv = np.tile(v, (4, 1))   # Stack 4 copies of v on top of each other
y = x + vv  # Add x and vv elementwise
#3 using broadcasting:
y = x + v