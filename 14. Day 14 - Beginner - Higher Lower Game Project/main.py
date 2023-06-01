import os
import random
import art
from game_data import data

randomList = []

def get_character_index():
    """Generates the random ig accounts from the game data file"""
    random_index = random.randrange(len(data))
    if random_index in randomList:
        get_character_index()
    else:
        randomList.append(random_index)
        return random_index
    

def scrape(account_index):
    """formats the data from the list for display"""
    data_dictionary = data[account_index]
    return f"{data_dictionary['name']}, a {data_dictionary['description']}, from {data_dictionary['country']}."

def get_count(character_index):
    """Fetches the number of followers for every given account index"""
    followers = data[character_index]['follower_count']
    return followers

def compare_counts(followers1, followers2):
    """Compares the followers and returns the higher one"""
    if followers1 > followers2:
        return 'A'
    else:
        return 'B'
    
def display(character_one, character_two, score):
    """Combines the game display and returns the user choice of the winner"""
    print(art.logo)
    if score > 0:
        print(f"You're right! Current score: {score}")
    character_one_intro = scrape(character_one)
    print(f"Compare A: {character_one_intro}")
    print(art.vs)
    character_two_intro = scrape(character_two)
    print(f"Compare B: {character_two_intro}")
    choice = input("Who has more followers? Type 'A' or 'B': ")
    return choice


score = 0
# Fetch the first character from the list
character_one = get_character_index()
continue_game = True

while continue_game:
    os.system('cls')
    character_two = get_character_index()
    followers_one = get_count(character_one)
    followers_two = get_count(character_two)
    print(f"{followers_one} vs {followers_two}")

    choice = display(character_one, character_two, score)
    higher = compare_counts(followers_one, followers_two)

    if higher == choice:
        score += 1
        character_one = character_two
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        continue_game = False
    
