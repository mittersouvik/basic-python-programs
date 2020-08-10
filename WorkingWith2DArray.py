import numpy as np

arr1 = np.array([
    [1,2,3,10,11,12],
    [4,5,6,13,14,15]
    ])
'''
print(arr1)
print(arr1.dtype)   #determines the type of array
print(arr1.ndim)    #determines the dimension of array
print(arr1.shape)   #determines the no of row and cols of array
print(arr1.size)    #determines the total number of elements in the matrix

arr2 = arr1.flatten()   #converts 2D array to 1D array
print(arr2)

arr3 = arr2.reshape(3,2,2)    #converts 1D array to N-D array
print(arr3)
'''

mat = np.matrix(arr1) # converts an array into matrix
print(mat)

m = np.matrix('1,2,10; 3,4,11; 5,6,12')
n = np.matrix('1,2,10; 3,4,11; 5,6,12')
multi = n * m
print("The matrix multiplication = ",multi)
print(m)
print(np.diagonal(m))
print("The min = ",m.min())
print("The max = ",m.max())
