def generamatriz(numf,numc,valor):
    return [[valor for c in range(0,numc)] for f in range(0,numf)]

def mostrartablero():
    x = 0
    while x < len(tablero):
        print(tablero[x])
        x += 1
    turnousuario()

        
def comprobador():
    if (tablero[fila_usu][colum_usu] == " "):
        if usu == 1:
            tablero[fila_usu][colum_usu] = "X"
        elif usu == 2:
            tablero[fila_usu][colum_usu] = "O"
    else:
        print("Esa casilla ya esta ocupada. Por favor escoje otra")
        turnousuario()

def turnousuario():
    print("Jugador",usu,". Escriba la fila que desea cambiar")
    global fila_usu
    fila_usu = int(input()) - 1
    print("Jugador",usu,". Escriba la columna que desea cambiar")
    global colum_usu
    colum_usu = int(input()) - 1
    comprobador()
        
def comprobarganador():
    if((tablero[0][0] and tablero[0][1] and tablero[0][2] == 'X') or (tablero[1][0] and tablero[1][1] and tablero[1][2] == 'X') or (tablero[2][0] and tablero[2][1] and tablero[2][2] == 'X') or (tablero[0][0] and tablero[1][0] and tablero[2][0] == 'X') or (tablero[0][1] and tablero[1][1] and tablero[2][1] == 'X') or (tablero[0][2] and tablero[1][2] and tablero[2][2] == 'X') or (tablero[0][0] and tablero[1][1] and tablero[2][2] == 'X') or (tablero[0][2] and tablero[1][1] and tablero[2][0] == 'X')):
        print("Jugador 1, ¡Eres el ganador!")
        return True
    elif((tablero[0][0] and tablero[0][1] and tablero[0][2] == 'O') or (tablero[1][0] and tablero[1][1] and tablero[1][2] == 'O') or (tablero[2][0] and tablero[2][1] and tablero[2][2] == 'O') or (tablero[0][0] and tablero[1][0] and tablero[2][0] == 'O') or (tablero[0][1] and tablero[1][1] and tablero[2][1] == 'O') or (tablero[0][2] and tablero[1][2] and tablero[2][2] == 'O') or (tablero[0][0] and tablero[1][1] and tablero[2][2] == 'O') or (tablero[0][2] and tablero[1][1] and tablero[2][0] == 'O')):
        print("Jugador 2, ¡Eres el ganador!")
        return True
    else:
        return False

tablero = generamatriz(3,3," ")
usu = 1
mostrartablero()
contador = 2
while contador < 9:
    if contador % 2 == 0:
        usu = 2
    else:
        usu = 1
    if comprobarganador() == True:
        break
    else:
        mostrartablero()
        contador += 1
        comprobarganador()


'''((tablero[0][0] == 'X' or 'O') and (tablero[0][1] == 'X' or 'O') and (tablero[0][2] == 'X' or 'O') and (tablero[1][0] == 'X' or 'O') and (tablero[1][1] == 'X' or 'O') and (tablero[1][2] == 'X' or 'O') and (tablero[2][0] == 'X' or 'O') and (tablero[2][1] == 'X' or 'O') and (tablero[2][2] == 'X' or 'O'))'''
        
