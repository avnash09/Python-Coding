import smtplib, os, datetime as dt, pandas as pd, random
DAYS_OF_THE_WEEK = {
    0:'Monday',1:'Tuesday',3:'Wednesday',4:'Thursday',5:'Friday',6:'Saturday',7:'Sunday'
}

os.system('cls')

# my_email = 'avinash.rkl09@gmail.com'
# password = 'vodftbmskqodvnoa'
# to_mail = 'sa.anand2809@gmail.com'

# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, 
#                         to_addrs=to_mail, 
#                         msg="Subject:Hello!\n\nemail body msg")

# now = dt.datetime(year = 1992, month=12, day=9)
# print(now.weekday())

quotes = pd.read_csv('./SMTP/Birthday-Wisher/quotes.txt', index_col=False, names=["Quotes"])
q_list = quotes.Quotes.to_list()
quote_of_the_day = random.choice(q_list)

#Get the day of the week
day = dt.datetime.now()
day_num = day.weekday()
day_of_the_week = DAYS_OF_THE_WEEK[day_num]

#Get Gmail App Password
with open("./SMTP/gmail_app_password.txt", mode='r') as p:
    details = p.readlines()
    mail_password = details[0]
    host_info = details[1]
    # host_info = details[1][0]
    # port_info = int(details[1][1])
    # print(details, host_info)

#Send Email

sender = "avinash.rkl09@gmail.com"
receiver = "sa.anand2809@gmail.com"

with smtplib.SMTP(host="smtp.gmail.com", port=587) as connect:
    connect.starttls()
    connect.login(user=sender, password=mail_password)
    connect.sendmail(from_addr=sender,
                    to_addrs=receiver,
                    msg=f"Subject:Quote of the day\n\nHey! Its {day_of_the_week}! A special quote for you today.\n\n{quote_of_the_day}.")
# connect.close()
