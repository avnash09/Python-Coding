import random, os

def clear_terminal():
    if os.name == "nt": #Windows
        os.system("cls")
    else:   #Mac/Linux
        os.system("clear")

clear_terminal()

def guess():
    while True:
        num = input("Enter your guess: ")
        if not num.isdigit():
            print("This is not a number, Please try again.")
        else:
            return int(num)

attempts = {
    "easy": 5,
    "hard": 10
}

def no_of_attempts():
    print("Choose your difficulty - ")
    for level, chances in attempts.items():
        print(f"\t {level} -> {chances} attempts")
        
    while True:
        difficulty = input("Type 'easy' or 'hard': ")
        if difficulty.lower() not in ['easy','hard']:
            print("Invalid input!")
        else:
            return attempts[difficulty]

def guess_the_number(number, user_guess):
    
    # previous_guesses = []
    if user_guess == number:
        print(f"Your guessed it right! the number was {number}.")
    else:
        if user_guess > number:
            print("Too high")
        else:
            print("Too low")

print("Welcome to the Number Guessing game!")
print("I'm thinking of a number between 1 and 100.")

attempts=no_of_attempts()
chosen_number = random.randint(1, 100)

for turn in range(attempts, 0, -1):
    print(f"You have {turn} guesses left to guess the number")
    guess_the_number(number = chosen_number, user_guess = guess())
    if turn > 1:
        print("Guess again.")
    else:
        print("Out of guesses!")
        print(f"The correct number was {chosen_number}.")
