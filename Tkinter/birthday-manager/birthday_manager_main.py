from tkinter import *
from tkinter import messagebox, ttk
import os, datetime as dt, json, pandas as pd

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
YEARS = [year for year in range(dt.datetime.now().year, 1950, -1)]

image_filename = 'birthday_manager.png'
csv_filename = 'birthdays.csv'
json_filename = 'birthdays.json'

def clear_terminal():
    if os.name == 'nt': os.system('cls')
    else: os.system('clear')
clear_terminal()

def read_json_file(path="./Tkinter/birthday-manager/", filename=json_filename):
    '''
    Function accepts a JSON file (Only file name)
    Default path: ./Tkinter/birthday-manager/
    '''
    filepath = f"./Tkinter/birthday-manager/{filename}"
    with open(filepath, mode='r') as data_file:
        df = json.load(data_file)
        return df

def save_entry(event=None):
    
    global person_name, person_email, birthday_date, birthday_month, birthday_year
    person_name = name_entry.get().strip().title()
    person_email = email_entry.get().strip()
    
    if person_name == '':
        messagebox.showerror(title='Error', message="Person name missing")
    elif (
        (not birthday_date.isnumeric() or birthday_date == '') or 
        (not birthday_date.isnumeric() or birthday_month == '') or 
        (not birthday_date.isnumeric() or birthday_year == '')
          ):
        messagebox.showerror(title="Error", message="Invalid date")
    elif person_email == '' or '@' not in person_email or not person_email.endswith('.com'):
        messagebox.showerror(title='Error', message="Invalid email ID")
    else:
        print(f"Name: {person_name}")
        print(f"Email: {person_email}")
        # print(f"Birthday: {birthday_date}-{MONTHS_DICT[birthday_month][1]}-{birthday_year}")
        birthday = (birthday_year, birthday_month, birthday_date)
        print(f"Birthday: {get_birthday_string(birthday_date=birthday)}")

        reset_fields()
        save_json_data_file()
        # create_csv_file()
    
    #Puts the cursor in the name_entry field
    name_entry.focus()

def reset_fields():
    name_entry.delete(0, END)
    name_entry.focus()
    year_dropdown.set('year')
    month_dropdown.set('month')
    date_dropdown.set('date')
    email_entry.delete(0, END)

def create_csv_file():
    
    with open(f"./Tkinter/birthday-manager/{csv_filename}", mode='w') as f:
            f.write(f"{person_name}|{person_email}|{birthday_year}|{MONTHS_DICT[birthday_month][1]}|{birthday_date}")

def save_json_data_file():
    
    new_entry = {
        person_name: {
            'email': person_email,
            'birthday': tuple([birthday_year, MONTHS_DICT[birthday_month][1], birthday_date])
        }
    }

    try:
        with open(f"./Tkinter/birthday-manager/{json_filename}", mode='r') as data_file:
            data = json.load(data_file)
    except json.JSONDecodeError:
        print("Invalid JSON format.")
        data = new_entry
    except FileNotFoundError:
        print("No data file exists.")
        data = new_entry
    else:
        data.update(new_entry)
    finally:
        with open(f"./Tkinter/birthday-manager/{json_filename}", mode='w') as data_file:
            json.dump(data, data_file, indent=4)
            messagebox.showinfo(title='Success', message="New data added successfully!")

