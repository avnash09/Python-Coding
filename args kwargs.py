def myfunc(*args, **kwargs):
    print(args)
    print(kwargs)
    print(f'I would like {args[1]} {kwargs['fruit']}')

# myfunc(10,20,30,fruit='Apples', food='eggs')

def add(*args):
    total = 0
    for n in args:
        total += n
    return total

result = add(1,2,3,4,5,6)
# print(result)

class Car:

    def __init__(self, **kw):
        # self.make = kw['make']
        # self.model = kw['model']

        self.make = kw.get('make')
        self.model = kw.get('model')
        self.color = kw.get('color')
        self.seats = kw.get('seats')

car = Car(make='Nissan', model='GT-R')
print(car.make, car.model, car.color)