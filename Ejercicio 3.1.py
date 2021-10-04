x = 0
res = 0
mul = 0

res = int(input("Dime un número: "))
mul = res

while x < 10:
    x = x + 1
    res = mul * x
    print(mul,"X", x, "=", res)
    