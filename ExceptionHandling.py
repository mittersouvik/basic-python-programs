def div42By(num):
    try:
        return 42/num
    except ZeroDivisionError:   #name of the error is optional
        print("Error: cannot be divided by zero")

print(div42By(2))
print(div42By(3))
print(div42By(0))
print(div42By(1))
