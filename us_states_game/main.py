import turtle
import pandas
import funciones
from estado import State
screen= turtle.Screen()
screen.title("U.S States game")
image="blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
#para obtener la posicion de donde se clickea en la pantalla
# def get_mouse_click_coor(x,y):
#     print(x,y)

# turtle.onscreenclick(get_mouse_click_coor)
estados,list_post_x,list_post_y=funciones.obtener_datos()
guessed_states=[]
while len(guessed_states)<50:
    answer_state=screen.textinput(title=f"{len(guessed_states)}/50 states correct ",prompt="whats another state name").lower()
    if answer_state=="exit":
        missing_states=[]
        for est in estados:
            if est not in guessed_states:
                missing_states.append(est)
        new_data=pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in estados:
        guessed_states.append(answer_state)
        posicion_x,posicion_y=funciones.obtener_posicion(answer_state,estados,list_post_x,list_post_y)
        estado=State(posicion_x,posicion_y,answer_state)

#turtle.mainloop()#its the same as exict  on click






#screen.exitonclick()