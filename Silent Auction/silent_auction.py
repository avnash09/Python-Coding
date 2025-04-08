import os, time
#from art import logo

def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

print("Welcome to the Silent Auction Program.")

bids = {}

bidding_is_on = True
while bidding_is_on:

    name = input('What is your name? ')
    bid_value = ''
    
    while not bid_value.isdigit():
        bid_value = input("What's your bid? $")
        if bid_value.isdigit():
            break
        else:
            print('Please enter a correct bid value.')
            time.sleep(1) #wait for 1 second before clearing the screen
            clear_terminal()
            print(f"What is your name? {name}")


    bids[name.capitalize()] = int(bid_value)

    another_bidder = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if another_bidder[0].upper() != 'Y':
        break

    clear_terminal()

winning_value = 0
winner = ''
for name in bids:
    #print(f"{name} --> ${bids[name]}")

    if bids[name] > winning_value:
        winning_value = bids[name]
        winner = name

clear_terminal()
print(f"The winner is {winner} with a bid of ${winning_value}.")
