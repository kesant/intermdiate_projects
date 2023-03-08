import tkinter
from tkinter import Canvas
from tkinter import PhotoImage
from tkinter import *
BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT=("Ariel",40,"italic")
WORD_FONT=("Ariel",60,"bold")

#**********************GUI********************************************
window=tkinter.Tk()

window.title("Flash card app")

#VARIBLES
title="title"
word="word"

#IMAGES
#it is necesary make a photoimage to use the create_image
front_card=PhotoImage(file="./images/card_front.png")
back_card=PhotoImage(file="./images/card_back.png")
right_image=PhotoImage(file="./images/right.png")
wrong_image=PhotoImage(file="./images/wrong.png")

#BUTTONS
right_button = Button(image=right_image, highlightthickness=0)
right_button.grid(column=0,row=1)
wrong_button = Button(image=wrong_image, highlightthickness=0)
wrong_button.grid(column=1,row=1)

#CANVAS
canvas=Canvas(width=800,height=526,bg= BACKGROUND_COLOR,highlightthickness=0)#the atribute bg is for the background
#highlightthickness is a atribute for the border of the canvas
canvas.create_image(0,0,image=front_card,anchor='nw')
canvas.grid(column=0,row=0,columnspan=2)
canvas.create_text(400,150,text="title",fill="Black",font=LANGUAGE_FONT)
canvas.create_text(400,263,text="word",fill="Black",font=WORD_FONT)

#canvas.create_text()

window.config(padx=50,pady=50,bg="#B1DDC6")
window.mainloop()
