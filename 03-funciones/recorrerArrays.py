from operator import truediv


listaNumeros = [1,2,3,4,5,6,7,8]
def encontrarNumer(listaNumeros):
    numeroEnArray = int(input("Busca un número en el array: "))
    for i in range(len(listaNumeros)):
        if(numeroEnArray == listaNumeros[i]):
            return True
    return False

def arrayToString(array):
    for i in range(len(listaNumeros)):
        if i == len(listaNumeros)-1:
            print(listaNumeros[i])
        else:
            print(str(listaNumeros[i]) + ", ", end = "")

def buscarNumeroEnArray(boolean, array):
    if(boolean):
        print("El número está en el array")
    else: 
        print("El número NO está en el array")

arrayToString(listaNumeros)
buscarNumeroEnArray(encontrarNumer(listaNumeros), listaNumeros)




