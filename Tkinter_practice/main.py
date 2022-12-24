# This is a sample Python script.
import tkinter #se importa la libreria de tkinter

window= tkinter.Tk()#se creo la pantalla
#aqui se comienza con el codigo de va en este espacio
window.title("My first GUI program")#agrega el titulo  a la pantalla
window.minsize(width=500,height=300)#definimos el tamano por default de la pantalla

#Label
my_label=tkinter.Label(text="aqui mi primera GUI")



window.mainloop()#se establece el loop para que la pantalla se mantenga,siempre tiene que ir al final del programa
