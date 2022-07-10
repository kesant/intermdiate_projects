2222# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from turtle import Turtle, Screen
import random

is_race_on=False
screen=Screen()
screen.setup(width=500,height=400)#we are defining the size of the screen
user=screen.textinput(title="turtle race",prompt="wich turtle will win the race ? choose a color ")
colors=["red","blue","yellow","orange","purple","green"]
y_position=[-78,-50,-30,-10,20,40]
all_turtles=[]
for indice in range (0,6):
    new_turtle=Turtle(shape="turtle")
    new_turtle.color(colors[indice])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[indice])
    all_turtles.append(new_turtle)
if user:
    is_race_on=True

while is_race_on:
    for turtle in all_turtles:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
        if turtle.xcor()>=230:
            print(f"the {turtle.pencolor()} turtle  is the winner ")
            if turtle.pencolor()==user:
                print("you win")
            else :
                print("you lose")
            is_race_on=False


screen.exitonclick()

# Press the green button in the gutter to run the script.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
