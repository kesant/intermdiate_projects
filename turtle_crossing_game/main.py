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
while game_is_on:
    time.sleep(0.1)
    screen.update()
