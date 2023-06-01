from art import logo
import random
from os import system

def win(userScoreValue, computerScoreValue):
    black_jack = 21

    if computerScoreValue == black_jack or userScoreValue > black_jack or computerScoreValue > userScoreValue:
        print("Computer Wins!")
    elif userScoreValue == black_jack or userScoreValue > computerScoreValue:
        print("You win!")
    elif userScoreValue == computerScoreValue:
        print("It's a draw!")
    else:
        print("idk what's going on here")


def blackJack():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    user = random.choices(cards, k = 2) #Random card choices for the user
    user_score = sum(user)

    computer = random.choices(cards, k = 2) #Random card choices for computer
    computer_score = sum(computer)

    black_Jack = 21

    start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if start == 'n':
        print("Thank you for opting to play!")
        return 
    elif start == 'y':
        system('cls')
        print(logo)
        print(f"Your cards: {user}")
        print(f"Computer's first card: {computer[0]}")

        pick = True
        while pick:
            game_choice = input("Type 'y' to get another card, type 'n' to pass: ")
            if game_choice == 'n':
                if 11 in user:
                    if user_score > 21:
                        user_score -= 10
                while computer_score <= 16 and computer_score <21:
                    new_card = random.choice(cards)
                    computer.append(new_card)
                    computer_score += new_card
                    print(f"Computer deck is now {computer} because it is less than 17")
                pick = False
            else:
                new_card = random.choice(cards)  # Draw a new deck of card
                user.append(new_card)
                print(f"You new deck {user}")
                user_score += new_card

            if user_score > 21:
                print("You have exceeded the 21 limit.")
                pick = False
            
        print(f"\nYour final hand: {user}")
        print(f"Computer final hand: {computer}")
        win(user_score, computer_score)
    blackJack()
        
        