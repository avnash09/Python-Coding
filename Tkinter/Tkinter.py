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

#Text Box
textbox = tkinter.Text(width=30, height=5)
textbox.insert(tkinter.END, "Enter new text here.")
textbox.focus()
textbox.pack()

#Spin box
def spinbox_action():
    print(spin.get())
spin = tkinter.Spinbox(from_=0, to=10, width=5, command=spinbox_action)
spin.pack()

#Checkbox
def show_state():
    print(choice.get())
choice = tkinter.IntVar()
checkbutton = tkinter.Checkbutton(text="I agree", variable=choice, command=show_state)
choice.get()
checkbutton.pack()

#Radio Buttons
def radio_state():
    print(radio_choice.get())

radio_choice = tkinter.IntVar()
radio1 = tkinter.Radiobutton(text="Option 1", variable=radio_choice, value=1, command=radio_state)
radio2 = tkinter.Radiobutton(text="Option 2", variable=radio_choice, value=2, command=radio_state)
radio1.pack()
radio2.pack()

#List Box
def listbox_used(event):
    print(listbox.get(listbox.curselection()))

listbox = tkinter.Listbox(height=4)
fruits = ['Apple','Banana','Peach','Orange']
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

window.mainloop() 