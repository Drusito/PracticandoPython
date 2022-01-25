alumnos = [None]*4
print(len(alumnos))
for i in range(len(alumnos)):
    alumnos[i] = int(input(f"Que nota tiene el alumno {i} ? \n"))

for i in range(len(alumnos)):
    if(alumnos[i]<5):
        print(f"{OKGREEN}El alumno {i} ha suspendido con un {alumnos[i]} de nota.")
    else:
        print(f"El alumno {i} ha aprobado con un {alumnos[i]} de nota.")