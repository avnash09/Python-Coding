from hangman import hangman_dict, hangman, hangman_logo
import requests, random, os

def clear_terminal():
    if os.name =='nt': #windows
        os.system('cls')
    else: #Linus based system
        os.system('clear')


no_of_letters = [4,5,6,7,8]

base_url = 'https://random-word-api.vercel.app/api'

#url = base_url.format(2)
length = random.choice(no_of_letters)

res = requests.get(base_url, params={'words':1, 'length':length, 'type':'uppercase'})
#print(f'length, {length}, {res.json()[0]}')

generated_word = res.json()[0]
#print(f'generated word: {generated_word}')

dictionary_api_url = f'https://api.dictionaryapi.dev/api/v2/entries/en/{generated_word}'

try:
    
    # Send a request to the API
    response = requests.get(dictionary_api_url)
     
     # Check if the request was successful
    response.raise_for_status()  # Raises an HTTPError if the response was unsuccessful

    # Extract the meaning from the response
    meanings = response.json()[0]['meanings']

    print(response.status_code)

except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")

except Exception as err:
        print(f"An error occurred: {err}")

except IndexError:
    print('Index Error.')

else:
    if response.status_code != 200:
        print(f"Error: Unable to fetch meaning for the word '{generated_word}'")
finally:
    hints = {}
    
    for meaning in meanings:
        part_of_speech = meaning['partOfSpeech']
        definitions = meaning['definitions']
        #hints.append(f"\t{part_of_speech}: {definition['definition']}")
        hints[part_of_speech] = [definition['definition'] for definition in definitions]
    #print(hints)


if __name__ == '__main__':

    #Clear the terminal
    #clear_terminal()

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

            print(f'\nHint: {len(generated_word)} letter word.\n')
            for key in hints.keys():
                print('\t'+key+': '+hints[key][0])

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

'''
#base_url = 'https://random-word-api.herokuapp.com/word'
#base_url = 'https://random-word-api.herokuapp.com/word?number={}'
#base_url = 'https://random-word-api.herokuapp.com/word?length={}'
#base_url = 'https://random-word-api.vercel.app/api?words=10&length=4'

#meaning = []
#part_of_speech = []
#hint = []

    meaning.append(meanings[0]['definitions'][0]['definition'])
    meaning.append(meanings[1]['definitions'][0]['definition'])

    part_of_speech.append(meanings[0]['partOfSpeech'].capitalize())
    part_of_speech.append(meanings[1]['partOfSpeech'].capitalize())

    hint = [part_of_speech, meaning]
    print(hint, part_of_speech, meaning)

'''