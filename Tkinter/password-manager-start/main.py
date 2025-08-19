from tkinter import *
from tkinter import messagebox
import os, random, pyperclip

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '%', '+', '@']
NO_OF_LETTERS = (8, 9, 10, 11, 12)

if os.name == 'nt':os.system('cls')
else: os.system('clear')

#check if the folder exists, if not create a new folder
dir_path = "./Tkinter/password-manager-start/"
if not os.path.exists(dir_path):
    # os.makedirs(dir_path)
    print("New folder created.")
# else:
#     print("folder exists")
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    password = ""
    while len(password) not in NO_OF_LETTERS:
        letters = random.sample(LETTERS, random.randint(6, 10))
        nums = random.sample(NUMBERS, random.randint(2, 4))
        syms = random.sample(SYMBOLS, random.randint(2, 4))
        #combine all the characters in a list
        password_list = (letters + nums + syms)
        #Shuffle the characters
        random.shuffle(password_list)
        #Create a password string out of the shuffled list
        password = ''.join(password_list)

    password_entry.delete(0, END)   #clears the password entry pane
    password_entry.insert(0, string=password)   #shows the password generated in the entry pane
    #Copy the password to the clipboard automatically
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_entry():
    website_name = website_entry.get().strip()
    email_id = email_entry.get().strip()
    password = password_entry.get().strip()

    if not website_name:
        print('Enter Website name.')
        messagebox.showwarning(title="Error", message="Please enter website.")
    elif not password:
        print('Enter password')
        messagebox.showwarning(title="Error", message="Please enter a password.")
    else:
        is_ok = messagebox.askokcancel(title=website_name, message=f"There are the details entered:\nEmail: {email_id}\nIs it ok to save?")
        if is_ok:
            with open(dir_path+"data.txt", mode='a') as data_file:
                data_file.write(f"{website_name} | {email_id} | {password}\n")
            messagebox.showinfo(title="Success", message="Data  Store saved successfully.")
            #wipe the entries clean from the window
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50) #width=300, height=300

canvas = Canvas(width=200, height=200, highlightthickness=0)
pass_img = PhotoImage(file='./Tkinter/password-manager-start/logo.png')
canvas.create_image(100, 100, image=pass_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

website_entry = Entry(width=54, justify='left')
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=54, justify='left')
email_entry.insert(END, "avinash@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=35, justify='left')
password_entry.grid(column=1, row=3)

gen_pwd_button = Button(text="Generate Password", justify='left', command=generate_password)
gen_pwd_button.grid(column=2, row=3)

add_button = Button(text="Add", width=46, justify='left', command=save_entry)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()