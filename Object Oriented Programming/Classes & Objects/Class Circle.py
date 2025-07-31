class Circle():

    #Class Object attribute
    pi = 3.14

    def __init__(self, radius = 1):
        
        self.radius = radius
        self.area = Circle.pi * (radius ** 2)

    def get_circumference(self):

        return 2 * Circle.pi * self.radius
    

my_circle = Circle(30)

print(my_circle.get_circumference())
print(my_circle.area)