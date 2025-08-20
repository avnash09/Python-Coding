from tkinter import *
import os, pandas as pd, random, json
BACKGROUND_COLOR = "#B1DDC6"

def clear_terminal():
    if os.name == 'nt': os.system('cls')
    else: os.system('clear')
clear_terminal()

image_path = './Tkinter/flash-card-project-start/images/'
data_path = './Tkinter/flash-card-project-start/data/'
to_learn = {}
current_card = {}

#read the csv file
try:
    data = pd.read_csv(data_path+'words_to_learn.csv')
except (FileNotFoundError, pd.errors.EmptyDataError):
    original_data = pd.read_csv(data_path+'french_words.csv')
    to_learn = original_data.to_dict(orient='records')
else:
    to_learn = data.to_dict(orient='records')

#generate a random word
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    current_language = 'French'
    current_word = current_card[current_language]
    canvas.itemconfig(title_text, text=current_language, fill='black')
    canvas.itemconfig(word_text, text=current_word, fill='black')
    canvas.itemconfig(canvas_img, image=card_front_img)
    flip_timer = window.after(3000, func=flip_cards)
    
#flip the cards
def flip_cards():
    flip_language = 'English'
    flip_word = current_card[flip_language]
    canvas.itemconfig(canvas_img, image=card_back_img)
    canvas.itemconfig(title_text, text=flip_language,fill='white')
    canvas.itemconfig(word_text, text=flip_word,fill='white')

def words_to_learn():
    to_learn.remove(current_card)
    print(len(to_learn))
    df = pd.DataFrame(to_learn)
    df.to_csv(data_path+'words_to_learn.csv', index=False)
    next_card()

#create a window
window = Tk()
window.title("Flashy")
#set background color
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(3000, func=flip_cards)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file=image_path+'card_front.png')
card_back_img = PhotoImage(file=image_path+'card_back.png')
canvas_img = canvas.create_image(400, 263, image=card_front_img)
title_text = canvas.create_text(400, 150, text='title', font=('Ariel', 40, 'italic'))
word_text = canvas.create_text(400, 263, text='Word', font=('Ariel', 60, 'bold'))
canvas.grid(row=0, column=0, columnspan=2)

wrong_img = PhotoImage(file=image_path+'wrong.png')
wrong_button = Button(image=wrong_img, bg=BACKGROUND_COLOR, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

right_img = PhotoImage(file=image_path+'right.png')
right_button = Button(image=right_img, bg=BACKGROUND_COLOR, highlightthickness=0, command=words_to_learn)
right_button.grid(row=1, column=1)

next_card()


window.mainloop()

