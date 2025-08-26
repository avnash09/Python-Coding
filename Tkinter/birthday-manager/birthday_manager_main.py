from tkinter import *
from tkinter import messagebox, ttk
import os, random, datetime as dt, re, json

person_name = ''
person_email = ''
birthday_date = ''
birthday_month = ''
birthday_year = ''

DATES = [i for i in range(1,32)]
MONTHS = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]
MONTHS_DICT = {month : (index+1, month[:3]) for index, month in enumerate(MONTHS)}
YEARS = [year for year in range(1980, dt.datetime.now().year + 1)]

image_filename = 'birthday_manager.png'
csv_filename = 'birthdays.csv'
json_filename = 'birthdays.json'

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
bday_mngr_image = PhotoImage(file=f"./Tkinter/birthday-manager/{image_filename}")
canvas.create_image(150, 120, image=bday_mngr_image)
canvas.grid(row=1, column=1, columnspan=6, padx=10)

def save_entry(event=None):
    
    global person_name, person_email, birthday_date, birthday_month, birthday_year
    person_name = name_entry.get().strip().title()
    person_email = email_entry.get().strip()
    
    if person_name == '':
        messagebox.showerror(title='Error', message="Person name missing")
    elif birthday_date == '' or birthday_month == '' or birthday_year == '':
        messagebox.showerror(title="Error", message="Invalid date")
    elif person_email == '' or '@' not in person_email or not person_email.endswith('.com'):
        messagebox.showerror(title='Error', message="Invalid email ID")
    else:
        print(person_name)
        print(person_email)
        print(f"Birthday: {birthday_date}-{MONTHS_DICT[birthday_month][1]}-{birthday_year}")

        reset_fields()
        # create_csv_file()
        create_json_file()

def reset_fields():
    name_entry.delete(0, END)
    year_dropdown.set('year')
    month_dropdown.set('month')
    date_dropdown.set('date')
    email_entry.delete(0, END)

def create_csv_file():
    
    with open(f"./Tkinter/birthday-manager/{csv_filename}", mode='w') as f:
            f.write(f"{person_name}|{person_email}|{birthday_year}|{MONTHS_DICT[birthday_month][1]}|{birthday_date}")

def create_json_file():
    
    new_entry = {
        'name': person_name,
        'email': person_email,
        'birthday': {
            'year': birthday_year,
            'month': birthday_month,
            'date': birthday_date
        } 
    }

    try:
        with open(f"./Tkinter/birthday-manager/{json_filename}", mode='r') as data_file:
            data = json.read(data_file)
    except FileNotFoundError:
        data = new_entry
    else:
        data.update(new_entry)
    finally:
        with open(f"./Tkinter/birthday-manager/{json_filename}", mode='w') as data_file:
            json.dump(data, data_file, indent=4)

def get_date(event):
    global birthday_date
    print('inside get_date: ', date_dropdown.get()) 
    birthday_date = date_dropdown.get()
    # month_dropdown.config(values=select_months(birthday_date))

def get_month(event):
    global birthday_month
    print('inside get_month: ',month_dropdown.get()) 
    birthday_month = month_dropdown.get()
    get_valid_date()

def get_year(event):
    global birthday_year
    print('inside get_year:', year_dropdown.get())
    birthday_year = year_dropdown.get()
    print(f"Birthday year {birthday_year}")
    get_valid_date()

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
    
def get_valid_date(year='', month='', date=''):
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

    print('+++++++++++++++++++++++')
    print(date_range)
    print(birthday_date.isnumeric())
    print(29 in date_range)
    print('+++++++++++++++++++++++')
    # date_dropdown.delete(0, END)
    date_dropdown.set('')
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

year_dropdown = ttk.Combobox(values=YEARS, width=7, state='readonly')
year_dropdown.set("year")
year_dropdown.grid(row=3, column=2, sticky='w')
year_dropdown.bind("<<ComboboxSelected>>", get_year)

delimiter_label1 = Label(text="/", width=1)
# delimiter_label1.grid(row=3, column=3, sticky='ew')
    
month_dropdown = ttk.Combobox(values=MONTHS, width=7, state='readonly')
month_dropdown.set("month")
month_dropdown.grid(row=3, column=3, sticky='w')
month_dropdown.bind("<<ComboboxSelected>>", get_month)

date_dropdown = ttk.Combobox(values='', width=7, state='readonly')
date_dropdown.set("date")
date_dropdown.grid(row=3, column=4)#, sticky='w')
date_dropdown.bind("<<ComboboxSelected>>", get_date)

delimiter_label2 = Label(text="/", width=1)
# delimiter_label2.grid(row=3, column=5, sticky='ew')

email_label = Label(text="Email ID: ",width=10, anchor='e')
email_label.grid(row=4, column=1)

email_entry = Entry(width=35)
email_entry.grid(row=4, column=2, columnspan=6, pady=5, sticky='w')

save_button = Button(text="Save", width=9, command=save_entry)
save_button.grid(row=5, column=2, columnspan=3, pady=5)
window.bind("<Return>", lambda event: save_entry())


window.mainloop()