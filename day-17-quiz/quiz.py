from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    # the questions in question_data are Dictionaries!
    quest = Question(question['text'], question['answer'])
    question_bank.append(quest)

# Here the questions are Question-objects!
print(question_bank[0].text)

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions():
    quiz_brain.next_question()

print("Quiz completed!")
print(f"You score was: {quiz_brain.score}/{len(question_bank)}")