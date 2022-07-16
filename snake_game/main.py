from turtle import  Screen
import  time
from food import  Food
from snake import  Snake
from scoreboard import  Scoreboard
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")#we set the background color of the screen
screen.title("My snake game")#we set the title of the screen
screen.tracer(0)#puting 0 inside the tracer methods we turn off the animation

snake=Snake()
food=Food()#creamos la comida
board=Scoreboard()#i create the scoreboard
screen.listen()
screen.onkey(fun=snake.up , key="Up")
screen.onkey(fun=snake.down,key="Down")
screen.onkey(fun=snake.left,key="Left")
screen.onkey(fun=snake.right,key="Right")
game_is_on=True
while game_is_on:
    screen.update()  # update the animation and turn it on
    time.sleep(0.1)#it makes the time goes slower stop the time 0.1 seconds
    snake.move()
    #detect the collision with the food
    if snake.segments[0].distance(food)<15:#we use the distance method to measure the distance of the head of the snake with the food
        food.refres()
        board.increase_score()
        snake.increase_snake()
    #detect collision with the wall
    if snake.segments[0].xcor()>280 or snake.segments[0].ycor()>280 or snake.segments[0].xcor()<-280 or snake.segments[0].ycor()<-280:
        board.game_over()
        game_is_on=False
    #detect collision with the tail
    for position in range(2,len(snake.segments)):
        if snake.segments[0].distance(snake.segments[position])<15:#we detect the distance between the head and the tail
            board.game_over()
            game_is_on=False

screen.exitonclick()