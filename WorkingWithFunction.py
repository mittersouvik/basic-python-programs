'''
def greetings(name):
    return "Hi " + name

print(greetings("Souvik"))
print(greetings("Mini"))
print(greetings("Rammy"))
'''

'''
def sum_sub(a,b): # formal arguments
    sum1 = a + b
    sub1 = a - b
    return sum1,sub1

result1, result2 = sum_sub(10,20) # actual arguments
print(result1, result2)
'''

def sum(*b): #variable_length argument concept is used. *b is a tuple here
    c = 0
    for i in b:
        c = c + i
    print(c)

sum(10,20,30,40)

def sum(a,b): #position argument concept is used
    print(a+b)

sum(10,20)

def details(name, age): #keyword argument concept is used
    print(name)
    print(age-5)

details(age=20, name="Souvik")

def details(name, age=18): #default argument concept is used
    print(name)
    print(age)

details("Souvik")



