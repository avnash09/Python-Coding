import os, turtle, pandas as pd, time

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
df = pd.read_csv(work_dir + 'indian_states_coordinates.csv')
state_list = df.state.to_list()
print(state_list)
guessed_states = []
missed_states = []
border_states = ['Goa', 'Mizoram', 'Tripura', 'Kerala', 'Sikkim', 'Manipur', 'Meghalaya', 'Nagaland', 'Arunachal Pradesh', "Jammu and Kashmir", "Ladakh"]

game_on = True

while len(guessed_states) < len(state_list):

    # Try to force focus back to the screen
    screen.update()
    time.sleep(0.1)  # Small delay to allow focus shift
    
    if not guessed_states:
        user_input_state = screen.textinput(f"Guess the state", prompt="What's another state name?").title()
    else:
        user_input_state = screen.textinput(f"{len(guessed_states)}/{len(state_list)} correct answers", prompt="What's another state name?").title()

    # user_input_state = user_input_state.replace('And','and')
    if user_input_state.split()[0] == "Jammu" and user_input_state.split()[2] == "Kashmir":
        user_input_state = "Jammu and Kashmir"

    if user_input_state == 'Exit':
        game_on = False
        missed_states = [state for state in state_list if state not in guessed_states]
        missed_states_dict = {'state': missed_states}
        missed_states_df = pd.DataFrame(missed_states_dict)
        missed_states_df.to_csv(work_dir + 'states_to_learn.csv')
        break

    elif user_input_state in state_list:
        state_data = df[df.state == user_input_state]
        print(state_data)
        guessed_states.append(user_input_state)
        x_cor = state_data.x.item()
        y_cor = state_data.y.item()
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(x_cor, y_cor)
        t.color('red')
        alignment = 'center'
        if user_input_state in border_states:
            t.dot(5)
            t.pendown()
            if user_input_state in ['Goa', 'Kerala', "Jammu and Kashmir"]:
                t.goto(x_cor - 30, y_cor - 30)
                alignment = 'right'
            elif user_input_state in ['Meghalaya', 'Tripura']:
                t.goto(x_cor - 10, y_cor - 30)
                alignment = 'right'
            elif user_input_state in ['Sikkim', 'Arunachal Pradesh', "Ladakh"]:
                t.goto(x_cor + 10, y_cor + 30)
                alignment = 'left'
            else:
                t.goto(x_cor + 30, y_cor - 30)
                alignment = 'left'
        t.write(user_input_state.replace(' ','\n'), move=False, align=alignment, font=('Times New Roman', 8, 'bold'))

if len(guessed_states) == len(state_list):
    print('Congratulations! You have guessed all states correctly!')

turtle.mainloop() 