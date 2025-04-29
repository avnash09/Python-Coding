import os

os.system('clear')

rows = 10

def triangle():

    star_count = 0
    for i in range(1, rows+1):
        print(' ' * (rows-i) + '* ' * i)
        star_count += i
    
    return star_count

def rectangle():

    for i in range(1, rows):
        if rows % 2 == 0:
            print(' ' * int((rows/2)+1) + '* ' * int((rows/2)-1))
        else:
            print(' ' + ' ' * int((rows/2)+1) + '* ' * int((rows/2)-1))

star_count = triangle()


print(f'star count: {star_count}')