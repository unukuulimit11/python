import random as r
number = r.randint(1, 100)
while True:

    try:
        guess = int(input("Guess the number between 1 and 100: "))
        if guess == number:
            print("Congratulations! You guessed the number 🥳")
            break
        elif guess > number:
            print("You guessed too high!")
        else:
            print("You guessed too low!")
    except ValueError:
        print("Please enter a number!!!")