def custom_messagebox(person):
    custom_window = Tk()
    custom_window.title('')
    custom_window.config(width=100, height=100, padx=20, pady=20)
    
    message_label = Label(custom_window, text="Entry exists", font=(('',12,'bold')))
    message_label.grid(row=1, column=1, columnspan=3)
    
    #read JSON file, get person's details
    data = read_json_file(json_filename)

    birthday_date = data[person]['birthday']
    birthday_string = get_birthday_string(birthday_date)
    person_details = f"Name: {person}\nDOB: {birthday_string}\nEmail: {data[person]['email']}"

    detail_label = Label(custom_window, text=person_details)
    detail_label.grid(row=2, column=2, padx=10, pady=10)

    def update_email():
        email_window = Tk()
        email_window.title("Update Email ID")
        email_window.config(width=50, height=50, padx=20, pady=20)

        email_label = Label(email_window, text="New Email ID")
        email_label.pack(padx=10, pady=5)

        email_entry = Entry(email_window, width=20)
        email_entry.pack(padx=10, pady=5)

        def update_email_data():
            # global person_email
            new_email = email_entry.get().strip()

            if new_email == '' or '@' not in new_email or not new_email.endswith('.com'):
                messagebox.showerror(title='Error', message="Invalid email ID")
            else:
                print(person)
                print(f"New Email: {new_email}")
                # print(f"Birthday: {birthday_date}-{MONTHS_DICT[birthday_month][1]}-{birthday_year}")

                with open(f"./Tkinter/birthday-manager/{json_filename}", mode='r') as data_file:
                    data = json.load(data_file)
                    data[person]['email'] = new_email
                
                with open(f"./Tkinter/birthday-manager/{json_filename}", mode='w') as data_file:
                    json.dump(data, data_file, indent=4)
                    is_ok = messagebox.showinfo(title='Success', message=f"Data Updated\nNew Email: {new_email}")
                    if is_ok:
                        email_window.destroy()
                        custom_window.destroy()
                        print("Email updated.")

        update_button = Button(email_window, text="Update", command=update_email_data)
        update_button.pack(padx=10, pady=5)

    def update_dob():

        dob_window = Tk()
        dob_window.title("Update DoB")
        dob_window.config(width=50, height=50, padx=20, pady=20)

        dob_label = Label(dob_window, text="Date of Birth")
        dob_label.grid(row=1, column=2, pady=10, padx=5)

        upd_date_dropdown = ttk.Combobox(dob_window, values='', width=7, state='readonly')
        upd_date_dropdown.set('date')
        upd_date_dropdown.grid(row=2, column=3, sticky='w', padx=5, pady=10)
        upd_date_dropdown.bind("<<ComboboxSelected>>", get_date)

        upd_month_dropdown = ttk.Combobox(dob_window, values=MONTHS, width=7, state='readonly')
        upd_month_dropdown.set('month')
        upd_month_dropdown.grid(row=2, column=2, sticky='w', padx=5, pady=10)
        upd_month_dropdown.bind("<<ComboboxSelected>>", lambda event: get_month(event, upd_date_dropdown))

        upd_year_dropdown = ttk.Combobox(dob_window, values=YEARS, width=7, state='readonly')
        upd_year_dropdown.set("year")
        upd_year_dropdown.grid(row=2, column=1, sticky='w', padx=5, pady=10)
        upd_year_dropdown.bind("<<ComboboxSelected>>", lambda event: get_year(event, upd_date_dropdown))

        def update_dob_data():
            date = upd_date_dropdown.get().strip()
            month = upd_month_dropdown.get().strip()
            year = upd_year_dropdown.get().strip()

            if date == '' or month == '' or year == '':
                messagebox.showerror(title="Error", message="Invalid date")
            else:
                new_dob = [year, month, date]
                print(person)
                print(f'New DoB: {new_dob}')

                with open(f"./Tkinter/birthday-manager/{json_filename}", mode='r') as data_file:
                    data = json.load(data_file)
                    data[person]['birthday'] = new_dob

                with open(f"./Tkinter/birthday-manager/{json_filename}", mode='w') as date_file:
                    json.dump(data, date_file, indent=4)
                    # dob_dt = dt.datetime.strptime(f"{year}-{month}-{date}", '%Y-%b-%d')
                    dob_string = get_birthday_string(new_dob)
                    is_ok = messagebox.showinfo(title='Success', message=f"Data Updated\nNew DoB: {dob_string}")
                    if is_ok:
                        dob_window.destroy()
                        custom_window.destroy()
                        print("DoB updated.")

        update_button = Button(dob_window, text="Update", command=update_dob_data)
        update_button.grid(row=3, column=2, padx=10, pady=5)

        print('DOB updated')

    def click_update():
        print('Update clicked')
        delete_button.destroy()
        ok_button.destroy()
        # custom_window.destroy()

        cancel_button = Button(custom_window, text='Cancel', width=7, relief="raised", command=close_window)
        cancel_button.grid(row=3, column=2, pady=20, padx=10)

        email_button = Button(custom_window, text="Update Email", command=update_email)
        email_button.grid(row=3, column=3, pady=5, padx=10)

        dob_button = Button(custom_window, text="Update DoB", command=update_dob)
        dob_button.grid(row=4, column=3, pady=5, padx=10)

    def close_window():
        custom_window.destroy()

    def delete_entry():
        print('Deleting entry')
        print(f"Name: {person}\n{data[person]}")
        person_details = f"Name: {person}\nDOB: {birthday_string}\nEmail: {data[person]['email']}"
        confirm_delete = messagebox.askyesno(title='Remove', message=f"Deleting the below records\n\n{person_details}\n\nAre you sure?")
        if confirm_delete:
            data.pop(person)
            # print(data)
        custom_window.destroy()
        name_entry.focus()

        #reload data into JSON file after delete
        with open(f"./Tkinter/birthday-manager/{json_filename}", mode='w') as data_file:
            json.dump(data, data_file, indent=4)
            messagebox.showinfo(title='Deleted', message='Records deleted.')

    update_button = Button(custom_window, text="Update", width=7, relief="raised", command=click_update)
    update_button.grid(row=3, column=1, pady=20, padx=10)

    ok_button = Button(custom_window, text="OK", width=7, relief="raised", command=close_window)
    ok_button.grid(row=3, column=2, pady=20, padx=10)

    delete_button = Button(custom_window, text="Delete", width=7, relief="raised", command=delete_entry)
    delete_button.grid(row=3, column=3, pady=20, padx=10)

    custom_window.mainloop()

