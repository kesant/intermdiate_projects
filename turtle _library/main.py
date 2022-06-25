# This is a sample Python script.
from turtle import Turtle,Screen
# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
tim=Turtle()


#draw a dashed line
# for i in range (50):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()
####draw shapes
def draw_shapes(num_sides):
    angle = 360 / num_sides
    for i in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for size in range(3,11):
    tim.color('dark blue')
    draw_shapes(size)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
screen=Screen()#shows a screen
screen.exitonclick()