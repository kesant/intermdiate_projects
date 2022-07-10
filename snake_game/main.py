from turtle import  Turtle,Screen
import  time
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")#we set the background color of the screen
screen.title("My snake game")#we set the title of the screen
starting_position=[(0,0),(-20,0),(-40,0)]
segments=[]
screen.tracer(0)#puting 0 inside the tracer methods we turn off the animation
for i in range(3):
    snake=Turtle(shape="square")
    snake.color("white")
    snake.penup()
    snake.goto(starting_position[i])
    segments.append(snake)

game_is_on=True
while game_is_on:
    screen.update()  # update the animation and turn it on
    time.sleep(0.1)#it makes the time goes slower
    for segme_num in range(len(segments)-1,0,-1):#it makes to change the position 3 to 2 and 2 to 1 and so
        new_x=segments[segme_num-1].xcor()
        new_y= segments[segme_num-1].ycor()
        segments[segme_num].goto(new_x,new_y)
    segments[0].forward(20)




screen.exitonclick()