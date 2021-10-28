''' Crea un script llamado vect3.py, que dado un vector de 50 elementos enteros, lo descomponga
en dos, uno formado por los valores pares y otro formado por los valores impares. En los dos
vectores resultantes los valores se podrán consecutivamente, uno detrás del otro, sin huecos'''
        
def detector_pares():
    for i in vector:
        if i % 2 == 0:
            pares.append(i)
        else:
            impares.append(i)
    pares.sort()
    impares.sort()

import random
impares = []
pares = []
vector = []
x = 0

for i in range(1,50+1):
    ran = random.randint(1,1000)
    vector.append(ran)

detector_pares()
print("Estos numeros son los pares: ",pares)
print("Estos numeros son los impares: ",impares)
        
