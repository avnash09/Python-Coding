import os,tkinter

def clear_terminal():
    if os.name == 'nt': os.system('cls')
    else: os.system('clear')
clear_terminal()

window = tkinter.Tk()
window.title("First GUI Program")
window.minsize(width=500, height=300)

label = tkinter.Label(text="I am a Label", font=("Arial", 18, "bold"))
# label.pack(expand=False)
label.grid(column=0, row=0)

#updating the Label on the screen
# label['text'] = "New Text"
# label.config(text="another new text")

def button_clicked():
    print('I got clicked!')
    # label['text'] = 'Button got clicked'
    # label.config(text='Button got clicked')
    user_input = input.get()
    label.config(text=user_input)

button1 = tkinter.Button(text='Click me', command=button_clicked, font=("Arial", 12, "normal"))
# button.pack()
button1.grid(column=2, row=1)

button2 = tkinter.Button(text="New click", command=button_clicked)
button2.grid(column=3, row=0)

input = tkinter.Entry(width=10)
input.insert(tkinter.END, "some text.")
input.grid(column=4, row=3)
# input.pack()
input.grid(column=4, row=4)

#Text Box
textbox = tkinter.Text(width=30, height=5)
textbox.insert(tkinter.END, "Enter new text here.")
textbox.focus()
# textbox.pack()

#Spin box
def spinbox_action():
    print(spin.get())
spin = tkinter.Spinbox(from_=0, to=10, width=5, command=spinbox_action)
# spin.pack()

#Checkbox
def show_state():
    print(choice.get())
choice = tkinter.IntVar()
checkbutton = tkinter.Checkbutton(text="I agree", variable=choice, command=show_state)
choice.get()
# checkbutton.pack()

#Radio Buttons
def radio_state():
    print(radio_choice.get())

radio_choice = tkinter.IntVar()
radio1 = tkinter.Radiobutton(text="Option 1", variable=radio_choice, value=1, command=radio_state)
radio2 = tkinter.Radiobutton(text="Option 2", variable=radio_choice, value=2, command=radio_state)
# radio1.pack()
# radio2.pack()

#List Box
def listbox_used(event):
    print(listbox.get(listbox.curselection()))

listbox = tkinter.Listbox(height=4)
fruits = ['Apple','Banana','Peach','Orange']
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
# listbox.pack()

window.mainloop() 