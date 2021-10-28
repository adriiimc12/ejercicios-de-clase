'''Crea un programa llamado vect4.py, en el que el usuario introduzca un número entero y el
programa genere una frase con las palabras correspondientes a cada cifra. 
Por ejemplo, 547 devolvería “cinco cuatro siete”.'''

def numeros_letras():
    if i == "0":
        letras.append("Cero")
    elif i == "1":
        letras.append("Uno")
    elif i == "2":
        letras.append("Dos")
    elif i == "3":
        letras.append("Tres")
    elif i == "4":
        letras.append("Cuatro")
    elif i == "5":
        letras.append("Cinco")
    elif i == "6":
        letras.append("Seis")
    elif i == "7":
        letras.append("Siete")
    elif i == "8":
        letras.append("Ocho")
    elif i == "9":
        letras.append("Nueve")
    

x = input("Dime un numero que separar en digitos: ")

digitos = []
letras = []

for i in str(x):
    digitos.append(i)
    
for i in digitos:
    numeros_letras()
    
print(letras)