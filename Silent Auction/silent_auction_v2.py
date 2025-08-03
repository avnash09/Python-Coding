import os
from art import logo

def clear_terminal():

    if os.name == "nt": #Widnows
        os.system("cls")
    else: #Mac/Linux
        os.system("clear")

clear_terminal()
print(logo)

print("Welcome to Silent auction")

bids = {}

next_bidder = True
while next_bidder:

    
    while True:
        name = input("Enter your name: ")
        if name.isalpha():
            break
        else:
            print("Please enter a valid name (letters only).")

    while True:
        try:
            bid = int(input("What is your bid? $ "))
            break
        except ValueError:
            print("Please enter a valid number for age.")

    bids[name.capitalize()] = bid

    is_next_bidder = input("Any other bidder? (y/n): ")
    if is_next_bidder[0].lower() == 'n':
        break
    else:
        clear_terminal()
        print(logo)

max_bid = 0
for name, bid in bids.items():
    print(name, bid)
    if bid > max_bid:
        highest_bidder = name
        max_bid = bid
    elif bid == max_bid:
        highest_bidder = highest_bidder + ", " + name

clear_terminal()
print(logo)
print(f"Congratulations {highest_bidder}! You won the auction with a bid of ${max_bid}!\n")