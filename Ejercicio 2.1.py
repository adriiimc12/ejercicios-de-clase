grados = 0

print("¿ A qué temperatura se encuentra el agua ?")
grados  = int(input("Grados celsius:"))

if grados < 0:
    print("El agua esta en estado solido")
    
if grados >= 0 and grados < 100:
    print("El agua esta en estado liquido")
    
if grados >= 100:
    print("El agua esta en estado liquido")