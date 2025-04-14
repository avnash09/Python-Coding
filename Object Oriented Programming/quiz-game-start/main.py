from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_bank.append(Question(question['text'], question['answer']))
    #print(question['text'])

# for question in question_bank:
#     print(question.text, '\t', question.answer)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():

    quiz.next_question()

print("You've completed the quiz.")
print(f"your final score was: {quiz.score}/{len(question_bank)}")