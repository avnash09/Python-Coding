class Dog():

    #Class object attribute
    #Available for any instance of the class

    species = 'Mammal'

    def __init__(self, breed, name):

        self.breed = breed
        self.name = name

    #Operations/Actions ----> Methods

    def bark(self):
        print(f'WOOF! My name is {self.name}. ')


my_dog = Dog('English Retriever', 'Cookie')
print(my_dog.breed)
print(my_dog.name, my_dog.species)

my_dog.bark()