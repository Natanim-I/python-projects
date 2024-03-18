# A number guessing game

import random
from art_logo import logo

HIDDEN_NUMBER = random.randint(1, 100)
number_of_attempts = 0

print(logo)
print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100.")
choice = input(f"Choose a difficulty, Type 'easy' or 'hard': ").lower()

if choice == 'easy':
    number_of_attempts = 10
elif choice == 'hard':
    number_of_attempts = 5


def update_attempts():
    """A function to update the number of attempts."""
    return number_of_attempts - 1


def guess_the_number(guess):
    """A function to compare the hidden number and the guessed number."""
    if HIDDEN_NUMBER < guess:
        return "Too High"
    elif HIDDEN_NUMBER > guess:
        return "Too Low"
    else:
        return 1


while number_of_attempts > 0:
    print(f"You have {number_of_attempts} attempts to guess the number.")
    my_guess = int(input("Make a guess: "))
    result = guess_the_number(my_guess)
    if result == 1:
        print(f"You got it. The answer was {HIDDEN_NUMBER}")
        print("You Won!!!")
        number_of_attempts = 0
    else:
        print(result)
        print("Guess again: ")
        number_of_attempts = update_attempts()

if number_of_attempts == 0:
    print("You have run out of attempts, You Lose!")