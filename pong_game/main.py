from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import  Scoreboard
import time

screen=Screen()
screen.bgcolor("black")
screen.setup(height=600,width=800)
screen.title("Pong")
screen.tracer(0)
game_is_on=True

score=Scoreboard()

padle_r=Paddle(350,0)
padle_l=Paddle(-350,0)

ball=Ball()

screen.listen()

screen.onkey(fun=padle_r.up,key="Up")
screen.onkey(fun=padle_r.down,key="Down")
screen.onkey(fun=padle_l.up,key="w")
screen.onkey(fun=padle_l.down,key="s")

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    #detect the colission with the wall
    if ball.ycor()>285 or ball.ycor()<-285:
        ball.bounce_y()
    #detect the collision with the paddel
    if ball.distance(padle_r)<50and ball.xcor()>320 or ball.distance(padle_l)<50and ball.xcor()<-320:
        ball.bounce_x()
    #detect if right paddle miss the ball
    if ball.xcor()>380:
        ball.restart()
        score.l_point()
    elif ball.xcor()<-380:
        ball.restart()
        score.r_point()
screen.exitonclick()


