from turtle import Turtle
UP=90
class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("square")
        self.shapesize(stretch_len=1,stretch_wid=5)
        self.goto(x=350,y=0)

    def move(self):
        self.forward(20)
