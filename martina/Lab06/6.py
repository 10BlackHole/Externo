N = int(input("Número de lugares donde las personas pueden pararse: "))
while (N <= 0):
    N = int(input("Error, ingrese un número mayor a 0: "))

A = []
for i in range(0, N):
    a = int(input("Ingrese un 0 si es vacío o un 1 si es ocupado: "))
    if (a!=0 or a!=1):
        a = int(input("Error, ingrese un 0 si es vacío o un 1 si es ocupado: ")) 
    A.append(a)

# Creamos una lista que contiene la informacion de los 1's
list_1 = []
for i in range(0, N):
    if (A[i] == 1):
        list_1.append(i)

if (N == 1):
    print("Se cumple el protocolo de distanciamiento social")
elif (len(list_1)==0 or len(list_1)==1):
    print("Se cumple el protocolo de distanciamiento social")
else:
    for i in range(0, len(list_1) - 1):
        if (list_1[i+1] - list_1[i]) < 5:
            print("No se cumple el protocolo de distanciamiento social")
            break
        else:
            print("Se cumple el protocolo de distanciamiento social")
