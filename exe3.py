import random

number=random.randint(1,25)

number_of_guesses = 0
while True:
    guess = int(input("pick a number"))
    if guess != number:
        if guess < number:
            print("increase your number")
        else :
            print("decrease your number")
    else:
        print("done")
        break