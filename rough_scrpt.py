def add(x,y):
    return x+y

# print(add(4,5))

my_function = "This is a variable."

def my_function():
    return "This is a function."

# print(my_function) # Output: This is a variable


from prettytable import PrettyTable

table = PrettyTable()
table.add_column('Pokemon Name', ['Pikachu','Squirtle','Charmander'])
table.add_column('Type', ['Electric','Water','Fire'])
table.align = 'l'
print(table)