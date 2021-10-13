n=0
mul=0

n = int(input("Dime un numero:"))

for i in (3,n+1):
    if(i % 3 == 0):
        mul += 1

print("Hay ", mul , " multiplos de 3 en", n)
