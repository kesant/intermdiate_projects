from turtle import Turtle
UP=90
class Paddle(Turtle):

    def __init__(self,x_pos,y_pos):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("square")
        self.shapesize(stretch_len=1,stretch_wid=5)
        self.goto(x=x_pos,y=y_pos)

    def up(self):
        new_y=self.ycor()+20
        self.goto(self.xcor(),new_y)
    def down(self):
        new_y=self.ycor()-20
        self.goto(self.xcor(),new_y)