import random, os
from blackjack_art import logo

print(logo)

def clear_terminal():
    '''Clears the terminal window.'''
    if os.name == 'nt': #Windows
        os.system('cls')
    else:   #Linux OS
        os.system('clear')

def deal_card():
    '''Deals a random card.'''
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    return random.choice(cards)

def check_score(cards = []):
    '''Returns player's score according to the cards they hold'''

    # Blackjack situation, Cards = [10, 11] or [11, 10]
    # Mimics the condition that player has exactly 2 cards, [10 & 11]
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    # Dealing with situation where a player holds an Ace.
    if 11 in cards and sum(cards) > 21:
        #return sum(cards) - 10
        cards.remove(11)
        cards.append(1)
    
    #return 0 if cards list is empty, return sum if cards list is non-empty
    return sum(cards) if cards else 0

def bust(player):
    '''Returns True if Player's score is greater than 21'''
    return True if check_score(player) > 21 else False

def play_again():
    '''
    Accepts 'y' or 'n' as input.
    Asks user if they want to play again.
    '''
    replay = input("Play again? Type 'y' or 'n': ").upper()
    return True if replay[0] == 'Y' else False

def compare(user_score, computer_score):
    '''Compares User & Computer scores to find the winner.'''
    if user_score == computer_score:
        return "It's a draw!"
    elif user_score == 0:
        return 'Win with a Blackjack!'
    elif computer_score == 0:
        return 'You lose, Opponent has a Blackjack!'
    elif user_score > 21:
        return 'You went over. You lose!'
    elif computer_score > 21:
        return 'Computer went over. You win!'
    elif user_score > computer_score:
        return 'You win!'
    else: #computer_score > user_score
        return 'Computer wins. You lose!'

game_on = True if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")[0].upper() == 'Y' else False

while game_on:

    clear_terminal()

    print(logo)
    is_user_playing = True

    dealer = []
    user = []
    
    for _ in range(2):
        dealer.append(deal_card())
        user.append(deal_card())

    while is_user_playing:

        if check_score(user) == 0 or check_score(dealer) == 0 or bust(user):
            is_user_playing = False

        else:
            print(f'Your cards: {user}, Current score: {check_score(user)}')
            print(f"Computer's first card: {dealer[0]}")

            another_card = input("Type 'y' to get another card, 'n' to pass: ").upper()

            if another_card[0] == 'Y':
                user.append(deal_card())

            else:
                is_user_playing = False
    
    while check_score(dealer) != 0 and check_score(dealer) < 17 and not bust(user):
        dealer.append(deal_card())
    
        if bust(dealer):
            break
    
    print(f"Your final hand: {user}, final score: {check_score(user)}.")
    print(f"Computer's final hand: {dealer}, final score: {check_score(dealer)}.")
    print(compare(check_score(user), check_score(dealer)))

    if not play_again():
        game_on = False
    
    