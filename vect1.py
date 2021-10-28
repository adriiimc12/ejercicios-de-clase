a = [0] * 2
b = [0, 0, 0]
a[0] = 2
a[1] = a[0] ** a[0]
a.append( a[0] + a[1] )
print(a)