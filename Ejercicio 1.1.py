hor = 0
min = 0
seg = 0
res = 0

print("Dime una hora del día en horas, minutos y segundos")
hor = int(input("Horas: "))
min = int(input("Minutos: "))
seg = int(input("Segundos: "))

hor = hor * 3600
min = min * 60
res = hor + min + seg

print("Eso son: ", res, " Segundos")