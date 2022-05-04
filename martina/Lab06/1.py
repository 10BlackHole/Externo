# Definimos una función que nos entrega los divisores de 'P'
def divisores(P):
    divisores = []
    for i in range(1, P):
        if P%i == 0:
            divisores.append(i)
    return divisores

# 'N' cantidad de números a ingresar y 'P' guarda los números ingresados
N = int(input("Ingrese la cantidad de números a considerar: "))
while (N <= 0 or N > 100):          # Restricción para N
    print("Error, ingrese un número en el intervalo (0, 100]")
    N = int(input("Ingrese la cantidad de números a considerar: "))
P = []
for i in range(0, N):
    numeros = int(input("Ingrese un número: "))
    while (numeros <= 0):        # Restricción para P
        numeros = int(input("Error, ingrese un número mayor a 0: "))
    P.append(numeros)

# Iteracion para  ver si 'P' es número perfecto o no
for i in range(0, N):
    suma_divisores = 0
    for j in range(0, len(divisores(P[i]))):
        suma_divisores = suma_divisores + divisores(P[i])[j]
    if (suma_divisores == P[i]):
        print(P[i], " Es un número perfecto")
    else:
        print(P[i], " No es un número perfecto")
