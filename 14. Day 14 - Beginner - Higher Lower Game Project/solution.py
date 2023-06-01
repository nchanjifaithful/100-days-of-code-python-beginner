import random
import os
from art import logo, vs
from game_data import data

def format_data(account):
    """Format the account into printable format"""
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_desc}, from {account_country}"

def check_answer(guess, a_followers, b_followers):
    """Check if user if correct"""
    if a_followers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b'

# print logo
print(logo)
score = 0

# Generate random account from the game data
account_a = random.choice(data)
account_b = random.choice(data)
if account_a == account_b:
    account_b = random.choice(data)

print(f"Compare A: {format_data(account_a)}")
print(vs)
print(f"Against B: {format_data(account_b)}")

guess = input("Who has more followers? Type 'A' or 'B': ").lower()

a_follower_count = account_a["follower_count"]
b_follower_count = account_b["follower_count"]

is_correct = check_answer(guess, a_follower_count, b_follower_count)

if is_correct:
    score += 1
    print(f"You're correct! Current score: {score}")
else:
    print(f"Sorry, that's wrong. Final score {score}")
