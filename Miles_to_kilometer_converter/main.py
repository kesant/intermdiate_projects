from tkinter import  *
import math
window=Tk()
window.title("Mile to kilomter converter")
window.minsize(width=300,height=200)
window.config(padx=20,pady=50)

#label 1
my_label1=Label(text="Miles",font=("Times New Roman",11,"bold"))
my_label1.grid(column=2,row=0)
#label 2
my_label2=Label(text="Km",font=("Times New Roman",11,"bold"))
my_label2.grid(column=2,row=1)

#label 3
my_label3=Label(text="is equal to : ",font=("Times New Roman",11,"bold"))
my_label3.grid(column=0,row=1)

#label result
result=Label(text="0",font=("Times New Roman",11,"bold"))
result.grid(column=1,row=1)

#button calculate
def button_clicked():
    numb_entere=int(entry.get())
    kilometers=round(numb_entere/0.6214,2)
    result.config(text=kilometers)
button1=Button(text="Calculate",command=button_clicked)
button1.grid(column=1,row=2)

#entry

entry=Entry(width=20)
entry.grid(column=1,row=0)




window.mainloop()