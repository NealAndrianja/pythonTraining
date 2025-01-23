import math

def squre_root(number):
    return math.sqrt(number)


nbre = float(input("Enter a number: "))
print(squre_root(nbre))

from random import randint

from random import randint


def guessedNumber():
    lucky = randint(1, 10)
    tries = 5

    while True:
        x = int(input("Enter your guess: "))
        if x == lucky:
            print("Congratulations! You guessed it.")
            break
        else:
            tries -= 1
            print(f"Your guess is wrong, {tries} {'try' if tries == 1 else 'tries'} left.")

        if tries == 0:
            print(f"Sorry, you lost! The lucky number was {lucky}.")
            break


guessedNumber()