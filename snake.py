
from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_STEP = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self) -> None:
        '''CREATING THE SNAKE BODY'''
        self.all_snake_parts = []
        self.create_snake()
        self.head = self.all_snake_parts[0]

    def create_snake(self):
        '''For creating new snake segments and appending them to a list(all_snake_parts).'''
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_snake_part = Turtle(shape="square")
        new_snake_part.color("white")
        new_snake_part.penup()
        new_snake_part.goto(position)
        self.all_snake_parts.append(new_snake_part)

    def extend_snake(self):
        self.add_segment(self.all_snake_parts[-1].position())

    def move(self):
        for part_number in range(len(self.all_snake_parts)-1, 0, -1):
            # The 3rd part goes to 2nd part's position and 2nd goes to 1st and the first moves in the direction.
            new_x = self.all_snake_parts[part_number-1].xcor()
            new_y = self.all_snake_parts[part_number-1].ycor()
            self.all_snake_parts[part_number].goto(new_x, new_y)
        self.head.forward(MOVE_STEP)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
