import os
os.system('cls')

# print(type(os.getcwd()))
# file = open(f"{filepath}my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

filepath = os.getcwd() + "\Files\\"

with open(f"{filepath}my_file.txt") as file:
    contents = file.read()
    # print(contents)

# with open(f"{filepath}my_file.txt", mode="a") as file:
#     file.write(input("Enter your text: "))

# with open(f"{filepath}new_file.txt", mode="w") as file:
#     file.write(input("File contents: "))

with open(f"{filepath}new_file.txt", mode="r") as file:
    print(file.read())