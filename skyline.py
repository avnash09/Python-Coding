def myfunc(str):
    new_str = []
    for index in range(0,len(str)):
        if (index+1) % 2 == 0:
            new_str.append(str[index].upper())
        else:
            new_str.append(str[index].lower())
    
    return ''.join(new_str)

result = myfunc(input('Enter a string: '))
print(result)