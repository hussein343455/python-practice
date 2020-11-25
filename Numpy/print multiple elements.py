import  numpy as np

a = np.array([[1,2], [3, 4], [5, 6]])

bool_idx = (a > 2)
print(bool_idx)#array of false and true
print(a[bool_idx])#we can print out the values of these

# We can do all of the above in a single concise statement:3 in 1
print(a[a > 2])     # Prints "[3 4 5 6]"