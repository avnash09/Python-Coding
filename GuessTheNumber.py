import random, os

def clear_terminal():
    if os.name == "nt": #Windows
        os.system("cls")
    else:   #Mac/Linux
        os.system("clear")

clear_terminal()

def guess():
    return input("Enter your guess: ")

user_guess = guess()

while True:
    if not user_guess.isdigit():
        print("This is not a number, Please try again.")
        user_guess = guess()
    else:
        break
    
    
    
print(user_guess)

def guess_the_number(num):
    pass