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

game_on = False

df = pd.read_csv(work_dir + 'indian_states_coordinates.csv')
# print(df.sample(10))
state_name = 'Assam' #df.state[0]

# Try to force focus back to the screen
screen.update()
time.sleep(0.1)  # Small delay to allow focus shift

user_input = screen.textinput("Guess the state", prompt="What's another state name?").title()

if user_input == state_name:
    state_data = df[df.state == state_name]
    print(state_data, state_data.x.item())
    x_cor = state_data.x.item()
    y_cor = state_data.y.item()
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.goto(x_cor, y_cor)
    t.write(state_name)

turtle.mainloop() 