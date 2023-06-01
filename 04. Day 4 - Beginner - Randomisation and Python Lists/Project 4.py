import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice_art = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 Scissors: "))

#checking for valididty of the input
if user_choice >= 3 or user_choice < 0:
    print("Invalid entry here. You lose!")
else:
    print(f"{choice_art[user_choice]}")
    computer_choice = random.randint(0, 2)
    print(f"Compute chose:\n{choice_art[computer_choice]}")

    #checking for the winning entry
    if user_choice == computer_choice: 
        print("It's a tie! No Win, No Loss")
    elif user_choice == 1 and computer_choice == 0:
        print("You're a champion!")
    elif user_choice == 0 and computer_choice == 2:
        print("You're a champion!")
    elif user_choice == 2 and computer_choice == 1:
        print("You're a champion!")
    else:
        print("Oh, you lose")