def get_birthday_string(birthday_date):
    '''
    This functions accepts DoB in the form of a List or Tuple [year, month, date]
    '''
    year, month, date = birthday_date   #list unpacking
    try:
            bday_dt = dt.datetime.strptime(f"{year}-{month}-{date}", '%Y-%b-%d')
    except ValueError:
        try:
            bday_dt = dt.datetime.strptime(f"{year}-{month}-{date}", '%Y-%B-%d')
        except ValueError:
            print(f'Error. Empty "birthday_date".')
            return None
    finally:
        birthday_string = dt.datetime.strftime(bday_dt, '%d-%b-%Y')

    return birthday_string


#def show_data(person=''):
    try:
        df = pd.read_json(f"./Tkinter/birthday-manager/{json_filename}")
        bday = df[person]['birthday']
    except KeyError:
        print("Key Error: No value for 'person' parameter")
    else:
        try:
            bday_dt = dt.datetime.strptime(f"{bday[0]}-{bday[1]}-{bday[2]}", '%Y-%b-%d')
        except ValueError:
            try:
                bday_dt = dt.datetime.strptime(f"{bday[0]}-{bday[1]}-{bday[2]}", '%Y-%B-%d')
            except ValueError:
                print(f'Unknown Error. Please check the date value for {person}')
                return None
        finally:
            formatted_bday = dt.datetime.strftime(bday_dt, '%d-%b-%Y')
            formatted_output = f"Name: {person}\nDOB: {formatted_bday}\nEmail: {df[person]['email']}"
        return (formatted_output)

def search_entry():
    person = name_entry.get().strip().title()
    if person:
        df = pd.read_json(f"./Tkinter/birthday-manager/{json_filename}")

        if person in df.columns.to_list():
            print(f"{person} already exists")
            custom_messagebox(person)
        else:
            messagebox.showinfo(message="Person details not found")
    else:
        messagebox.showerror(title='Error', message="Person name missing")

    name_entry.focus()

