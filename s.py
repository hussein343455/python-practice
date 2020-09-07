# animals = ['cat', 'dog', 'monkey']
# for idx, animal in enumerate(animals):
#
#     print('#%d: %s' % (idx + 1, animal))
# # Prints "#1: cat", "#2: dog", "#3: monkey", each on its own line

#---------------------------------------------------------------------------

# nums = [0, 1, 4, 3, 4]
# squares = []
# i=0;
# for x in nums:
#     squares.append(x++2)#append:apply the function in the() to all x's
# print(squares)
#---------------------------------------------------------------------------

# nums = [0, 1, 2, 3, 4]
# squares = [x+2 for x in nums]#same as before
# print(squares)
#---------------------------------------------------------------------------

# nums = [0, 1, 2, 3, 4]
# even_squares = [x ** 2 for x in nums if x % 2 == 0] #same with an if
# print(even_squares)
#---------------------------------------------------------------------------
                            #Dictionaries/hashs

# d = {'cat': 'cute', 'dog': 'furry'}  # Create a new dictionary with some data
# print(d['cat'])       # Get an entry from a dictionary; prints "cute"
# print('cat' in d)     # Check if a dictionary has a given key; prints "True"
# d['fish'] = 'wet'     # Set an entry in a dictionary
# print(d['fish'])      # Prints "wet"
# print(d.get('monkey', 'N/A'))  # Get an element with a default; prints "N/A"
# print(d.get('fish', 'N/A'))    # Get an element with a default; prints "wet"
# del d['fish']         # Remove an element from a dictionary
# print(d.get('fish', 'N/A')) # "fish" is no longer a key; prints "N/A"

#---------------------------------------------------------------------------
# d = {'person': 2, 'cat': 4, 'spider': 8}
# for animal in d:
#     legs = d[animal]
#     print('A %s has %d legs' % (animal, legs))
#---------------------------------------------------------------------------

# d = {'person': 2, 'cat': 4, 'spider': 8}
# for animal, legs in d.items():   #same as before
#     print('A %s has %d legs' % (animal, legs))

#---------------------------------------------------------------------------

# nums = [0, 1, 2, 3, 4]
# even = {x: x ** 2 for x in nums if x % 2 == 0}
# print(even)

#---------------------------------------------------------------------------
                            #functions
# def sign(x):
#     if x > 0:
#         return 'positive'
#     elif x < 0:
#         return 'negative'
#     else:
#         return 'zero'
#
# for x in [-1, 0, 1]:
#     print(sign(x))
# # Prints "negative", "zero", "positive"
#---------------------------------------------------------------------------
                                # class
# class Greeter(object):
#
#     # Constructor
#     def __init__(self, name):
#         self.name = name  # Create an instance variable
#
#     # Instance method
#     def greet(self, loud=False):
#         if loud:
#             print('HELLO, %s!' % self.name.upper())
#         else:
#             print('Hello, %s' % self.name)
#
# g = Greeter('Fred')  # Construct an instance of the Greeter class
# g.greet()            # Call an instance method; prints "Hello, Fred"
# g.greet(loud=True)   # Call an instance method; prints "HELLO, FRED!"
#---------------------------------------------------------------------------
                                #numpy
import numpy as np
# a = np.array([1, 2, 3])   # Create a rank 1 array
# print(type(a))            # Prints "<class 'numpy.ndarray'>"
# print(a.shape)            # Prints "(3,)"
# print(a[0], a[1], a[2])   # Prints "1 2 3"
# a[0] = 5                  # Change an element of the array
# print(a)                  # Prints "[5, 2, 3]"
#
# b = np.array([[1,2,3],[4,5,6]])    # Create a rank 2 array
# print(b.shape)                     # Prints "(2, 3)"
# print(b[0, 0], b[0, 1], b[1, 0])   # Prints "1 2 4"
#---------------------------------------------------------------------------
# a = np.zeros((3,3))   # Create an array of all zeros
# a = np.ones((2,1))    # Create an array of all ones
# a = np.full((3,3), 7)  # Create a constant array
# a = np.eye(3)         # Create a 2x2 identity matrix
# a = np.random.random((2,2))  # Create an array filled with random values

#---------------------------------------------------------------------------
# Create the following rank 2 array with shape (3, 4)
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]
# a = np.array([[1,2,3,4],
#               [5,6,7,8],
#               [9,10,11,12]])
# Use slicing to pull out the subarray consisting of the first 2 rows
# and columns 1 and 2; b is the following array of shape (2, 2):
# [[2 3]
#  [6 7]]
# b = a[:2, 1:3]
# [[6 7]
#  [10 11 ]]
# b = a[1:3, 1:3]
# A slice of an array is a view into the same data, so modifying it
# will modify the original array.
# b[0, 0] = 77     # b[0, 0] is the same piece of data as a[0, 1]
# print(a[0, 1])   # Prints "77"
#---------------------------------------------------------------------------
# a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
# Two ways of accessing the data in the middle row of the array.
# Mixing integer indexing with slices yields an array of lower rank,
## while using only slices yields an array of the same rank as the
# original array:
# row_r1 = a[1, :]    # Rank 1 view of the second row of a
# row_r2 = a[1:2, :]  # Rank 2 view of the second row of a
# print(row_r1, row_r1.shape)  # Prints "[5 6 7 8] (4,)"
# print(row_r2, row_r2.shape)  # Prints "[[5 6 7 8]] (1, 4)"

