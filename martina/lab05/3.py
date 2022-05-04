numero = int(input("Ingrese un número entero mayor que cero: "))
while numero <= 0:
    print("Error, valor mal ingresado")
    numero = int(input("Ingrese un número entero mayor que cero: "))

suma = 0
if numero % 2 == 0:
    for i in range(0, numero + 1, 2):
        suma = suma +i
else:
    for i in range(0 ,numero , 2):
        suma = suma + i
print(suma)
