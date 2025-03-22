def myfunc(*args):
    return [num for num in args if num % 2 == 0]

print(myfunc(5,6,7,8,9))