# We can make the same distinction when accessing columns of an array:
# col_r1 = a[:, 1]
# col_r2 = a[:, 1:2]
# print(col_r1, col_r1.shape)
# print(col_r2, col_r2.shape)
#---------------------------------------------------------------------------
# a = np.array([[16,42],
#               [3, 4],
#               [5, 6]])
# # The returned array will have shape (3,) and
# print(a[[0, 1, 2], [0, 1, 0]])  # Prints "[1 4 5]" indexes are [[0,0] [1,1] [2,0]]
#
# print(a[[0, 0], [1, 1]])  # Prints "[2 2]"
# print(np.array([a[0, 1], a[0, 1]]))  # Prints "[2 2]" Equivalent to the previous integer array indexing example
#---------------------------------------------------------------------------
# Create a new array from which we will select elements
# a = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
#
# # Create an array of indices
# b = np.array([0, 2, 0, 1])
# print(a[np.arange(4), b])  # equivalent toa [[0 ,1 ,2 ,3 ], [0, 2, 0, 1]]  Prints "[ 1  6  7 11]"
# # Mutate one element from each row of a using the indices in b
# a[np.arange(4), b] += 10# add 10 to only [ 1  6  7 11] in a

#---------------------------------------------------------------------------
# a = np.array([[1,2], [3, 4], [5, 6]])
#
# bool_idx = (a > 2)
# print(bool_idx)#array of false and true
# print(a[bool_idx])#we can print out the values of these
#
# # We can do all of the above in a single concise statement:3 in 1
# print(a[a > 2])     # Prints "[3 4 5 6]"
#---------------------------------------------------------------------------
# x = np.array([1.0, 2.0])   # Let numpy choose the datatype
# print(x.dtype)             # Prints dtype="float64"
# x = np.array([1, 2], dtype=np.int64)   # Force a particular datatype
#---------------------------------------------------------------------------

# x = np.array([[1,2],[3,4]], dtype=np.int64)
# y = np.array([[5,6],[7,8]], dtype=np.int64)
# print(x + y) #we can do a{-,/,*}
# print(np.sqrt(x))# or a square root
# print(x.dot(y))# Inner product of vectors;
#---------------------------------------------------------------------------
# x = np.array([[1,2],[3,4]])
# print(np.sum(x))  # Compute sum of all elements; prints "10"
# print(np.sum(x, axis=0))  # Compute sum of each column; prints "[4 6]"
# print(np.sum(x, axis=1))  # Compute sum of each row; prints "[3 7]"
# print(x.T)  # Prints "[[1 3] [2 4]]"  transposing
#---------------------------------------------------------------------------
                #Broadcasting in numpy
#-to work with arrays of different shapes smaller array and a larger array
#-we want to use the smaller array multiple times to perform some operation on the larger array.

# x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
# v = np.array([1, 0, 1])
#
# #y=add  v to each row of the matrix x,
# #1
# y = np.empty_like(x)    # empty matrix shape = as x
# for i in range(4):  #the slow way
#     y[i, :] = x[i, :] + v
# #2
# vv = np.tile(v, (4, 1))   # Stack 4 copies of v on top of each other
# y = x + vv  # Add x and vv elementwise
# #3 using broadcasting:
# y = x + v
#---------------------------------------------------------------------------
                    # Matplotlib
# #read abd show an img
# from matplotlib import pyplot as plt
# import cv2 as cv
# img = cv.imread('ss.jpg')
# print(img.dtype, img.shape)
# img_tinted = img *[1, 0.95, 0.9]
# plt.imshow(np.uint8(img_tinted))
# plt.show()
#---------------------------------------------------------------------------
# x = np.arange(0, 3 * np.pi, 0.1)
# y = np.sin(x)
#
# # Plot the points using matplotlib
# plt.plot(x, y)
# plt.show()

#---------------------------------------------------------------------------

# import matplotlib.pyplot as plt
# # Compute the x and y coordinates for points on sine and cosine curves
# x = np.arange(0, 3 * np.pi, 0.1)
# y_sin = np.sin(x)
# y_cos = np.cos(x)
# # Set up a subplot grid that has height 2 and width 1,
# # and set the first such subplot as active.
# plt.subplot(2, 1, 1)
# # Make the first plot
# plt.plot(x, y_sin)
# plt.title('Sine')
# # Set the second subplot as active, and make the second plot.
# plt.subplot(2, 1, 2)
# plt.plot(x, y_cos)
# plt.title('Cosine')
# # Show the figure.
# plt.show()

#---------------------------------------------------------------------------
