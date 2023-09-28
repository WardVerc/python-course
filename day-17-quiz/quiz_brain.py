class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {question.text} (True/False)?\n")
        self.check_answer(answer, question.answer)
        
    def check_answer(self, answer, correct_answer):
        if answer.lower() == correct_answer.lower():
            print("Correct\n")
            self.score += 1
        else:
            print("Not correct baa\n")
        print(f"Correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}\n")