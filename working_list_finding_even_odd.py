def count(lst):
    even = odd = 0
    for i in lst:
        if i % 2 == 0:
            even = even + 1
        else:
            odd = odd + 1
    return even, odd

try:
    lst = []
    while True:
        lst.append(int(input()))
except:
    even, odd = count(lst)
    print("even: {} and odd: {}".format(even,odd))



    
    

