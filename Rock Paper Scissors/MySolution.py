from RockPaperScissors import rock, paper, scissors
import random

game_dict = {'1':rock, '2':paper, '3':scissors}

def choose():
    while True:
        
        choice = input('Choose:\n\[1] Rock\n\[2] Paper\n\t[3] Scissor\n----> ')
        if choice not in ['1','2','3']:
            print('Invalid choice! Please try again.')
        else:
            return choice
            break

def rps(choice):
    return game_dict[choice]

def display(player_choice, computer_choice):
    print(f'Player Choice: {player_choice}')
    print(f'Computer Choice: {computer_choice}')

game_on = True
while game_on:

    player = rps(choose())
    computer = rps(str(random.randint(1,3)))

    display(player, computer)

    if player == computer:
        print('DRAW. Try again.')
        continue
    elif (player == rock and computer == paper) or (player == paper and computer == scissors) or (player == scissors and computer == rock):
        print('Computer WINS!')
    else:
        print('Player WINS!')
    
    play_again = input('Play again? (y/n): ')
    if play_again[0].upper() != 'Y':
        game_on = False