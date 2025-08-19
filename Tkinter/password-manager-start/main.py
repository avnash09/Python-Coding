from tkinter import *
from tkinter import messagebox
import os, random, pyperclip, pandas as pd, pathlib, json
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '%', '+', '@']
NO_OF_LETTERS = (8, 9, 10, 11, 12)
DATA_STORE_HEADERS = ['Website', 'Email', 'Password']

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

# ---------------------------- SEARCH WEBSITE ------------------------------- #
def search():

    input_website = website_entry.get().strip().capitalize()
    # data_file = dir_path+'data.txt'
    data_file = dir_path+'data.json'
    password = ''

    ####################################################################################################################
    ############################## Intentionally commented this code ###################################################
    # data = pd.read_csv(data_file, header=None, index_col=False, delimiter='|', names=DATA_STORE_HEADERS)
    # websites = [site.strip() for site in data.Website.unique()]
    # if input_website in websites:
    #     line = data[data.Website == input_website+' ']
    #     email = line.Email.item()
    #     password = line.Password.item()
    #     messagebox.showinfo(title=f"{input_website} details", message=f"Email: {email}\nPassword: {password}\n")
    ####################################################################################################################

    ####################################################################################################################
    ############ Code placeholder for update password functionality ####################################################
    # else:
    #     pass
        # upd_pwd = messagebox.askyesno("Update Password", message="Do you want to update your password?")
        # if upd_pwd:
        #     data.loc[data.Website == input_website, 'Password'] = password
        #     data.to_csv(data_file, sep="|", header=False, index=False)
    ####################################################################################################################

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_entry():
    website_name = website_entry.get().strip().capitalize()
    email_id = email_entry.get().strip()
    password = password_entry.get().strip()

    if not website_name:
        print('Enter Website name.')
        messagebox.showwarning(title="Error", message="Please enter website.")
    elif not password:
        print('Enter password')
        messagebox.showwarning(title="Error", message="Please enter a password.")            
    else:
        ####################################################################################################################
        ############################## Intentionally commented this code ###################################################
        # is_ok = messagebox.askokcancel(title=website_name, message=f"Wesbite: {website_name}\nEmail: {email_id}\nOk to Save?")
        # if is_ok:
        #     with open(dir_path+"data.txt", mode='a') as data_file:
        #         data_file.write(f"{website_name.title()} | {email_id} | {password}\n")
        ####################################################################################################################

        #Changing the file format to json
        #New data mimicking the json format
        new_data = {
            website_name: {
                'email': email_id,
                'password': password
            }
        }

        try:
            with open(dir_path+'data.json', mode='r') as data_file:
                #Reading the data
                data = json.load(data_file)
        except FileNotFoundError:
            data = new_data
        else:
            #updating old data with new data
            data.update(new_data)
        finally:
            with open(dir_path+'data.json', mode='w') as data_file:
                #saving the updated data
                json.dump(data, data_file, indent=4)

        messagebox.showinfo(title="Success", message="Data Store saved successfully.")
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

website_entry = Entry(width=35, justify='left')
website_entry.grid(column=1, row=1, columnspan=1)
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

search_button = Button(text="Search", width=15, command=search)
search_button.grid(column=2, row=1)

window.mainloop()