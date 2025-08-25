from tkinter import *
from tkinter import messagebox, ttk
import os, random, datetime as dt, re

birthday_date = ''
birthday_month = ''
birthday_year = 1900

DATES = [i for i in range(1,32)]
MONTHS = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

YEARS = [year for year in range(1980, dt.datetime.now().year + 1)]

filename = 'birthday_manager.png'

def clear_terminal():
    if os.name == 'nt': os.system('cls')
    else: os.system('clear')
clear_terminal()

window = Tk()
window.title("Birthday Manager")
window.config(width=600, height=600, padx=10, pady=10)

label = Label(text="Welcome to Birthday Manager")
# label.grid(row=0, column=0, columnspan=9)

canvas = Canvas(width=300, height=240)
bday_mngr_image = PhotoImage(file=f"./SMTP/birthday-wisher-extrahard-start/{filename}")
canvas.create_image(150, 120, image=bday_mngr_image)
canvas.grid(row=1, column=1, columnspan=6, padx=10)

def save_entry():
    print(f"Birthday: {birthday_date}-{birthday_month}-{birthday_year}")

def get_name(event=None):
    person = name_entry.get().strip().title()
    print(person)
    if birthday_date == '' or birthday_month == '' or birthday_year == '':
        messagebox.showerror()
    save_entry()

def get_date(event):
    global birthday_date
    print('inside get_date: ', date_dropdown.get()) 
    birthday_date = date_dropdown.get()
    # month_dropdown.config(values=select_months(birthday_date))

def get_month(event):
    global birthday_month
    print('inside get_month: ',month_dropdown.get()) 
    birthday_month = month_dropdown.get()
    is_valid_date()

def get_year(event):
    global birthday_year
    print('inside get_year:', year_dropdown.get())
    birthday_year = year_dropdown.get()
    print(f"Birthday year {birthday_year}")
    is_valid_date()

def is_leap_year(year_input) -> bool:
    try:
        year = int(year_input)
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            # print('inside leap_year(): Leap Year')
            return True
        else:
            # print('inside leap_year(): not a leap year')
            return False
    except TypeError:
        print(f"Unexpected value of year = {year} inside is_leap_year().")
    except:
        print('Unknown error.')
    
def is_valid_date(year='', month='', date=''):
    date = birthday_date
    month = birthday_month
    year = birthday_year

    print(f"Date: {date}, Type: {type(date)}")
    print(f"Month: {month}, Type: {type(month)}")
    print(f"Year: {year}, Type: {type(year)}")
    
    if month == 'February' and is_leap_year(year): 
        date_range = [dt for dt in range(1, 30)]    #last date: 29

    elif month == 'February' and not is_leap_year(year):
        date_range = [dt for dt in range(1, 29)]    #last date: 28 

    elif month in ['April','June','September','November']:
        date_range = [dt for dt in range(1, 31)]    #last date: 30

    else:
        # print('Else statement')
        date_range = [dt for dt in range(1, 32)]    #last date: 31

    date_dropdown.delete(0, END)
    date_dropdown.config(values=date_range)
    if birthday_date.isnumeric() and int(birthday_date) in date_range:
        date_dropdown.set(birthday_date)

label = Label( text="")
# label.grid(row=4, column=0)

name_label = Label(text="Name: ", width=10, anchor='e')
name_label.grid(row=2, column=1)

name_entry = Entry(width=35)
name_entry.focus()
name_entry.grid(row=2, column=2, columnspan=6, pady=5, sticky='w')

birthday_label = Label(text='Birthday: ', width=10, anchor='e')
birthday_label.grid(row=3, column=1, pady=5)

date_dropdown = ttk.Combobox(values='', width=7)
date_dropdown.set("date")
date_dropdown.grid(row=3, column=4)
date_dropdown.bind("<<ComboboxSelected>>", get_date)

delimiter_label1 = Label(text="/", width=1)
# delimiter_label1.grid(row=3, column=3, sticky='ew')
    
month_dropdown = ttk.Combobox(values=MONTHS, width=7)
month_dropdown.set("month")
month_dropdown.grid(row=3, column=3)
month_dropdown.bind("<<ComboboxSelected>>", get_month)

delimiter_label2 = Label(text="/", width=1)
# delimiter_label2.grid(row=3, column=5, sticky='ew')

year_dropdown = ttk.Combobox(values=YEARS, width=7)
year_dropdown.set("year")
year_dropdown.grid(row=3, column=2)
year_dropdown.bind("<<ComboboxSelected>>", get_year)

save_button = Button(text="Save", width=9, command=get_name)
save_button.grid(row=4, column=2, columnspan=3, pady=5)
window.bind("<Return>", lambda event: get_name())


window.mainloop()