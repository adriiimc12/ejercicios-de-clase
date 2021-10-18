from funciones import *

Menu = True

while(Menu):
    
    imprimirmenu()
    
    opcion = int(input())
    
    if (opcion == 1):
        leer_archivo()
    elif (opcion == 2):
        añadirlinea_archivo()
    elif (opcion == 3):
        borrar_archivo()
    elif (opcion == 4):
        break