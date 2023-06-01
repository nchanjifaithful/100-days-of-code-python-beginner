import os
import art

restart = True
secret_auction = {}

while restart:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    secret_auction[name] = bid

    continue_auction = input("Are there any other bidders? Type 'yes' or 'no'. \n")
    if continue_auction == "no":
        restart = False
    os.system("cls")

max_bid = 0
for bidders in secret_auction:
    if max_bid <= secret_auction[bidders]:
        max_bid = secret_auction[bidders]

print(f"The winner is {secret_auction}")
print(max_bid)
print(secret_auction)
        