from turtle import Screen
from paddle import  Paddle
import  time
screen=Screen()
screen.bgcolor("black")
screen.setup(height=600,width=800)
screen.title("Pong")
screen.tracer(0)
game_is_on=True
padle=Paddle()
while game_is_on:
    time.sleep(0.2)
    screen.update()
    padle.move()
screen.exitonclick()


