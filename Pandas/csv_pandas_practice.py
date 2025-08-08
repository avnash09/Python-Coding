import os, csv, pandas

os.system('cls')

curr_dir = os.getcwd()
work_file = curr_dir + "\\Pandas\\weather_data.csv"
# print(work_dir)

# with open(work_file, mode='r') as f:
#     weather_data = f.readlines()

# for data in weather_data:
#     print(data.strip())

with open(work_file, mode='r') as f:
    data = [data.strip() for data in f.readlines()]
    # print(data)

#using csv library
with open(work_file, mode='r') as f:
    data = csv.reader(f)
    temperatures = []
    for row in data:
        # print(row)
        if row[1] != 'temp':
            temperatures.append(int(row[1]))

    # print(temperatures)

data = pandas.read_csv(work_file)
# print(data["temp"])
print(data.temp)
print(data.temp.to_list())

data_dict = data.to_dict()
# print(data_dict)

temp_list = data["temp"].to_list()
avg_temp = sum(temp_list) / len(temp_list)
# print(round(avg_temp, 2))

#Get data in column
# print(data["temp"].mean())
# print(data["temp"].max())

# print(data.temp.mean())

#Get data in row
# print(data[data.day == 'Monday'])

#Get the row which has the highest temperature
max_temp = data.temp.max()
# print(data[data.temp == max_temp])

#Get Monday's temperature & convert it into Fahrenheit
monday = data[data.day == "Monday"]
# print(monday)
monday_temp = monday.temp
# print(monday_temp[0])
monday_temp_F = monday_temp[0] * (9/5) + 32
# print(monday_temp_F)

#Create a Dataframe from scratch

data_dict = {
    "students": ["Avinash", "Annie", "Binay"],
    "scores": [76, 85, 89]
}

data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv(curr_dir + "\\Pandas\\students.csv")