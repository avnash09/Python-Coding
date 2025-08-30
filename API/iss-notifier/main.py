import requests, os, datetime as dt, pandas as pd
import smtplib
os.system('cls')

LAT = 13.064240
LNG = 77.587448
SENDER = 'avinashtestmails@gmail.com'
RECIPIENT = 'avinashlearnspython@gmail.com'
MAIL_FILE = 'gmail_app_password.txt'
DIR_PATH = './SMTP/'

def is_iss_overhead():
    iss_url='http://api.open-notify.org/iss-now.json'

    response = requests.get(url=iss_url)
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data['iss_position']['latitude'])
    iss_longitude = float(data['iss_position']['longitude'])

    if (LAT-5 <= iss_latitude <= LAT+5) and (LNG-5 <= iss_longitude <= LNG+5):
        return True
    return False

def is_night_time():
    sun_url = 'https://api.sunrise-sunset.org/json'
    parameters = {
        'lat': LAT,
        'lng': LNG,
        'formatted': 0,
        'tzid': 'Asia/Kolkata'
        }

    res = requests.get(sun_url, params=parameters)
    res.raise_for_status()
    data = res.json()
    sunrise = int(data['results']['sunrise'].split("T")[1].split(":")[0])
    sunset = int(data['results']['sunset'].split("T")[1].split(":")[0])

    print(sunrise, sunset)
    print(dt.datetime.now().hour)

    time_now = dt.datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True

def get_mail_pwd(dir, filename):
    filepath = dir + filename
    data = pd.read_csv(filepath, sep='|', index_col=False, names=['key', 'value'])
    pwd_data = data[data.key == SENDER]
    return pwd_data.value.item()

if is_night_time() and is_iss_overhead():
    password = get_mail_pwd(DIR_PATH, MAIL_FILE)
    
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=SENDER, password=password)
        connection.sendmail(
            from_addr=SENDER,
            to_addrs=RECIPIENT,
            msg=f"Subject:Look Up!\n\nThe ISS is above you in the sky."
        )