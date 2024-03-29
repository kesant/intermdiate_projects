import tkinter
from tkinter import Canvas, END
from tkinter import PhotoImage
from tkinter import  messagebox
import random
import pyperclip
import json
FONT=("Arial",10,"bold")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']



    password_letters = [random.choice(letters)  for _ in range(random.randint(8, 10))]
    password_symbols=[random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers=[random.choice(numbers) for _ in range(random.randint(2, 4))]
    password_list=password_letters+password_numbers+password_symbols
    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))
    #
    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)
    #
    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)

    random.shuffle(password_list)

    # password = ""
    # for char in password_list:
    #   password += char
    # the join method combine all the characters from my collection, it can work  with tuples , dictionaries and list
    password="".join(password_list)
    pyperclip.copy(password)#we copying the generated password to clivkboaard
    password_entry.insert(0,password)

# ---------------------------- SEARCH INFO -------------------------------#
def search_info():
    website = website_entry.get().lower()
    with open("important_information.json", mode="r") as file:
        # READ DATA
        data = json.load(file)
        try:
            password=data[website]["Password"]
            email=data[website]["Email"]
        except:
            messagebox.showinfo(title="Error",message="you need to type the name of a website")
        else:
            messagebox.showinfo(title="informaction", message=f"theses are the information: \nWebsite: {website}"
                                                          f"\nEmail: {email} "
                                                          f"\nPassword: {password}\n")
            pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def check_lenght():
    website= website_entry.get()
    email= email_user_entry.get()
    password= password_entry.get()
    if len(website) and len(password) !=0:
        return True
    else:
        return False
def  guardar_informacion():
    website= website_entry.get().lower()
    email= email_user_entry.get().lower()
    password= password_entry.get()
    #with this funtion we can ask the users with a pop up if we want save or not the information
    #the result its saved in a boolean in the variable is_ok
    new_data={
        website:{
            "Email" :email,
            "Password" :password
        }
    }

    if check_lenght():
        is_ok = messagebox.askokcancel(title=website, message=f"theses are the details entered: \nEmail: {email}"                                                     
                                                              f"\nPassword: {password} \n is it ok to save?")
        if is_ok:
            try:
                # with open("important_information.json", mode="r") as file: #we are using the w parameter to write in the json file
                #     # changing the mode to a its that we are going to add new information to the file
                #     #READ DATA
                #     data=json.load(file)
                #     #UPDATE DATA
                #     data.update(new_data)
                file=open("important_information.json", mode="r")
            except FileNotFoundError:
                with open("important_information.json", mode="w") as file:
                    #we use the dump funtion to write in the json file , givin asa an argument the dictionary and the file we want to open
                    #WRITE DATA
                    json.dump(new_data,file,indent=4)#the argument indent gives us the number of spaces we want to indent the information
                    website_entry.delete(0, END)#with the funtion delete we will be deleting the information in the charts after
                    #clicking add button
                    password_entry.delete(0, END)
            else :
                file.close()
                with open("important_information.json", mode="r") as file: #we are using the w parameter to write in the json file
                    # changing the mode to a its that we are going to add new information to the file
                    #READ DATA
                    data=json.load(file)
                    #UPDATE DATA
                    data.update(new_data)
                with open("important_information.json", mode="w") as file:
                    #we use the dump funtion to write in the json file , givin asa an argument the dictionary and the file we want to open
                    #WRITE DATA
                    json.dump(data,file,indent=4)#the argument indent gives us the number of spaces we want to indent the information
                    website_entry.delete(0, END)#with the funtion delete we will be deleting the information in the charts after
                    #clicking add button
                    password_entry.delete(0, END)

    else:
        messagebox.showinfo(title="Error",message="Please don't leave any field empty!!")

# ---------------------------- UI SETUP ------------------------------- #
if __name__=="__main__":
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
    #email_user_entry.insert(0,"here you put your email")#insert text at a given index is like when you put a default value
    #the is an alternative as an argument for the funtion insert , if we use .inset(END) it can be a continuation of the  text

    password_entry.grid(row=3,column=1)#adding the pad it can be spaced between elements




    #BUTTONS
    search_button=tkinter.Button(text="Search",width=15,command=search_info)
    search_button.grid(row=1,column=3)
    password_button=tkinter.Button(text="Generate Password",command=generate_password)
    password_button.grid(row=3,column=3)
    add_button=tkinter.Button(text="Add",width=30,command=guardar_informacion)
    add_button.grid(row=4,column=1,columnspan=2)



    window.mainloop()
