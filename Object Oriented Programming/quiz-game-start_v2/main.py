from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import os

os.system('cls')

# for q_dict in question_data:
#     for key, value in q_dict.items():
#         print(q_dict[key])

question_bank = [Question(question["text"], question["answer"]) for question in question_data]
quiz = QuizBrain(question_bank)

# quiz.next_question()
# print(quiz.still_has_questions())

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz!")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")