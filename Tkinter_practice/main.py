# This is a sample Python script.
from tkinter import  *#se importa la libreria de tkinter

window= Tk()#se creo la pantalla
#aqui se comienza con el codigo de va en este espacio
window.title("My first GUI program")#agrega el titulo  a la pantalla
window.minsize(width=500,height=300)#definimos el tamano por default de la pantalla

#Label
my_label=Label(text="aqui mi primera GUI",font=("Arial",24,"bold"))
#una vez creado el label tenemos que indicar como lo vamos a mostrar en la pantalla
my_label.pack()#muestra el label cente  rado en la pantalla
#button
def button_clicked():
    print("i got clicked")
    new_text=input.get()
    my_label.config(text=new_text)
button=Button(text="click Me" , command=button_clicked)
button.pack()
#entry component
input= Entry(width=10)#we add a chart o add text
input.pack()
print(input.get())#with .get we get the information inside the chart




window.mainloop()#se establece el loop para que la pantalla se mantenga,siempre tiene que ir al final del programa
