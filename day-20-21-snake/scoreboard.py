from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = data.read()
        self.color("yellow")
        self.penup()
        self.goto(0, 360)
        self.hideturtle()
        self.update_scoreboard()
 
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Arial", 36, "normal"))

    def reset(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
            with open("data.txt", "w") as data:
                data.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align="center", font=("Arial", 46, "normal"))

    def add(self):
        self.score += 1
        self.update_scoreboard()