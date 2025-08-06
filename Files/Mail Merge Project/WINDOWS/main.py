#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

import os

os.system('cls')

PLACEHOLDER = "[name]"
current_dir = os.getcwd()
working_dir = current_dir + "\\Files\\Mail Merge Project\\WINDOWS"

# print(working_dir)
# print(os.listdir(working_dir))
# print(letter_text)

with open(working_dir+"\\Input\\Names\\invited_names.txt") as names:
    name_list = names.readlines()

# print(name_list)

with open(working_dir+"\\Input\\Letters\\starting_letter.txt", mode='r') as letter:
    letter_text = letter.read()
    for name in name_list:
        stripped_name = name.strip()
        new_letter = letter_text.replace(PLACEHOLDER, stripped_name)
        with open(working_dir+f"\\Output\\ReadyToSend\\letter_for_{stripped_name}.txt", mode='w') as completed_letter:
            completed_letter.write(new_letter)

# for name in name_list:
#     stripped_name = name.strip()
#     with open(working_dir+f"\\Output\\ReadyToSend\\letter_for_{stripped_name}.txt", mode='w') as f:
#         for line in letter_text:
#             f.write(line.replace(PLACEHOLDER, stripped_name))


path = working_dir + "\\Output\\ReadyToSend"
if os.access(path, os.W_OK):
    print("Write access confirmed.")
else:
    print("No write access to:", path)

    