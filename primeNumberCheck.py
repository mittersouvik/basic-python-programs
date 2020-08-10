# check given number is prime or not

num = eval(input("Enter a number: "))

'''
flag = 0
for i in range(2, num):
    if num % i == 0:
        flag = 1
        break

if flag == 1:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")
'''

#Below implementing the concept of for-else
for i in range(2, num//2):
    if num % i == 0:
        print(num, "is not a prime number")
        break
else:
    print(num, "is a prime number")
    
        
