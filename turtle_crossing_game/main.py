import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
#we create the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)#we turn off the tracer

game_is_on = True
player=Player()
cars=CarManager()
screen.listen()#we set that our screen listen to events
screen.onkey(player.go_up,"Up")
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_cars()
    cars.move_car()
    #detect the collision of the turtle  with the car
    for car in cars.all_cars:
        if car.distance(player)<20:
            game_is_on=False
screen.exitonclick()