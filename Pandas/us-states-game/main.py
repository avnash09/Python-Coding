import os, pandas as pd, turtle, time

work_dir = os.getcwd() + "/Pandas/us-states-game/"
csv_file = "50_states.csv"
csv_filepath = work_dir + csv_file

def clear_terminal():
    if os.name == 'nt': os.system('cls')
    else: os.system('clear')

clear_terminal()

screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.title('US States Game')
image = work_dir + "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
# screen.tracer(0)

def get_mouse_click_coor(x, y):
    print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)

#Get data from the csv file
data = pd.read_csv(csv_filepath)
states = data.state.to_list()

game_on = True
while game_on:
    user_answer = screen.textinput(title="Guess the State", prompt="What's another state's name?")
    # print(user_answer)
    state_name = user_answer.title()
    print(state_name)
    print(state_name in states)
    if state_name in states:
        # state_data = data[data.state == state_name]
        # print(state_data)
        # x = state_data.x[0]
        # y = state_data.y[0]

        x_cor, y_cor = data.loc[data.state == state_name, ['x', 'y']].iloc[0]

        t = turtle.Turtle()
        t.speed('slow')
        t.penup()
        t.hideturtle()
        t.goto(x_cor, y_cor)
        # time.sleep(0.7)
        screen.ontimer(t.goto, 5000)
        t.write(state_name, move=True, align='center', font=('Arial', 9, "normal"))
        # screen.update()

        states.remove(state_name)
        print(state_name)
        print("state list:", states)

    if not states:
        game_on = False
        print('State list os now empty')

turtle.mainloop()
# s.exitonclick()