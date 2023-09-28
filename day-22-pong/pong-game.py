from turtle import Screen
from paddle import Paddle
import time
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pongo pong")
screen.tracer(0)

paddle_left = Paddle()
paddle_right = Paddle((360, 0))
ball = Ball()
score_left = Scoreboard((-200, 260))
score_right = Scoreboard((200, 260))

screen.listen()
screen.onkey(paddle_left.up, "w")
screen.onkey(paddle_left.down, "s")
screen.onkey(paddle_right.up, "Up")
screen.onkey(paddle_right.down, "Down")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.05)
    ball.move()

    if ball.ball.ycor() > 280 or ball.ball.ycor() < - 280:
        ball.bounce_y()

    if ball.ball.distance(paddle_right.paddle) < 50 or ball.ball.distance(paddle_left.paddle) < 50:
        if ball.ball.xcor() > 330 or ball.ball.xcor() < -340:
            ball.bounce_x()

    if ball.ball.xcor() > 380:
        score_left.add()
        score_left.update_scoreboard()
        ball.reset()
        ball.bounce_x()

    if ball.ball.xcor() < -380:
        score_right.add()
        score_right.update_scoreboard()
        ball.reset()
        ball.bounce_x()

screen.exitonclick()