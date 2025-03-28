def create_cubes_list(n):
    result = []
    for x in range(n):
        result.append(x ** 3)
    return result

def create_cubes(n):
    for num in range(n):
        yield num ** 3

#print(create_cubes_list(3))
for i in create_cubes(3):
    pass #print(i)

#Create a generator that yields "n" random numbers between a low and high number (that are inputs).
import random
def rand_num(low, high, n):
    for x in range(n):
        yield random.randint(low, high)

for x in rand_num(1,10, 15):
    pass #print(x)

#print(list(rand_num(1,4,10)))

#print(next(rand_num(1,5,10)))

#Skyline

def skyline(strr):
    for i in range(1, len(strr)+1):
        if i % 2 == 0:
            yield strr[i-1].upper()
        else:
            yield strr[i-1].lower()

print(skyline('Avinash'))

print(list(skyline('Avinash')))

for letter in skyline('Avinash'):
    print(letter)