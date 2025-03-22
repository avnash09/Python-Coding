class Animal():

    def __init__(self):
        print('Animal created.')

    def eat(self):
        print('Eating.')

class Dog(Animal):

    def __init__(self, breed, name):
        Animal().__init__()
        print('Dog created')
        self.breed = breed
        self.name = name
    
    def speak(self):
        print(f"{self.name} says Woof!")

class Cat(Animal):

    def __init__(self,name):
        super().__init__()
        print('Cat created')
        self.name = name

    def speak(self):
        print(f"{self.name} says Meow!")

niko = Dog('Lab','Niko')
felix = Cat('Felix')

pets = [niko, felix]
for pet in pets:
    pet.speak()

#Trying to use Lamda expressions
#print(list(map(lambda x:x.speak(), pets)))