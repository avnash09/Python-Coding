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

# def get_mouse_click_coor(x, y):
#     print(x, y)
# # turtle.onscreenclick(get_mouse_click_coor)

#Get data from the csv file
data = pd.read_csv(csv_filepath)
all_states = data.state.to_list()
correct_answers = []

game_on = True
while game_on:
    
    # Try to force focus back to the screen
    screen.update()
    time.sleep(0.1)  # Small delay to allow focus shift

    if not correct_answers:
        user_answer = screen.textinput(title="Guess the State", prompt="What's another state's name?")
    else:
        user_answer = screen.textinput(title=f"{len(correct_answers)}/50 correct answers", prompt="What's another state's name?")

    if user_answer.lower() == 'exit':
        game_on = False
        #create a csv file with all the missing states
        missing_states = pd.DataFrame(all_states, columns=['State'])
        missing_states.to_csv(work_dir + "states_to_learn.csv")
        break

    state_name = user_answer.title()

    if state_name in all_states:
        
        correct_answers.append(state_name)
        state_data = data[data.state == state_name]

        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        # x_cor, y_cor = data.loc[data.state == state_name, ['x', 'y']].iloc[0]
        #item() gets the scalar or the actual data from the pandas.series output
        x_cor = state_data.x.item()
        y_cor = state_data.y.item()
        t.goto(x_cor, y_cor)
        t.write(state_name, move=True, align='center', font=('Arial', 8, "normal"))

        all_states.remove(state_name)

    if not all_states:
        game_on = False
        print('Congratulations! You guessed all the states!')


# turtle.mainloop()
# s.exitonclick()