import  numpy as np

x = np.array([[1,2],[3,4]], dtype=np.int64)
y = np.array([[5,6],[7,8]], dtype=np.int64)
print(x + y) #we can do a{-,/,*}
print(np.sqrt(x))# or a square root
print(x.dot(y))# Inner product of vectors;

print(np.sum(x))  # Compute sum of all elements; prints "10"
print(np.sum(x, axis=0))  # Compute sum of each column; prints "[4 6]"
print(np.sum(x, axis=1))  # Compute sum of each row; prints "[3 7]"
print(x.T)  # Prints "[[1 3] [2 4]]"  transposing