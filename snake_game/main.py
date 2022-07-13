from turtle import  Screen
import  time
from food import  Food
from snake import  Snake
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")#we set the background color of the screen
screen.title("My snake game")#we set the title of the screen
screen.tracer(0)#puting 0 inside the tracer methods we turn off the animation

snake=Snake()
food=Food()#creamos la comida
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


screen.exitonclick()