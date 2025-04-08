import os
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', ' ', '[', ']', '{', '}', '|', '\\', ':', ';', '"', "'", '<', '>', ',', '.', '?', '/']

characters = letters + numbers + symbols

def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def ceasar_cipher(message, shift_number, action):

    if action == 'decode':
        shift_number *= -1

    output_msg = ''
    for each_letter in message:

        if each_letter not in characters:
            output_msg += each_letter
        else:
            index = characters.index(each_letter)
            adj_index = (index+shift_number) % len(characters)
            output_msg += characters[adj_index]

    print(f'Your {action}d message is --> {output_msg}')

clear_terminal()

while True:

    cipher_action = input("Type 'encode' to encode a message, Type 'decode' to decode.\n")

    if cipher_action.lower() not in ['encode', 'decode']:
        print('Invalid input! Try again.')
        continue

    else:

        message = input('Type your message to encode: ')
        shift_number = int(input('Enter shift number: '))
        ceasar_cipher(message.lower(), shift_number, cipher_action)

    continue_cipher = input('Do you want to continue? (y/n): ')

    if continue_cipher[0].upper() != 'Y':
        break




'''
## OLD CODE
#encoded_msg = ''.join([letters[(letters.index(each_letter)+shift_number) if (letters.index(each_letter)+shift_number) < 26 else ((letters.index(each_letter)+shift_number) % 26)] for each_letter in message])

def encode(message, shift_number):

    encoded_msg = ''
    for each_letter in message:
        index = characters.index(each_letter)
        adj_index = (index+shift_number) if (index+shift_number) < len(characters) else ((index+shift_number) % len(characters))
        encoded_msg += characters[adj_index]

    print(message, '-->', encoded_msg, '-',shift_number)

def decode(message, shift_number):

    decoded_msg = ''
    for each_letter in message:

        index = characters.index(each_letter)
        adj_index = index-shift_number if (index-shift_number) >= 0 else ((index-shift_number) + len(characters))
        decoded_msg += characters[adj_index]

    print(message, '-->', decoded_msg)


        #clear terminal
        clear_terminal()

        if cipher.lower() == 'encode':

            clear_terminal()

            message = input('Type your message to encode: ')
            shift_number = int(input('Enter shift number: '))
            encode(message.lower(), shift_number)
            break
        #my name is avinash qcdreqidmwde mrewl
        else:

            clear_terminal()

            message = input('Type your message to decode: ')
            shift_number = int(input('Enter shift number: '))
            decode(message.lower(), shift_number)
            break
'''