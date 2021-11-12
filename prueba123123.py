import random

def generamatriz(numf,numc,valor):
    return [[valor for c in range(0,numc)] for f in range(0,numf)]
def numerorandom():
    for i in 0,num_filas_a:
        x = random.randint(0,10)
    return x

num_filas_a= int(input("Dime un numero de filas para la matriz:"))
num_columnas_a= int(input("Dime un numero de filas para la matriz:"))


matrizA = generamatriz(num_filas_a,num_columnas_a,numerorandom())
matrizB = generamatriz(num_filas_a,num_columnas_a,numerorandom())
nuevalista = []

for n in range(len(matrizA)):
    for i in range(len(matrizA[0])):
        nuevalista.append(matrizA[n][i]+matrizB[n][i])
        
matrizfinal = [nuevalista[i:i + num_filas_a] for i in range(0, len(nuevalista), num_filas_a)]
print(matrizfinal)

'''
while (contador < num_columnas_a):
    for index in matrizA[contador][index-1]:
        random = random.radint(0,10)
        matrizA.append(random)
'''