import os, pandas as pd, turtle

work_dir = os.getcwd() + "\\Pandas\\us-states-game\\"
csv_file = "50_states.csv"
csv_filepath = work_dir + csv_file

def clear_terminal():
    if os.name == 'nt': os.system('cls')
    else: os.system('clear')

clear_terminal()

# screen = turtle.Screen()
# screen.setup(width=800, height=600)
# screen.title('US States Game')
# image = work_dir + "blank_states_img.gif"
# screen.addshape(image)
# turtle.shape(image)

def get_mouse_click_coor(x, y):
    print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)

# for _ in range(3):
#     user_answer = screen.textinput(title="Guess the State", prompt="What's another state's name?")
#     print(user_answer)

#Get data from the csv file
data = pd.read_csv(csv_filepath)
states = data.state.to_list()
print()





# turtle.mainloop()
# s.exitonclick()