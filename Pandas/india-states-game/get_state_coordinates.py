import os, time, pandas as pd, turtle

def clear_terminal():
    if os.name == 'nt': os.system('cls')
    else: os.system('clear')
clear_terminal()

work_dir = os.getcwd() + "/Pandas/india-states-game/"
image = work_dir + "india_blank_states_img.gif"
coordinates_list = []
screen = turtle.Screen()
screen.title("India States game")
screen.setup(width=900, height=900)
screen.addshape(image)
turtle.shape(image)

def save_onclick_coor(x, y):
    print(f"Clicked at: ({x}, {y})")
    coordinates_list.append((x, y))
    if len(coordinates_list) == len(all_states) + 1:
        print(f"Collected {len(coordinates_list)} coordinates.")
        coordinates_list.pop(0) #First click is a initialization click, which is not required
        print(coordinates_list)
        coordinates_dict = {
            'state': all_states,
            'x': [c[0] for c in coordinates_list],
            'y': [c[1] for c in coordinates_list]
        }
        coordinates_df = pd.DataFrame(coordinates_dict)
        coordinates_df.to_csv(work_dir + 'indian_states_coordinates.csv', index=False)
        turtle.bye()
    else:
        print(next(state_gen))

#Loop through all Indian states & get their Screen coordinates
df = pd.read_csv(work_dir + 'state_names.csv')
# print(df.columns.item())    #State
all_states = df.State.to_list()

#Creating a generator to run onclick basis
state_gen = map(lambda state: state, all_states)

screen.onscreenclick(save_onclick_coor)

turtle.mainloop()