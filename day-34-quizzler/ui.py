from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20)
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)
        self.question_text = self.canvas.create_text(150, 120, text="Question text comes here okay yes its here ok", width=250, font=("Arial", 20, "italic"), fill="black")
        self.score = Label(text="Score: {self.score}", font=("Arial", 14), fg="white")
        self.score.grid(column=1, row=0)
        self.correct_img = PhotoImage(file="images/true.png")
        self.correct_button = Button(image=self.correct_img, highlightthickness=0, command=self.answer)
        self.correct_button.grid(row=2, column=0)
        self.false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.false_img, highlightthickness=0, command=self.answer)
        self.false_button.grid(row=2, column=1)

        self.window.mainloop()

    def answer(s):
        print("True")

