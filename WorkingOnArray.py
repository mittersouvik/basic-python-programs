# Accepting numbers for user using Array in Python

from array import *

arr = array('i', [])
size = eval(input("Enter the length of the array: "))

for i in range(size):
    x = eval(input("Enter the element: " ))
    arr.append(x)

print(arr)

val = eval(input("Enter the number to be searched: "))
try:
    index = arr.index(val)
    print(val, "found at index ", index)
except ValueError:
    print("Not found in the array")
    
    
