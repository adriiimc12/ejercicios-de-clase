import random

def generamatriz(numf,numc):
    return [[numerorandom() for c in range(0,numc)] for f in range(0,numf)]
def numerorandom():
    return random.randint(0,10)
def printearmatriz():
    x = 0
    while x < num_columnas_a:
        print(matrizfinal[x])
        x += 1


num_filas_a= int(input("Dime un numero de filas para la matriz:"))
num_columnas_a= int(input("Dime un numero de filas para la matriz:"))


matrizA = generamatriz(num_filas_a,num_columnas_a)
matrizB = generamatriz(num_filas_a,num_columnas_a)
nuevalista = []

for n in range(len(matrizA)):
    for i in range(len(matrizA[0])):
        nuevalista.append(matrizA[n][i]+matrizB[n][i])
        
matrizfinal = [nuevalista[i:i + num_filas_a] for i in range(0, len(nuevalista), num_filas_a)]
print("La suma de la matriz A+B es :")
printearmatriz()