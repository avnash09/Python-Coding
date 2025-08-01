class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        # print(self.question_list[self.question_number])
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)?:  ")
        self.check_answer(user_answer, correct_answer=current_question.answer)
            

    def check_answer(self, user_answer, correct_answer):
        if user_answer[0].lower() == correct_answer[0].lower():
            print(f"You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was {correct_answer}")
        print(f"Your currect score is: {self.score}/{self.question_number}")
        print("\n\n")