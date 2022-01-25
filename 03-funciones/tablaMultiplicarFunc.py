def tablaMultiplicar(numero):
    for i in range(1,11):
        multiplicacion = i*numero
        print(f"{i} X {numero} = {multiplicacion}")

num = int(input("Introduce un numero para saber su tabla de multiplicar: "))
tablaMultiplicar(num)

