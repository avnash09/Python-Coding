hangman = '''
    ________
    |/     |
    |      |
    |      O
    |     /|\\
    |     / \\
    |_______
    '''
hangman_logo = '''
###############################
####### H A N G M A N #########
###############################
'''
hangman_dict = {
    7:
    '''
    
    
    
    
    
    
    ._______
    ''',
    6:
    '''
    
    |
    |      
    |      
    |     
    |     
    |_______
    ''',
    5:
    '''
    ________
    |/     
    |      
    |      
    |     
    |     
    |_______
    ''',
    4:
    '''
    ________
    |/     |
    |      |
    |      O
    |     
    |     
    |_______
    ''',
    3:
    '''
    ________
    |/     |
    |      |
    |      O
    |     /|
    |     
    |_______
    ''',
    2:
    '''
    ________
    |/     |
    |      |
    |      O
    |     /|\\
    |     
    |_______
    ''',
    1:
    '''
    ________
    |/     |
    |      |
    |      O
    |     /|\\
    |     / 
    |_______
    ''',
    0:
    '''
    ________
    |/     |
    |      |
    |      O
    |     /|\\
    |     / \\
    |_______
    '''
}

if __name__ == '__main__':
    while True:
        i = input("Enter a number from 0-7 (x to exit): ")

        if not i.isdigit():
            if i[0].lower() == 'x':
                break
            else:
                print('Invalid input. try again.')
        elif (int(i) not in hangman_dict.keys() and i[0].lower() != 'x'):
            print('Invalid input. try again.')
            continue
        else:
            print(hangman_dict[int(i)])

