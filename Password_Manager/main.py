import tkinter
from tkinter import  Canvas
from tkinter import PhotoImage

FONT=("Arial",15,"bold")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window= tkinter.Tk()

window.title("Password Manager ")#seteamos el titulo de nuestro recuadro
window.minsize(width=500,height=300)
window.config(padx=20,pady=20)
#canvas
canvas=Canvas(width=200,height=200,highlightthickness=1)#the atribute bg is for the background
#highlightthickness is a atribute for the border of the canvas
#it is necesary make a photoimage to use the create_image
tomato_img=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=tomato_img)#here we define the x and y position defined on the canvas
canvas.grid(row=0,column=1)

#LABELS
website_label=tkinter.Label(text="Website",font=FONT)
email_user_label=tkinter.Label(text="Email/Username",font=FONT)
password_label=tkinter.Label(text="Password",font=FONT)
website_label.grid(row=1,column=0)
email_user_label.grid(row=2,column=0)
password_label.grid(row=3,column=0)

#ENTRIES
website_entry=tkinter.Entry(width=35)
email_user_entry=tkinter.Entry(width=35)
password_entry=tkinter.Entry(width=21)
website_entry.grid(row=1,column=1,columnspan=2)
email_user_entry.grid(row=2,column=1,columnspan=2)
password_entry.grid(row=3,column=1)

#BUTTONS


window.mainloop()
