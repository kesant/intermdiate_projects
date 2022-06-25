# This is a sample Python script.
import turtle as t
import random
# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


#draw a dashed line
# for i in range (50):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()
####draw shapes
# def draw_shapes(num_sides):
#     angle = 360 / num_sides
#     for i in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
#
# for size in range(3,11):
#     tim.color('dark blue')
#     draw_shapes(size)
#####Draw a random walk

#####making a spinogharp
tim=t.Turtle()
t.colormode(255)#especifica el rango del color
def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    color=(r,g,b)
    return  color

tim.speed("fastest")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
def draw_spirograph(size_of_gap):
    for i in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading()+size_of_gap)
draw_spirograph(5)
screen=t.Screen()#shows a screen
screen.exitonclick()