#Funciones acabadas

'a) Con valores aleatorios entre 1 y 10, y a continuación diga cuantos pares e impares hay.'

def aleatorios_vector():
    import random
    vector = []
    pares = 0
    impares = 0
    x = 0
    res = 0
    for i in range(1,15+1):
        ran = random.randint(1,10)
        vector.append(ran)
    while x < 15:
        res = vector[x] % 2
        x += 1
        if res == 0:
            pares += 1
        else:
            impares += 1
    print("Hay ", pares, " pares y ", impares," impares")

'b) Con valores aleatorios entre 1 y 10, y a continuación sume los que estén en posiciones'
'que son múltiplos de 3.'

def multiplo3_vector():
    vector = []
    x = 0
    suma = 0
    for i in range(1,15+1):
        ran = random.randint(1,10)
        vector.append(ran)
    while x < len(vector)-1:
        x += 1
        if x % 3 == 0:
            suma = suma + vector[x]
    print("La suma es ", suma)

'c) Con los primeros valores de la serie de Fibonacci.'

def fibonacci_vector():
    vector = []
    x = 0
    fib1 = 1
    fib2 = 0
    res = 0
    vector.append(0)
    vector.append(1)
    while x < 14:
        res = fib1 + fib2
        fib2 = fib1
        fib1 = res
        vector.append(res)
        x += 1
        

'd) Con valores introducidos por el usuario, y a continuación que los imprima al revés.'

def inverso_vector():
    vector = []
    i = 0
    while i < 15:
        x = int(input("Escriba un numero: "))
        vector.append(x)
        i += 1
    vector.reverse()

'e) Con valores introducidos por el usuario, donde cada valor se debe pedir de nuevo hasta'
'que esté entre 1 o 10.'

def usuarionum_vector():
    vector = []
    i = 0
    while i < 15:
        x = int(input("Escriba un numero entre 1 y 10: "))
        if x <= 10 and 0 <= x:
            vector.append(x)
            i += 1
        else:
            print("Introduzca un numero correcto")

'f) Con valores introducidos por el usuario, que deben formar una secuencia creciente.'

def creciente_vector():
    vector = []
    i = 0
    x = -9999
    while i < 15:
        print("Escriba un numero mayor que", x,": ")
        res = int(input())
        if res > x:
            vector.append(res)
            i += 1
            x = res
        else:
            print("¡ Debe ser un numero mayor que ", x, " !")
    

'g) Con valores introducidos por el usuario, que no deben estar repetidos.'

def duplicados_vector():
    import collections
    vector = []
    index = 0
    x = 0
    while index < 15:
        x = int(input("Dime un numero que no se haya repetido: "))
        if x not in vector:
            vector.append(x)
            index += 1
        else:
            print("He dicho un numero que no este repetido")
        print(vector)
