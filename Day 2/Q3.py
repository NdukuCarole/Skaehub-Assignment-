import random

#range of numbers
num = random.rint(1, 5)
guess = None

# number that program picks
while guess != num:
    guess = input("guess a number between 1 and 5: ")
    guess = int(guess)

#user input to play
    if guess == num:
        print("congratulations! you won!")
        break
    else:
        print("nope, sorry. try again!")