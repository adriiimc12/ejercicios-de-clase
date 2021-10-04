F = 0
C = 0
res = 0

'Menu para seleccionar si transformar farenheit o celsius:'

print("Presiona '1' si quieres pasar de celsius a farenheit")
print("Presiona '2' si quieres pasar de farenheit a celsius")
res = int(input())


if res == 1:
    C = float(input("Dime una temperatura en ºC para convertir: "))
    F= (C * 1.8) + 32
    print("Eso serían: ", F , "º Farenheit")

    
if res == 2:
    F = float(input("Dime una temperatura en ºF para convertir: "))
    C= (F - 32) / 1.8
    print("Eso serían: ", C , "º Celsius")