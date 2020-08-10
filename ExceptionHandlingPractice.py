print('How many cats do you have?')
numCats = input()

try:
    if int(numCats) < 0:
        print("Input should  be a positive number")
    elif int(numCats) >= 0 and int(numCats) <= 4:
        print("That is not that many cats")
    else:
        print("That is too much cats")
except:
    print("Input is not a number")

