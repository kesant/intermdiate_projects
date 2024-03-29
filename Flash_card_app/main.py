import tkinter
from tkinter import Canvas
from tkinter import PhotoImage
from tkinter import *

import pandas
import  pandas as pd
import random
#CONSTANTS

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT=("Ariel",40,"italic")
WORD_FONT=("Ariel",60,"bold")

#VARIBLES
title="title"
word="word"
palabras_traduccion=""


#READ THE FILES
try:
    data = pd.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("./data/french_words.csv")
finally:
    data_dict = data.to_dict(orient="records")  # records turn the dict into a list of dictionaries



#*********************FUNTIONS **********************
def general_button():
    """select a random letter in french and  set it in the canvas varible"""
    global palabras_traduccion,flipped_card
    window.after_cancel(flipped_card)
    palabras_traduccion=random.choice(data_dict)
    title="French"
    word=palabras_traduccion[title]
    canvas.itemconfig(card_title,text=title,fill="Black")
    canvas.itemconfig(card_word,text=word,fill="Black")
    canvas.itemconfig(font_card,image=front_card)
    flipped_card=window.after(3000,flip_cards)
def right_clicked():
    general_button()
    delete_word()

def flip_cards ():
    """flip the card and shows the translation of the word"""
    canvas.itemconfig(font_card,image=back_card)
    word_english=palabras_traduccion["English"]
    canvas.itemconfig(card_title,text="English",fill="White")
    canvas.itemconfig(card_word,text=word_english,fill="White")

def delete_word():
    """it will delete the word from the list when the user press the check button"""
    data_dict.remove(palabras_traduccion)
    new_dataframe=pd.DataFrame(data_dict)
    new_dataframe.to_csv("./data/words_to_learn.csv",index=False)
    print(data_dict)


#*****************************FILES******************

#**********************GUI********************************************
window=tkinter.Tk()
window.title("Flash card app")
window.config(padx=50,pady=50,bg="#B1DDC6")
flipped_card=window.after(3000,flip_cards)

#IMAGES
#it is necesary make a photoimage to use the create_image
front_card=PhotoImage(file="./images/card_front.png")
back_card=PhotoImage(file="./images/card_back.png")
right_image=PhotoImage(file="./images/right.png")
wrong_image=PhotoImage(file="./images/wrong.png")

#BUTTONS
right_button = Button(image=right_image, highlightthickness=0,command=right_clicked)
right_button.grid(column=0,row=1)
wrong_button = Button(image=wrong_image, highlightthickness=0, command=general_button)
wrong_button.grid(column=1,row=1)

print(word)
print(title)

#CANVAS
canvas=Canvas(width=800,height=526,bg= BACKGROUND_COLOR,highlightthickness=0)#the atribute bg is for the background
#highlightthickness is a atribute for the border of the canvas
font_card=canvas.create_image(0,0,image=front_card,anchor='nw')
card_title=canvas.create_text(400,150,text=title,fill="Black",font=LANGUAGE_FONT)
card_word=canvas.create_text(400,263,text=word,fill="Black",font=WORD_FONT)
canvas.grid(column=0,row=0,columnspan=2)
general_button()



window.mainloop()
