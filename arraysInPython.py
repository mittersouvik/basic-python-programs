#Demo of Array in Python

import array as arr

vals = arr.array('i', [10, 20, 30, 40])
print(vals)
print(vals.buffer_info())

'''
  Output of buffer_info()
    (55861888, 4) ----> (add, tot_name_elements)
'''


vals.reverse()
print(vals)
print("-------------------------------")
l = vals.tolist()
l.sort()
print("List: ", l)

for i in range(len(vals)):
    print(vals[i])
print()

newArr = arr.array(vals.typecode, (s*s for s in vals))

for i in newArr:
    print(i)

 
