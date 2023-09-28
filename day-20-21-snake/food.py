import random
from turtle import Turtle

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.75, 0.75)
        self.color("green")
        self.speed("fastest")
        self.refresh()
        

    def refresh(self):
        # 800 width (-400, 400) and 800 height, snakebody is 20 -> 380
        random_x = random.randint(-380, 380)
        random_y = random.randint(-380, 380)
        self.goto(random_x, random_y)