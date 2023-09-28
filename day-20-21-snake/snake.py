from turtle import Turtle
SPACE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake: 

    def __init__(self):
        self.snek_bod = []
        self.create_snake()
        self.head = self.snek_bod[0]
        
    def extend(self):
        snek_bod_part = Turtle("square")
        snek_bod_part.penup()
        snek_bod_part.color("white")
        # -1 index takes the last element
        snek_bod_part.setposition(self.snek_bod[-1].position())
        self.snek_bod.append(snek_bod_part)

    def create_snake(self):
        for index in range(0, 3):
            snek_bod_part = Turtle("square")
            snek_bod_part.penup()
            snek_bod_part.color("white")
            snek_bod_part.setposition((-SPACE * index), 0)
            self.snek_bod.append(snek_bod_part)
        self.head = self.snek_bod[0]

    def reset(self):
        for part in self.snek_bod:
            part.goto(1000,1000)
        self.snek_bod.clear()
        self.create_snake()
        

    def move(self):
        # for every bod-element in snek_bod, starting from the last element en iterate back to
        # the first element (using a step of -1), so for 3 elements: index 2 -> 1 -> 0 
        for bod_index in range(len(self.snek_bod) -1, 0, -1):
            # get the coord. of the position of the previous element
            # and set it to the current bod element
            # so starting from the tail element, move it to where the second to last element was
            new_x = self.snek_bod[bod_index - 1].xcor()
            new_y = self.snek_bod[bod_index - 1].ycor()
            self.snek_bod[bod_index].setposition(new_x, new_y)
        
        self.head.forward(SPACE)

    def up(self):
        if not self.head.heading() == DOWN:
            self.head.setheading(90)
    def down(self):
        if not self.head.heading() == UP:
            self.head.setheading(270)
    def left(self):
        if not self.head.heading() == RIGHT:
            self.head.setheading(180)
    def right(self):
        if not self.head.heading() == LEFT:
            self.head.setheading(0)