# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from turtle import Turtle,Screen

tim = Turtle()
def position_rigth():
    tim.right(10)
def position_left():
    tim.left(10)

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)
def clean_screen():
    screen.reset()
# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    screen = Screen()
    screen.listen()
    screen.onkey(key="d",fun=position_rigth)
    screen.onkey(key="a", fun=position_left)
    screen.onkey(key="w", fun=move_forward)
    screen.onkey(key="s", fun=move_backward)
    screen.onkey(key="c", fun=clean_screen)
    screen.exitonclick()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
