import os
os.system('cls')

# print(type(os.getcwd()))
# file = open(f"{filepath}my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

filepath = os.getcwd() + "\Files\\"

# with open(f"{filepath}my_file.txt") as file:
#     contents = file.read()
    # print(contents)

# with open(f"{filepath}my_file.txt", mode="a") as file:
#     file.write(input("Enter your text: "))

# with open(f"{filepath}new_file.txt", mode="w") as file:
#     file.write(input("File contents: "))

# with open(f"{filepath}new_file.txt", mode="r") as file:
#     print(file.read())

file1 = []
with open(filepath + 'file1.txt', mode='r') as f:
    file1 = f.readlines()
    
file2 = []
with open(filepath + 'file2.txt', mode='r') as f:
    file2 = f.readlines()

import pandas as pd
data = pd.read_csv(filepath + 'file2.txt')
# print(data)

print([int(num) for num in file1 if num in file2])