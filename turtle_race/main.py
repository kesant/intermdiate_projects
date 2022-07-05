2222# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from turtle import Turtle, Screen



screen=Screen()
screen.setup(width=500,height=400)#we are defining the size of the screen
user=screen.textinput(title="turtle race",prompt="wich turtle will win the race ? choose a color ")
colors=["red","blue","yellow","orange","purple","green"]
y_position=[-78,-50,-30,-10,20,40]
for indice in range (0,6):
    tim=Turtle(shape="turtle")
    tim.color(colors[indice])
    tim.penup()
    tim.goto(x=-230,y=y_position[indice])

screen.exitonclick()

# Press the green button in the gutter to run the script.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
