N = int(input("Ingrese la cantidad de datos: "))
datos = []
for i in range(0, N, 1):
    numeros = int(input("Ingrese un numero: "))
    datos.append(numeros)

par = []
impar = []

suma = 0
multiplicacion = 1

for j in range(0, N):
    if datos[j]%2 == 0:
        par.append(datos[j])
    else:
        impar.append(datos[j])
        
for k in range(0, len(par)):
    suma = suma + par[k]
for h in range(0, len(impar)):
    multiplicacion = multiplicacion * impar[h]

print("La suma de los número pares ingresados es: ", suma)
print("La multiplicacion de los números impares ingresados es: ", multiplicacion)
