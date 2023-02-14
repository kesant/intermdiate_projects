import tkinter
from tkinter import Canvas, END
from tkinter import PhotoImage

FONT=("Arial",10,"bold")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def  guardar_informacion():
    website= website_entry.get()
    email= email_user_entry.get()
    password= password_entry.get()
    with open("important_information.txt", mode="a") as file:
        # changing the mode to a its that we are going to add new information
        # to the file
        file.write(f"\n {website}|{email}|{password}")
        website_entry.delete(0, END)
        password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window= tkinter.Tk()

window.title("Password Manager ")#seteamos el titulo de nuestro recuadro
window.minsize(width=500,height=300)
window.config(padx=40,pady=40)
#canvas
canvas=Canvas(width=200,height=200,highlightthickness=1)#the atribute bg is for the background
#highlightthickness is a atribute for the border of the canvas
#it is necesary make a photoimage to use the create_image
tomato_img=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=tomato_img)#here we define the x and y position defined on the canvas
canvas.grid(row=0,column=1)

#LABELS
website_label=tkinter.Label(text="Website : ",font=FONT)
email_user_label=tkinter.Label(text="Email/Username : ",font=FONT)
password_label=tkinter.Label(text="Password : ",font=FONT)
website_label.grid(row=1,column=0)
email_user_label.grid(row=2,column=0)
password_label.grid(row=3,column=0)

#ENTRIES
website_entry=tkinter.Entry(width=35)
email_user_entry=tkinter.Entry(width=35)
password_entry=tkinter.Entry(width=19)
#the columnspan attribute indicates how many columns it want the element go across
website_entry.grid(row=1,column=1,columnspan=2)
website_entry.focus()
email_user_entry.grid(row=2,column=1,columnspan=2)
email_user_entry.insert(0,"kejosant@espol.edu.ec")#insert text at a given index is like when you put a default value
#the is an alternative as an argument for the funtion insert , if we use .inset(END) it can be a continuation of the  text

password_entry.grid(row=3,column=1)#adding the pad it can be spaced between elements




#BUTTONS
password_button=tkinter.Button(text="Generate Password")
password_button.grid(row=3,column=2)
add_button=tkinter.Button(text="Add",width=36,command=guardar_informacion)
add_button.grid(row=4,column=1,columnspan=2)



window.mainloop()
