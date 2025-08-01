class QuizBrain:

    def __init__(self, question_list):
        
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def __str__(self):
        return "Questions are ready, Let's play!"

    def still_has_questions(self):
        
        return self.question_number < len(self.question_list)
    
    def next_question(self):
        if self.still_has_questions():
            current_question = self.question_list[self.question_number]
            self.question_number += 1
            user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ")
            self.check_answer(user_answer, current_question.answer)
        
    def check_answer(self, user_answer, correct_answer):
        if user_answer[0].lower() == correct_answer[0].lower():
            self.score += 1
            print('You have got it right.')
        else:
            print("That's wrong")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print('\n')

if __name__ == '__main__':
    
    from main import Question, question_bank

    q = QuizBrain([question_bank[0], question_bank[1]])
    q.next_question()
    q.question_number += 1
    q.next_question()


#print(f"Q.{self.question_number}: {current_question.text} (True/False)?: ")
#print(f"Q.{self.question_number + 1}: {self.question_list[self.question_number]} (True/False)?: ")