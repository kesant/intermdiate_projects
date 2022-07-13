from turtle import  Turtle
STARTING_POSITION=[(0,0),(-20,0),(-40,0)]#contant
MOVE_DISTANCE=20
UP=90
DOWN=270
RIGHT=0
LEFT=180
class Snake :
    def __init__(self):
        self.segments=[]
        self.create_snake()

    def create_snake(self):
        for i in range(3):
            new_segment = Turtle(shape="square")
            new_segment .color("white")
            new_segment .penup()
            new_segment .goto(STARTING_POSITION[i])
            self.segments.append(new_segment )
    def move(self):
        for segme_num in range(len(self.segments) - 1, 0, -1):  # it makes to change the position 3 to 2 and 2 to 1 and so
            new_x = self.segments[segme_num - 1].xcor()
            new_y = self.segments[segme_num - 1].ycor()
            self.segments[segme_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)
    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(90)
    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(270)
    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(0)
    def left (self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(180)