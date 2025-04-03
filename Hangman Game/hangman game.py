from hangman import hangman_dict, hangman, hangman_logo
import requests, random, os

def clear_terminal():
    if os.name =='nt': #windows
        os.system('cls')
    else: #Linus based system
        os.system('clear')


no_of_letters = [4,5,6,7,8]

#base_url = 'https://random-word-api.herokuapp.com/word'
#base_url = 'https://random-word-api.herokuapp.com/word?number={}'
#base_url = 'https://random-word-api.herokuapp.com/word?length={}'
#base_url = 'https://random-word-api.vercel.app/api?words=10&length=4'
base_url = 'https://random-word-api.vercel.app/api'

#url = base_url.format(2)
length = random.choice(no_of_letters)

res = requests.get(base_url, params={'words':1, 'length':length, 'type':'uppercase'})
#print(f'length, {length}, {res.json()[0]}')

generated_word = res.json()[0]
#print(generated_word)

dictionary_api_url = f'https://api.dictionaryapi.dev/api/v2/entries/en/{generated_word}'

meaning = []
part_of_speech = []
hint = []

try:
    
    # Send a request to the API
    response = requests.get(dictionary_api_url)
     
     # Check if the request was successful
    response.raise_for_status()  # Raises an HTTPError if the response was unsuccessful

    # Extract the meaning from the response
    meanings = response.json()[0]['meanings']
    meaning.append(meanings[0]['definitions'][0]['definition'])
    meaning.append(meanings[1]['definitions'][0]['definition'])

    part_of_speech.append(meanings[0]['partOfSpeech'].capitalize())
    part_of_speech.append(meanings[1]['partOfSpeech'].capitalize())

    hint = [part_of_speech, meaning]

except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")

except Exception as err:
        print(f"An error occurred: {err}")

else:
    print(f"Error: Unable to fetch meaning for the word '{generated_word}'")


if __name__ == '__main__':

    #Clear the terminal
    clear_terminal()

    print(hangman_logo)
    print(hangman)
    print('###############################\n')
    print("Let's play!")
    print(f"It's a {len(generated_word)} letter word. Can you guess it?")

    word_list = list(generated_word)
    #print(word_list)

    blank_spaces = ['-'] * len(generated_word)
    guess_word = ''.join(blank_spaces)

    chances = len(generated_word)
    guesses = set()

    print(f"Hint:\t{hint[0][0]}: {hint[1][0]}\n\t{hint[0][1]}: {hint[1][1]}")


    while True:

        if guess_word == generated_word:
            
            #Clear the terminal
            clear_terminal()

            print(' '.join(blank_spaces))
            print(f"The word is '{''.join(blank_spaces)}'.")
            print(f'\nYOU WIN! with {chances} chances left.\n')
            
            break
        
        else:
            
            if chances != len(generated_word):
                print(hangman_dict[chances])

            print(f'\nNo of chances left: {chances}')

            if guesses:
                print(f"Previous guesses: '{','.join(guesses)}'")

            print('\n' + ' '.join(blank_spaces))
            
            guess = input('\nEnter a letter: ').upper()
            if guess in guess_word and guess not in word_list:
                print('You have already guessed this letter.')
                chances -= 1
                
            elif guess not in guess_word and guess in word_list:
                occurences = [index for index, letter in enumerate(word_list) if letter == guess]
                for index in occurences:
                    blank_spaces[index] = guess
                    word_list[index] = '-'

            else:
                chances -= 1

            guesses.add(guess)

        if chances == 0:

            #Clear the terminal
            clear_terminal()

            print(f"YOU LOSE! The word was '{generated_word}'")
            print('\n' + hangman_dict[chances])
            print('\n' + ' '.join(blank_spaces))
            missed_letters = [letter for letter in word_list if letter != '-']
            if missed_letters == blank_spaces:
                print('You missed all the letters!')
            else:
                print(f"\nYou missed the letters {','.join(missed_letters)}\n")

            break
        
        guess_word = ''.join(blank_spaces)