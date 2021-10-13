x = 0
num = 0
lista = []

print("Dime 5 numeros: ")
num = int(input())
lista .append(num)

while x < 4:
    
    num = int(input())
    lista .append(num)
    x = x + 1
    
lista .sort()
print("El numero mas grande es",lista[4],"y el mas pequeño es",lista[0])

