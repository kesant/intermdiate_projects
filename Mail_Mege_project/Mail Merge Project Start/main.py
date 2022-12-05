#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
def obtener_nombres():
    with open("./Input/Names/invited_names.txt","r") as file:# abrimos el archivo en modo lectura
        nombres=file.readlines()#almacenamos todas las lineas del archivoen una lista
    return nombres
def obtener_carta():
    with open("./Input/Letters/starting_letter.txt","r") as file:# abrimos el archivo en modo lectura
        carta=file.readlines()#almacenamos todas las lineas del archivoen una lista
    return carta
def realizar_carta(nombre,carta):
    nombre=nombre.strip('\n')
    carta2=carta.copy()
    carta2[0] = carta2[0].replace("[name]", nombre)
    with open(f"./Output/ReadyToSend/letter_to_{nombre}.txt","w") as file :
        for linea in carta2:
            file.write(f"\n{linea}")

#programa principal
nombres=obtener_nombres()
print(nombres)
carta=obtener_carta()
print(carta)
for nombre in nombres:
    realizar_carta(nombre,carta)

