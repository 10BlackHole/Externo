v = int(input("Cantidad de votos: "))

F = []
C = []
X = []
_ = []

for i in range(v):

    voto = str(input("Ingrese voto: "))
    if (voto == "F" or voto == "f"):
        F.append(1)
    if (voto == "C" or voto == "c"):
        C.append(1)
    if (voto == "X" or voto == "x"):
        X.append(1)
    if (voto == "_" or voto == "-"):
        _.append(1)

inicitiva = (len(F) + len(_)) / (v - len(X))

print("Cantidad de votos a favor: ", len(F))
print("Cantidad de votos en contra: ", len(C))
print("Cantidad de votos nulos: ", len(X))
print("Cantidad de votos en blanco: ", len(_))

if (inicitiva > 2/3):
    print("Iniciativa aprobada")
else:
    print("Iniciativa rechazada")


