num1 = int(input("Escribe el primer número: "))
num2 = int(input("Escribe el segundo número: "))

if num1 < num2:
    for i in range(num1,num2+1):
        mitad = i/2
        print(f"La mitad de {i} es {mitad}")
else:
    for i in range(num2, num1+1):
        mitad = i/2
        print(f"La mitad de {i} es {mitad}")