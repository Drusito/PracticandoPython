coleccion = []

for i in range(0,5):
    coleccion.append(i)
    coleccion[i] = int(input(f"Selecciona un número para la posicion {i}: "))

print("########EL ARRAY ES EL SIGUIENTE########\n")
print("\t   [", end = " ")
for i in range(len(coleccion)):
    if(i == len(coleccion)-1):
        print(str(coleccion[i]) + "]\n")
    else:
        print(str(coleccion[i]) + ", ", end = "")