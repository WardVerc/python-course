from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(800, 800)
screen.bgcolor("black")
screen.title("Snake")
# turn off tracer so we can control the update func of the screen
screen.tracer(0)

snek = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snek.up, "Up")
screen.onkey(snek.down, "Down")
screen.onkey(snek.left, "Left")
screen.onkey(snek.right, "Right")

game_on = True

while game_on:
    screen.update()
    time.sleep(0.05)
    snek.move()
    

    if snek.head.distance(food) < 20:
        score.add()
        snek.extend()
        food.refresh()

    # this is slicing in Python [1:] -> starting from index 1 til the end
    for part in snek.snek_bod[1:]:
    #for part in snek.snek_bod:
        if snek.head.distance(part) < 10:
    #    if part != snek.head and snek.head.distance(part) < 10:
            score.reset()
            snek.reset()

    if snek.head.xcor() > 380:
        snek.head.setx(-400)
    elif snek.head.xcor() < -380:
        snek.head.setx(400)
    elif snek.head.ycor() > 380:
        snek.head.sety(-400)
    elif snek.head.ycor() < -380:
        snek.head.sety(400)
    

screen.exitonclick()