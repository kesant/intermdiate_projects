
import pandas


def obtener_datos():
    """Lee el archivo csv y retorna la columna de estados, y sus posiciones"""
    datos = pandas.read_csv("50_states.csv")
    estados = datos["state"].to_list()
    estados_minusculas = [x.lower() for x in estados]
    posicion_x = datos["x"].to_list()
    posicion_y = datos["y"].to_list()
    return estados_minusculas,posicion_x,posicion_y

def obtener_posicion(user_state,estados,posicion_x,posicion_y):
    """recive por entrada el nombre del estado digitado por el usuario , las listas
    de estados y las listas de sus posiciones, retorna la posicion del estado
    """
    indice=estados.index(user_state.lower())
    posicion_x=posicion_x[indice]
    posicion_y=posicion_y[indice]
    return posicion_x,posicion_y
