from turtle import Turtle
import  random
class Food(Turtle) :#we make the food class being the child class of turtle
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)#we reduce half of the height and width of the circle
        self.color("blue")
        self.speed("fastest")
        self.refres()
    def refres(self):
        random_x=random.randint(-280,280)
        random_y =random.randint(-280, 280)
        self.goto(random_x,random_y)