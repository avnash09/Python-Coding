import pandas as pd, os

def clear_terminal():
    if os.name == 'nt': os.system('cls')
    else: os.system('clear')
clear_terminal()

work_dir = os.getcwd() + "/Pandas/NATO-alphabet-start/"
csv_file = 'nato_phonetic_alphabet.csv'
filepath = work_dir + csv_file

df = pd.read_csv(filepath)
# print(df.columns.tolist())
# print(df.sample(3))

nato_dict = {row.letter:row.code for index, row in df.iterrows()}
print(nato_dict)

user_input = input("Enter a word: ").upper()
phonetic_words = [nato_dict[letter] for letter in user_input]

print(phonetic_words)