print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_______/
*******************************************************************************
''')

print("Welcome to Treasure Island. \nYou mission is to find the treasure.")
firstDirection = input("You're at cross road. Where do you want to go? Type 'left' or 'right' \n")
if firstDirection.lower() == "right":
	print("Oh! you ran into a gang of robbers. Your mission ends here.")
else:
	secondDirection = input("You\'ve come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across. ")
	if secondDirection == "swim":
		print('''How sad! You are breakfast for the piranhas 
          ,---,
  _    _,-'    `--,
 ( `-,'            `\
  \           ,    o \
  /   ,       ;       \
 (_,-' \       `, _  ""/
     pb `-,___ =='__,-'
              ````
''')
	else: 
		thirdDirection = input("You arrive at the Island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you go with?")
		if thirdDirection == "red":
			print('''You have choosen the room with Dragons and so is your fate!
			          ____ __
          { --.\  |          .)%%%)%%
           '-._\\ | (\___   %)%%(%%(%%%
               `\\|{/ ^ _)-%(%%%%)%%;%%%
           .'^^^^^^^  /`    %%)%%%%)%%%'
  jgs     //\   ) ,  /       '%%%%(%%'
    ,  _.'/  `\<-- \<
     `^^^`     ^^   ^^
''')
		elif thirdDirection == "blue":
			print('''You were swallowed by an ocean wave! 
           _.====.._
         ,:._       ~-_
             `\        ~-_
               | _  _  |  `.
             ,/ /_)/ | |    ~-_
    -..__..-''  \_ \_\ `_      ~~--..__...----... AN OCEAN WAVE ...''')
		elif thirdDirection == "yellow":		
			print("You are the chosen one! Congratulation, the treasure box is yours!")
		else:
			print("Please, chose the appropriate door.")
