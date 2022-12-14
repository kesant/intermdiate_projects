#creamos la clase estado
from turtle import Turtle
FONT = ("Courier", 12, "normal")

class State(Turtle):
    def __init__(self,posicion_x,posicion_y,nombre):
        super(State, self).__init__()
        self.hideturtle()
        self.penup()
        self.posx=posicion_x
        self.posy=posicion_y
        self.nombre=nombre
        self.ubicacion()
    def ubicacion(self):
        self.goto(self.posx,self.posy)
        self.write(f"{self.nombre.title()}", align="center", font=FONT)
