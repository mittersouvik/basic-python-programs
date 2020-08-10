''' Decorators is technique of adding extra features to the existing function.
    without changing the content of the file where that function is defined
'''

def div(a,b):
    return a/b


''' We are writing the below code to demonstrate the use of
    decorators in python
'''
def smart_div(func):

    def inner(a,b):
        if a<b:
            a, b = b, a
        return func(a,b)
    return inner

div1 = smart_div(div)
print(div1(2,4))

