import tkinter
from tkinter import  Canvas
from tkinter import PhotoImage
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window= tkinter.Tk()

window.title("Password Manager ")#seteamos el titulo de nuestro recuadro
window.minsize(width=500,height=300)
window.config(padx=20,pady=20)
#canvas
canvas=Canvas(width=200,height=200,highlightthickness=0)#the atribute bg is for the background
#highlightthickness is a atribute for the border of the canvas
#it is necesary make a photoimage to use the create_image
tomato_img=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=tomato_img)#here we define the x and y position defined on the canvas
canvas.pack()

window.mainloop()
