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
    "easy": 3,
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

def guess_the_number(number, user_guess, attempt):
    
    # previous_guesses = [0]
    if user_guess == number:
        print(f"Your guessed it right! the number was {number}.")
        return (True, attempt -1)
    else:
        if attempt > 1:
            if user_guess > number:
                print("Too high")
            else:
                print("Too low")
            print("Guess again.")
        else:
            print("Out of guesses!")
            print(f"The correct number was {chosen_number}.")
        return (False, attempt -1)

        # if user_guess - number < previous_guesses[-1] - number:
        #     print("Getting closer")
        # else:
        #     print("Previous guess was better.")
    # previous_guesses.append(user_guess)

print("Welcome to the Number Guessing game!")
print("I'm thinking of a number between 1 and 100.")

attempts=no_of_attempts()
chosen_number = random.randint(1, 100)
print(f"Correct number is {chosen_number}")
correct_guess = False

while not correct_guess and attempts > 0:
    print(f"turn: {attempts}")
    print(f"You have {attempts} guesses left to guess the number")
    #Tuple unpacking
    correct_guess, attempts = guess_the_number(number = chosen_number, user_guess = guess(), attempt= attempts)
