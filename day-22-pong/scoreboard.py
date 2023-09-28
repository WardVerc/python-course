from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, position = (0, 260)):
        super().__init__()
        self.score = 0
        self.color("yellow")
        self.penup()
        self.goto(position)
        self.hideturtle()
        self.update_scoreboard()
 
    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align="center", font=("Arial", 36, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align="center", font=("Arial", 46, "normal"))

    def add(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()