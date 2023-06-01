import random

EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")

def check_guess(random_number, user_guess):
        if user_guess > random_number:
            return "Too high.", False
        elif user_guess < random_number:
            return "Too Low.", False
        else:
            return f"You go it! The answer is {user_guess}", True

def guessing_game():
    random_number = random.randint(1, 101)
    print(random_number)
    end_game = False

    difficulty = input("Choose a difficulty: Type 'easy' or 'hard': ")
    if difficulty == 'easy':
        attempts = EASY_ATTEMPTS
    elif difficulty == 'hard':
        attempts = HARD_ATTEMPTS
    else: 
        print(ValueError)

    while end_game == False and attempts > 0:
        print(f"You have {attempts} remaining to guess the number.")
        user_guess = int(input("Make a guess: "))
        attempts -= 1
        message, end_game = check_guess(random_number, user_guess)
        print(message)
        if attempts == 0 and random_number != user_guess:
            print("You've run out of guesses, you lose.")

guessing_game()
