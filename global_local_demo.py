def spam():
    global a #this will make the variable a as global variable all through the code
    a = 10
    print("The value of a in spam function is ", a)

a = 20
spam()
print("a = ", a)

