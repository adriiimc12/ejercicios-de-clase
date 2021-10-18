
def escribir_archivo():
    from io import open
    texto = input("Dime que texto guardar:")
    fichero = open('fichero.txt','w')
    fichero.write(texto)
    fichero.close()
    
def leer_archivo():
    from io import open
    fichero = open('fichero.txt','r')
    texto = fichero.read()
    fichero.close()
    print("Los nombres son:")
    print(texto)
    
def añadirlinea_archivo():
    from io import open
    fichero = open('fichero.txt','a')
    texto = input("Dime que texto guardar:")
    fichero.write(texto)
    fichero.write('\n')
    fichero.close()
    
def borrar_archivo():
    from io import open
    print("Se borraran todos los nombres. ¿Estas Seguro?:")
    print("1.Si")
    print("2.No")
    res = int(input())
    if (res == 1):
        fichero = open('fichero.txt','w')
        texto = "   "
        fichero.write(texto)
        fichero.close()
    
def imprimirmenu():
    print("1. Lista de Nombres")
    print("2. Escibir nuevo nombre")
    print("3. Borrar todos los nombres")
    print("4. Salir")
    
