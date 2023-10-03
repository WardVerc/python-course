from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=50)
        self.question_text = self.canvas.create_text(150, 120, text="Question text comes here okay yes its here ok", width=250, font=("Arial", 20, "italic"), fill="black")
        self.score = Label(text="Score: 0", font=("Arial", 14), fg="white", bg=THEME_COLOR)
        self.score.grid(column=1, row=0)
        self.correct_img = PhotoImage(file="images/true.png")
        self.correct_button = Button(image=self.correct_img, highlightthickness=0, command=self.answer_true)
        self.correct_button.grid(row=2, column=0)
        self.false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.false_img, highlightthickness=0, command=self.answer_false)
        self.false_button.grid(row=2, column=1)

        self.next_question()

        self.window.mainloop()

    def answer(s):
        print("True")

    def next_question(self):
        self.canvas.config(bg="white")
        self.score.config(text=f"Score: {self.quiz.score}")

        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="End of quiz.")
            self.correct_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def answer_true(self):
        is_right = self.quiz.check_answer("true")
        self.give_feedback(is_right)

    def answer_false(self):
        is_right = self.quiz.check_answer("false")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.next_question)