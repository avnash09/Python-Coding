import requests,os

os.system('cls')

API_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
LAT, LNG = (13.064240, 77.587448)
API_KEY = 'f994da2b47da73e1743bc09dea058dcf'
parameters = {
    'lat': LAT,
    'lon': LNG,
    'appid': API_KEY,
    'cnt': 4
}
res = requests.get(API_ENDPOINT, params=parameters)
res.raise_for_status

weather_data = res.json()
weather_list = (weather_data['list'])

# for row in weather_list:
#     for key, value in row.items():
#         if key == 'weather' and value[0]['id'] < 700:
#             pass #print('Bring an umbrella')

for data in weather_data['list']:
    condition_code = (data['weather'][0]['id'])
    if condition_code < 700:
        print('Bring an Umbrella')
    else:
        print("No rain for the next 12 hrs")