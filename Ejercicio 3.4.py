x = 0
n = 2
divisores = 0

while x < 1000:
    x = x + 1
    n = 2
    divisores = 0
    if x < 2:
        print(x)
    else:
        while n < 1000:
            if x % n == 0:
                divisores = divisores + 1
            n = n + 1
    if divisores == 1:
        print(x)
        