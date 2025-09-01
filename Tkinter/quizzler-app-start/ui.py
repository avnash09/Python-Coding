from tkinter import *
from tkinter import messagebox
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
dir_path = './Tkinter/quizzler-app-start/'

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(width=600, height=500, bg=THEME_COLOR, padx=20, pady=20)
        
        self.canvas = Canvas(self.window, width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text(150, 125, width=280, text='', font=('Arial', 20, 'italic'))
        self.canvas.grid(row=2, column=1, columnspan=2, pady=50)

        self.score_label = Label(self.window, text='Score: 0', bg=THEME_COLOR, highlightthickness=0, fg='white')
        self.score_label.grid(row=1, column=2, padx=10, pady=10)

        true_img = PhotoImage(file=dir_path+'images/true.png')
        false_img = PhotoImage(file=dir_path+'images/false.png')

        self.true_button = Button(self.window, image=true_img, command=self.true_check)
        self.true_button.grid(row=3, column=1, padx=10, pady=10)

        self.false_button = Button(self.window, image=false_img, command=self.false_check)
        self.false_button.grid(row=3, column=2, padx=10, pady=10)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="Game ends.")
            self.true_button.config(state='disabled')
            self.false_check.config(state='disabled')

    def true_check(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_check(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)