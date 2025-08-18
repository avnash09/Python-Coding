from tkinter import *
import os, random

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
NO_OF_LETTERS = 10

if os.name == 'nt':os.system('cls')
else: os.system('clear')

#check if the folder exists, if not create a new folder
dir_path = "./Tkinter/password-manager-start/"
if not os.path.exists(dir_path):
    # os.makedirs(dir_path)
    print("folder created")
else:
    print("folder exists")
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    pwd = ""
    while len(pwd) != NO_OF_LETTERS:
        letters = random.sample(LETTERS)
        nums = random.sample(NUMBERS)
        syms = random.sample(SYMBOLS)
    print('Password generated')

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_entry():
    website_name = website_entry.get()
    email_id = email_entry.get()
    if not os.path.exists(dir_path+"data.txt"):
        write_mode = 'w'
    else:
        write_mode = 'a'
    write_mode = 'w'
    
    with open(dir_path+"data.txt", mode=write_mode) as data_file:
        data_file.write(f"{website_name} | {email_id} | \n")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg='white') #width=300, height=300

canvas = Canvas(width=200, height=200, bg='white', highlightthickness=0)
pass_img = PhotoImage(file='./Tkinter/password-manager-start/logo.png')
canvas.create_image(100, 100, image=pass_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:", bg='white')
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:", bg='white')
email_label.grid(column=0, row=2)

password_label = Label(text="Password:", bg='white')
password_label.grid(column=0, row=3)

website_entry = Entry(width=54, justify='left', textvariable=StringVar())
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=54, justify='left')
email_entry.insert(END, "avinash@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=35, justify='left')
password_entry.grid(column=1, row=3)

gen_pwd_button = Button(text="Generate Password", bg='white', justify='left', command=generate_password)
gen_pwd_button.grid(column=2, row=3)

add_button = Button(text="Add", width=46, bg='white', justify='left', command=save_entry)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()