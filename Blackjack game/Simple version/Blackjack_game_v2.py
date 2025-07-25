import random, blackjack_art, os

# game_on = True

def clear_terminal():
    if os.name == "nt": #Windows
        os.system("cls")
    else:   #Mac/Linux
        os.system("clear")

def start_game():
    
    while True:
            start = input("Do you want to play a game of Blackjack? (y/n): ")
            if start and start[0].upper() == 'Y':
                return True
            elif start and start[0].upper() == 'N':
                return False
            else:
                print("Please provide a valid input!")


clear_terminal()
game_on = start_game()
#game_on = True

#Game setup
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def deal_card():
    return random.choice(cards)

#calculate score
def score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    
    return sum(cards)

while game_on:

    #players
    player_cards = []
    computer_cards = []

    #Deal cards to players
    for _ in range(2):
        player_cards.append(deal_card())
        computer_cards.append(deal_card())
    
    clear_terminal()
    print(blackjack_art.logo)
    print("Let's Play!")

    while True:

        #display initial hands
        print(f"Your cards: {player_cards}, score: {score(player_cards)}")
        print(f"Computer's first hand: {computer_cards[0]}")
        if score(player_cards) == 0:
            print("You win with a Blackjack!")
            break
        elif score(computer_cards) == 0:
            print("Dealer wins with a Black! You lose.")
            break

        user_input = input("\nDo you want to take another card? (y/n): ")
        if user_input[0].upper() == 'Y':
            player_cards.append(deal_card())
            clear_terminal()
            print(blackjack_art.logo)
            if score(player_cards) > 21:
                print(f"BUST! You went over, you lose.")
                break

        elif user_input[0].upper() == 'N':
            clear_terminal()
            print(blackjack_art.logo)
            
            #Dealers deals till his score is greater than 17
            while score(computer_cards) < 17:
                computer_cards.append(deal_card())

            if score(computer_cards) > 21:
                print("Dealer went over, You WIN!")
            elif score(computer_cards) == score(player_cards):
                print("Draw!")
            elif score(computer_cards) < score(player_cards):
                print("Congratulations! You WIN!")
            else:
                print("Dealer wins. Sorry, You lose!")
            break

        else:
            print("Invalid input! Try again.")

    print(f"Your cards: {player_cards}, Your Score: {score(player_cards)}")
    print(f"Computer's hand: {computer_cards}, Computer's Score: {score(computer_cards)}")
        
    game_on = True if input("\nDo you want to play again? (y/n): ")[0].upper() == 'Y' else False