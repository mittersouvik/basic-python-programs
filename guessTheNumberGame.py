#This is guess the number game

import random

print('Enter your name: ')
name = input()
#print('Please enter a string')
guessedNumber = random.randint(1,20)
print('Hi ' + name + ' start thinking of a number between 1 and 20')

#you will get 6 chances to guess the number

for guessTaken in range(1,7):
    print('Take a guess..')
    guess = int(input())
    if guess > guessedNumber:
        print('Your guess is too high')
    elif guess < guessedNumber:
        print('Your guess is too low')
    else:
        break #this condition is for correct guess

if guess == guessedNumber:
    print('Hi ' + name + ' you have guessed the number in ' + str(guessTaken) + ' guesses')
else:
    print('you have lost all your guesses. ' + 'The number is ' + str(guessedNumber))


    
