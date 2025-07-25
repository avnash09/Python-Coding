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

attempts = {
    "easy": 5,
    "hard": 10
}

print("Choose your level - ")
for level, chances in attempts.items():
    print(f"\t {level} -> {chances} attempts")

difficulty = input("Type 'easy' or 'hard': ")

while True:
    if difficulty.lower() not in ['easy','hard']:
        print("Invalid input!")
        difficulty = input("Type 'easy' or 'hard': ")
    else:
        break

print(difficulty)

def guess_the_number(num):
    pass