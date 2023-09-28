from turtle import Turtle
class Ball:
    def __init__(self):
        self.ball = Turtle()
        self.ball.shape("circle")
        self.ball.color("white")
        self.ball.penup()
        self.x_speed = 10
        self.y_speed = 10
        
    def move(self):
        new_x = self.ball.xcor() + self.x_speed
        new_y = self.ball.ycor() + self.y_speed
        self.ball.goto(new_x, new_y)

    def bounce_y(self):
        self.y_speed = -self.y_speed

    def bounce_x(self):
        self.x_speed = -self.x_speed

    def reset(self):
        self.ball.setposition(0,0)