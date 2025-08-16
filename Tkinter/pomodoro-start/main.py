from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
NEW_GREEN = '#08CB00'
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00", fill='white', font=(FONT_NAME, 35, 'bold'))
    timer_label.config(text="Timer", font=(FONT_NAME, 35, "bold"), bg=YELLOW, highlightthickness=0, fg=GREEN)
    check_mark.config(bg=YELLOW, highlightthickness=0, fg=NEW_GREEN)
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    work_secs = WORK_MIN * 60
    short_break_secs = SHORT_BREAK_MIN * 60
    long_break_secs = LONG_BREAK_MIN * 60

    global reps
    reps += 1
    if reps % 8 == 0:
        count_down(long_break_secs)
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_secs)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(work_secs)
        timer_label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    print(count)
    mins = math.floor(count / 60)
    secs = count % 60

    if secs < 10:
        secs = f"0{secs}"

    canvas.itemconfig(timer_text, text=f"{mins}:{secs}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count -1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += " ✔ "
            check_mark.config(text=marks, bg=YELLOW, highlightthickness=0, fg=NEW_GREEN)

# ---------------------------- UI SETUP ------------------------------- #

#Create a window
window = Tk()
window.title("Pamodora")
window.config(padx=100, pady=50, bg=YELLOW)

#Create a canvas containing a Tomato image & timer "00:00" on top of the image
#bg: Background color of the tomato imgae
#highlightthickness: Border of the image
#create_image(): Accepts only a tkinter PhotoImage
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='./Tkinter/pomodoro-start/tomato.png')
canvas.create_image(100, 112, image = tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill='white', font=(FONT_NAME, 35, 'bold'))
# canvas.create_text(100, 90, text="Timer")
canvas.grid(column=2, row=2)

#Create a timer label
timer_label = Label(window, text="Timer", font=(FONT_NAME, 35, "bold"), bg=YELLOW, highlightthickness=0, fg=GREEN)
timer_label.grid(column=2, row=1)

#Create Start & Reset Buttons

start_button = Button(window, text="Start", bg='white', command=start_timer)
start_button.grid(column=1, row=3)

reset_button = Button(window, text="End", bg='white', command=reset_timer)
reset_button.grid(column=3, row=3)

#Create check mark as a Label
# check_mark_symbol = " ✔ "
check_mark = Label(window, bg=YELLOW, highlightthickness=0, fg=NEW_GREEN)
check_mark.grid(column=2, row=3)

window.mainloop()