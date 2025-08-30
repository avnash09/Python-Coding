from tkinter import *
import requests, os

def clear_terminal():
    if os.name == 'nt': os.system('cls')
    else: os.system('clear')
clear_terminal()

dir_path = './API/kanye-quotes-start/'

def get_quote():
    pass
    #Write your code here.
    kanye_url='https://api.kanye.rest'

    res = requests.get(url=kanye_url)
    res.raise_for_status()
    print(res.json())
    quote_str = res.json()['quote']
    print(quote_str)
    canvas.itemconfig(quote_text, text=quote_str)



window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file=dir_path+"background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file=dir_path+"kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()