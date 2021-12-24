import time
from turtle import Screen, Turtle
screen = Screen()
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTACE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:

    def __init__(self):
        self.squares = []
        self.create_snake()
        self.head = self.squares [0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        square = Turtle(shape="square")
        square.color("white")
        square.penup()
        square.goto(position)
        self.squares.append(square)

    def reset(self):
        for seg in self.squares:
            seg.goto(1000,1000)
        self.squares.clear()
#        self.create_snake()
#        self.head = self.squares[0]

    def extend(self):
        self.add_segment(self.squares[-1].position())

    def snake_move(self):
        screen.update()
        time.sleep(0.1)
        for current_square in range(len(self.squares) - 1, 0, -1): #keep in mind range excludes position 0
            new_x = self.squares[current_square - 1].xcor()
            new_y = self.squares[current_square - 1].ycor()
            self.squares[current_square].goto(new_x, new_y)
        self.squares[0].forward(MOVE_DISTACE)


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)


    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)


    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
