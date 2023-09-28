from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(800, 700)
colors = ["red", "blue", "orange", "yellow", "purple", "green"]

turtles = []

for index, color in enumerate(colors):
    tim = Turtle()
    tim.shape("turtle")
    tim.penup()
    tim.color(colors[index])
    tim.goto(-350 , (-100 + (30 * index)))
    turtles.append(tim)

user_guess = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color:")

race_started = True

while race_started:
    for turtle in turtles:
        turtle.forward(random.randint(0, 10))
        if turtle.xcor() > 320:
            race_started = False
            winner = turtle.pencolor()
            if user_guess == winner:
                print(f"You've won! The winner is: {winner}")
            else:
                print(f"You've lost. The winner was: {winner}")



screen.exitonclick()