def get_date(event):
    global birthday_date
    birthday_date = event.widget.get()

def get_month(event, related_date_dropdown):
    global birthday_month
    birthday_month = event.widget.get()
    get_valid_date(event, related_date_dropdown)

def get_year(event, related_date_dropdown):
    global birthday_year
    birthday_year = event.widget.get()
    get_valid_date(event, related_date_dropdown)
    # print('inside get_year:', year_dropdown.get())

def is_leap_year(year_input) -> bool:
    try:
        year = int(year_input)
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            return True
        else:
            return False
    except TypeError:
        print(f"Unexpected value of year = {year} inside is_leap_year().")
    except:
        print('Unknown error.')
    
def get_valid_date(event, related_date_dropdown):
    date = birthday_date
    month = birthday_month
    year = birthday_year
    
    if month == 'February' and is_leap_year(year): 
        date_range = [dt for dt in range(1, 30)]    #last date: 29

    elif month == 'February' and not is_leap_year(year):
        date_range = [dt for dt in range(1, 29)]    #last date: 28 

    elif month in ['April','June','September','November']:
        date_range = [dt for dt in range(1, 31)]    #last date: 30

    else:
        date_range = [dt for dt in range(1, 32)]    #last date: 31
    
    related_date_dropdown.set('')
    related_date_dropdown.config(values=date_range)
    if date.isnumeric() and int(date) in date_range:
        related_date_dropdown.set(date)

# ==============================================================================================

window = Tk()
window.title("Birthday Manager")
window.config(width=600, height=600, padx=10, pady=10)

canvas = Canvas(width=300, height=240)
bday_mngr_image = PhotoImage(file=f"./Tkinter/birthday-manager/{image_filename}")
canvas.create_image(150, 120, image=bday_mngr_image)
canvas.grid(row=1, column=1, columnspan=6, padx=10)

name_label = Label(text="Name: ", width=10, anchor='e')
name_label.grid(row=2, column=1)

name_entry = Entry(width=25)
name_entry.focus()
name_entry.grid(row=2, column=2, columnspan=2, pady=5, sticky='ew')

birthday_label = Label(text='Birthday: ', width=10, anchor='e')
birthday_label.grid(row=3, column=1, pady=5)

year_dropdown = ttk.Combobox(values=YEARS, width=7, state='readonly')
year_dropdown.set("year")
year_dropdown.grid(row=3, column=2, sticky='w')
year_dropdown.bind("<<ComboboxSelected>>", lambda event: get_year(event, date_dropdown))
    
month_dropdown = ttk.Combobox(values=MONTHS, width=7, state='readonly')
month_dropdown.set("month")
month_dropdown.grid(row=3, column=3, sticky='w')
month_dropdown.bind("<<ComboboxSelected>>", lambda event: get_month(event, date_dropdown))

date_dropdown = ttk.Combobox(values='', width=7, state='readonly')
date_dropdown.set("date")
# date_dropdown.custom_name = 'date_dropdown'
date_dropdown.grid(row=3, column=4, sticky='w')
date_dropdown.bind("<<ComboboxSelected>>", get_date)

email_label = Label(text="Email ID: ",width=10, anchor='e')
email_label.grid(row=4, column=1)

email_entry = Entry(width=35)
email_entry.grid(row=4, column=2, columnspan=6, pady=5, sticky='w')

save_button = Button(text="Save", width=9, command=save_entry)
save_button.grid(row=5, column=2, columnspan=3, pady=5, padx=5)
window.bind("<Return>", lambda event: save_entry())

search_button = Button(window, text="Search", width=6, command=search_entry)
search_button.grid(row=2, column=4, columnspan=2)#, pady=5, padx=5, sticky='w')
search_button.bind("<Return>", lambda event: search_entry())

window.mainloop()

# ==============================================================================================