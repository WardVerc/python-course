from turtle import Turtle

class Label(Turtle):
    def __init__(self, label = "label", position = (0, 260)):
        super().__init__()
        self.penup()
        self.goto(position)
        self.hideturtle()
        self.write(f"{label}", align="center", font=("Arial", 10, "normal"))
