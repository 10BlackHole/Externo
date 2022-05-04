x = int(input("Ingrese un primer valor: "))
y = int(input("Ingrese un segundo valor: "))

if x < y:
    print(y, " es mayor que ", x)
elif x == y:
    print(x, " es igual a ", y)
else:
    print(x, " es mayor que ", y)
