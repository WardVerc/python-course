from turtle import Turtle

class Paddle:
    def __init__(self, position = (-370, 0)):
        self.paddle = Turtle()
        self.paddle.shape("square")
        self.paddle.color("white")
        self.paddle.penup()
        self.paddle.shapesize(4, 1)
        self.paddle.setposition(position)

    def up(self):
        ypos = self.paddle.ycor()
        self.paddle.sety(ypos + 50.0)

    def down(self):
        ypos = self.paddle.ycor()
        self.paddle.sety(ypos - 50.0)