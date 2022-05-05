from numpy import sqrt
 
def distancia(a,b):
    dif = 0
    for i in range(3):
        dif = dif + (b[i] - a[i])**2
    return sqrt(dif)

P1 = []
P2 = []
Pp1 = []
Pp2 = []

for i in range(3):
    p1 = int(input("Ingrese las coordeenadas de P1: "))
    P1.append(p1)

for i in range(3):
    p2 = int(input("Ingrese las coordeenadas de P2: "))
    P2.append(p2)

for i in range(3):
    pp1 = int(input("Ingrese las coordeenadas de Pp1: "))
    Pp1.append(pp1)

for i in range(3):
    pp2 = int(input("Ingrese las coordeenadas de Pp2: "))
    Pp2.append(pp2)

desplazamiento = abs(distancia(P1, P2) - distancia(Pp1, Pp2)) 

print("d(P1, P2) = ", distancia(P1, P2))
print("d(P'1, P'2) = ", distancia(Pp1, Pp2))
print("Magnitud de desplazamiento = ", desplazamiento)
