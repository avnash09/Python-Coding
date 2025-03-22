# RETURN TRUE IF ANY NUMBER INSIDE THE LIST IS TRUE

def check_even_list(mylist):
    for num in mylist:
        if num % 2 == 0:
            return True
    return False
        
lst = [1,3,5,7,9,2]
print(check_even_list(lst))