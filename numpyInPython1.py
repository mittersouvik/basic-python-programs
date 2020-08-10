# copying an array

import numpy as np

arr1 = np.array([1,2,3,4,5])
#arr = arr + 5
#print(arr)

#arr2 = arr1
arr2 = arr1.view() #shallow copy---> if arr1 is changed, changes reflects in arr2 as well
arr2 = arr1.copy() #deep copy----> if arr1 is changed, changes does not reflect in arr2
arr1[1] = 6

print("arr1 = ", arr1)
print("arr2 = ", arr2)

print("Address of arr1=", id(arr1))
print("Address of arr2=", id(arr2))


      
