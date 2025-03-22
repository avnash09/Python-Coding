work_hours = [('Abby',100),('Billy',4000),('Cassie',800)]

def employee_check(work_hours):
    max_hours = 0
    employee_of_month = ''

    for employee,hours in work_hours:
        if hours > max_hours:
            max_hours = hours
            employee_of_month = employee

    return(employee_of_month,max_hours)

name,hours = employee_check(work_hours)
print(f"{name} is our employee of the month who has worked {hours} hours.")