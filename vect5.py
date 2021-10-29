'''Crea un programa llamado vect5.py, en el que el usuario introduzca una palabra o frase y el
programa diga si es palíndromo, es decir, si se lee igual hacia delante que hacia atrás. 
Por ejemplo “amor a roma”, “ojo” y “arribalabirra” son palíndromos'''

lista = []
listainv = []
x = input("Dime una palabra: ")

for i in x:
    lista.append(i)
    
n = len(lista)

for i in lista:
    listainv.append(lista[n-1])
    n = n - 1
res = "".join(listainv)

if res == x:
    print("La palabra",x,"es palindroma")
else:
    print("La palabra",x,"no es palindroma")
