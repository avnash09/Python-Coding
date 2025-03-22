def myfunc(*args, **kwargs):
    print(args)
    print(kwargs)
    print(f'I would like {args[1]} {kwargs['fruit']}')

myfunc(10,20,30,fruit='Apples', food='eggs')