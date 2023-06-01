import random
from os import system
from art import logo

def deal_card():
    """Randomly deals a card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(card_list):
    """Get's the list of cards and calculates the score"""
    sum_score = sum(card_list)
    if sum_score == 21 and len(card_list) == 2:
        return 0
    if 11 in card_list and sum_score > 21:
        card_list.remove(11)
        card_list.append(1)
    return sum_score

def compare(user_score, computer_score):
    """Compare the user score and the computer score"""
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Computer Wins with a BlackJack"
    elif user_score > 21:
        return "You Lose"
    elif user_score == 0 or computer_score > 21:
        return "You conquered"
    elif user_score > computer_score:
       return "You Win!"
    else:
        return "Computer Wins"

def play_game():
    print(logo)
    
    user_cards = []
    computer_cards = []
    end_game = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"    Your cards: {user_cards}, current score: {user_score}")
    print(f"    Computer first card: {computer_cards[0]}")

    while not end_game:
        if user_score == 0 or computer_score == 0 or user_score > 21:
            end_game = True
        else:
            draw_again = input("Type 'y' to get another card, type 'n' to pass: ")
            if draw_again == 'y':
                user_cards.append(deal_card())
                user_score = calculate_score(user_cards)
            else:
                end_game = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"    Your final hand: {user_cards}, final score: {user_score}")
    print(f"    Computer final hand: {computer_cards}, final score {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    system('cls')
    play_game()
print("Thank you for playing my game of BlackJack :)")