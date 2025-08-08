import os,pathlib, pandas as pd

def clear_terminal():
    if os.name == 'nt': os.system('cls')
    else: os.system('clear')

clear_terminal()

curr_dir = os.getcwd()
filename = "2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv"
filepath = curr_dir + "\\Pandas\\" + filename
dir = curr_dir + "\\Pandas\\"

# print(os.path.exists(filepath))
# print(pathlib.Path(filepath).exists())

data = pd.read_csv(filepath)
# print(data.head())    # Print the first 5 rows
# print(type(data.columns))   #<class 'pandas.core.indexes.base.Index'>
# print(data.columns)
# print(data.columns.to_list())

# ================== Easy Method ==================

gray_count = len(data[data['Primary Fur Color'] == 'Gray'])
cinnamon_count = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black_count = len(data[data['Primary Fur Color'] == 'Black'])

data_dict = {
    "fur colors": ['Gray','Cinnamon','Black'],
    "count": [gray_count, cinnamon_count, black_count]
}

df = pd.DataFrame(data_dict)
df.to_csv(dir + "squirrel_count.csv")

# ================== Easy Method ==================

all_fur_colors = data['Primary Fur Color']
# print(all_fur_colors)

fur_colors = all_fur_colors.dropna().unique()
print(type(fur_colors)) #<class 'numpy.ndarray'>

color_count = []
for color in fur_colors:
    color_count.append(len(data[data['Primary Fur Color'] == color]))
print(color_count)

color_dict = {
    "fur color": fur_colors.tolist(),
    "count": color_count
}

#Create csv file
df = pd.DataFrame(color_dict)
df.to_csv(dir + "squirrel_count_new.csv")