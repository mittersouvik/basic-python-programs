# numpy practice: multiple ways of creating an array

import numpy as np
arr = np.array([10,20,30,40])
print(arr)
print(arr.dtype) #tells the data type of array created by numpy
print("---------------------------------------------------")

arr1 = np.linspace(0,15,16) #interval = 16
print(arr1)
print("---------------------------------------------------")

arr2 = np.arange(1,11,2) # step diff = 2
print(arr2)
print("---------------------------------------------------")

arr3 = np.logspace(1,40,5) #interval = 5
print(arr3)
print('%.2f' %arr3[2])
print("---------------------------------------------------")

arr4 = np.zeros(5, int)
print(arr4)
print("---------------------------------------------------")

arr4 = np.ones(5,int)
print(arr4)

