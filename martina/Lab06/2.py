K = int(input("Ingrese número de consultas que serán realziadas: "))
for i in range(K):
    # Para un K
    N  = int(input("Ingrese la coordenada X: "))
    M  = int(input("Ingrese la coordenada Y: "))

    if (N<0 and M>0):
        print("Nlogonia Norocciedntal")
    elif (N>0 and M>0):
        print("Nlogonia Noriental")
    elif (N>0 and M<0):
        print("Nlogonia Sudoriental")
    elif (N>0 and M<0):
        print("Nlogonia Sudoccidental")
    else:
        print("Frontera")

