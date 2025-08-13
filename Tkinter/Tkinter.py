import os,tkinter

def clear_terminal():
    if os.name == 'nt': os.system('cls')
    else: os.system('clear')
clear_terminal()

window = tkinter.Tk()
window.title("First GUI Program")
window.minsize(width=500, height=300)

label = tkinter.Label(text="I am a Label", font=("Arial", 18, "bold"))
label.pack(expand=False)

#updating the Label on the screen
# label['text'] = "New Text"
# label.config(text="another new text")

def button_clicked():
    print('I got clicked!')
    # label['text'] = 'Button got clicked'
    # label.config(text='Button got clicked')
    user_input = input.get()
    label.config(text=user_input)

button = tkinter.Button(text='Click me', command=button_clicked, font=("Arial", 12, "normal"))
button.pack()

input = tkinter.Entry(width=20)
input.pack()


window.mainloop() 