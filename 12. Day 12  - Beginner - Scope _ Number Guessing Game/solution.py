# Fetching a random number
import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#functions
def check_answer(guess, answer, turns):
    """Checks answer against guess and return the remaining turns"""
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")

def set_difficulty():
    """set's the difficulty based on input"""
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    """game function"""
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")

    value = random.randint(1, 100)
    user_guess = 0
    turns = set_difficulty()

    while user_guess != value:
        print(f"You have {turns} attempts remaining.")
        user_guess = int(input("Make a guess: "))
        check_answer(user_guess, value, turns)
        if turns == 0:
            print("You've run out of turns! You lose")
            return 
        elif user_guess != value:
            print("Try again!")

game()