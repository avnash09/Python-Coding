import os

os.system('clear')

rows = 10

for i in range(1, rows):
    print(' ' * (rows-i) + '* ' * i)

for i in range(1, rows):
    print(' ' * int((rows/2)+1) + '* ' * int((rows/2)-1))