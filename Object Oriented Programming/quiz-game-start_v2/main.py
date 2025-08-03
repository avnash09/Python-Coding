from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import os, html

os.system('cls')

question_bank = []
for question in question_data:
    decoded_question = html.unescape(question["question"])
    answer = question["correct_answer"]
    question_bank.append(Question(q_text=decoded_question, q_answer=answer))

# question_bank = [Question(html.unescape(question["question"]), question["correct_answer"]) for question in question_data]
quiz = QuizBrain(question_bank)

for q_dict in question_data:
    for key, value in q_dict.items():
        print(q_dict[key])

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz!")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")