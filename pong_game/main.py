from turtle import Screen
from paddle import  Paddle
from ball import Ball

import  time

screen=Screen()
screen.bgcolor("black")
screen.setup(height=600,width=800)
screen.title("Pong")
screen.tracer(0)
game_is_on=True

padle=Paddle(350,0)
padle2=Paddle(-350,0)

ball=Ball()

screen.listen()

screen.onkey(fun=padle.up,key="Up")
screen.onkey(fun=padle.down,key="Down")
screen.onkey(fun=padle2.up,key="w")
screen.onkey(fun=padle2.down,key="s")

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

screen.exitonclick()


