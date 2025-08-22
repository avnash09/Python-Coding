import smtplib, os, random, pandas as pd, datetime as dt

SENDER = 'avinashtestmails@gmail.com'
RECIPIENT = 'avinashlearnspython@gmail.com'

def clear_terminal():
    if os.name == 'nt': os.system('cls')
    else: os.system('clear')
clear_terminal()

def get_dir_hierarchy(folder, sub_folder, files):
    print(f"Folder:\t{folder}")
    for dir in sub_folder:
        print(f"Sub folder:\t{dir}")
    for f in files:
        print(f"Files:\t{f}")
    print('-'*80 + '\n' +'-'*80)

work_dir = "birthday-wisher-extrahard-start"
base_path = "./SMTP/"
letters_dir = "letter_templates"
letters = ''
password_file = 'gmail_app_password.txt'

for folder, sub_folder, files in os.walk(base_path):
    if os.path.basename(folder) == work_dir:
        target_path = folder   # store full path
        get_dir_hierarchy(folder, sub_folder, files)
    elif os.path.basename(folder) == letters_dir:
        letters_path = folder
        letters = files
        get_dir_hierarchy(folder, sub_folder, files)

# print("letters_dir:", letters_dir)
# print("letter_path:", letters_path)
# print("work_dir:", work_dir)
# print('target_path:', target_path)
# print(letters)

if target_path:
    os.chdir(target_path)
    print("Changed working directory to:", os.getcwd())
else:
    print(f"Directory '{work_dir}' not found under {base_path}")

birthdays = pd.read_csv('./birthdays.csv')#, index_col=False)

test = dt.datetime(2025, 12, 9)
test_tuple = (test.day, test.month)

picked_letter = random.choice(letters)

for index, bday_person in birthdays.iterrows():
    if (test.day, test.month) == (bday_person.day, bday_person.month):

        # with open(f"../{password_file}", mode='r') as f:
        #     pwd = f.readline().strip()
        #     print(pwd)

        pwd_data = pd.read_csv(f"../{password_file}", names=['key','value'], delimiter="|", index_col=False)
        data = pwd_data[pwd_data.key == SENDER]
        pwd = data.value.item()
        # print(pwd)

        with open(os.path.join(letters_dir,picked_letter), mode='r') as f:
            contents = f.read()
            contents = contents.replace('[NAME]', bday_person['name'])
            print(contents)

        with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=SENDER, password=pwd)
            connection.sendmail(from_addr=SENDER,
                                to_addrs=birthdays['email'],
                                msg=f"Subject:Happy Birthday {bday_person['name']}!\n\n{contents}")
