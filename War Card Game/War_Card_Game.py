from class_player import Player
from class_deck import Deck
import random

#Game setup

player1 = Player('One')
player2 = Player('Two')
game_deck = Deck()
game_deck.shuffle()

print(f"Player 1 : {player1.name}\nPlayer 2 : {player2.name}")
print(game_deck)

for x in range(26):
        player1.add_cards(game_deck.deal_one())
        player2.add_cards(game_deck.deal_one())

print(player1 , player2)
#print(player1.all_cards[0], player2.all_cards[0])

game_on = True
round_num = 0

while game_on:

    round_num += 1
    print(f'Round {round_num}')
        
    if len(player1.all_cards) == 0:
          print(f"Player {player1.name} has 0 cards, GAME OVER!")
          print(f"Player {player2.name} WINS!")
          game_on = False
          break
    
    if len(player2.all_cards) == 0:
          print(f"Player {player2.name} has 0 cards, GAME OVER!")
          print(f"Player {player1.name} WINS!")
          game_on = False
          break
    
    player_one_cards = []
    player_one_cards.append(player1.remove_one())
    
    player_two_cards = []
    player_two_cards.append(player2.remove_one())

    at_war = True

    while at_war:
          
        if player_one_cards[-1].value > player_two_cards[-1].value:
            print(f"Player {player1.name}: {player_one_cards[-1]}, Player {player2.name}: {player_two_cards[-1]}")
            print(f"Player {player1.name} gets all the cards.\n")
            player1.add_cards(player_one_cards)
            player1.add_cards(player_two_cards)
            at_war = False

        elif player_one_cards[-1].value < player_two_cards[-1].value:
            print(f"Player {player1.name}: {player_one_cards[-1]}, Player {player2.name}: {player_two_cards[-1]}")
            print(f"Player {player2.name} gets all the cards.\n")
            player2.add_cards(player_one_cards)
            player2.add_cards(player_two_cards)
            at_war = False

        else:
            
            print(f"Player {player1.name}: {player_one_cards[-1]}, Player {player2.name}: {player_two_cards[-1]}")
            print('WAR!')

            if len(player1.all_cards) < 10:
                print("Player One unable to play war! Game Over at War")
                print("Player Two Wins! Player One Loses!")
                game_on = False
                break
            
            elif len(player2.all_cards) < 10:
                print("Player Two unable to play war! Game Over at War")
                print("Player One Wins! Player Two Loses!")
                game_on = False
                break

            else:
                 
                 for i in range(10):
                      player_one_cards.append(player1.remove_one())
                      player_two_cards.append(player2.remove_one())
