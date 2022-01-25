from operator import indexOf
from tkinter import E


list2D = [
    {
        "categoria":"ACCIÓN",
        "juegos": ["GTA","COD", "PUBG"]
    },
    {
        "categoria":"AVENTURA",
        "juegos":["Assasains", "Crash", "Prince of persia"]
    },
    {
        "categoria":"DEPORTES",
        "juegos": ["FIFA21","PES21","MOTOGP21"]
    }
    ]

def recorrerLista(list):
    for categoria in list:
        print(categoria["categoria"])
        print("-------------------")
        for juego in categoria["juegos"]:
            print(juego)
        else: print()
    
recorrerLista(list2D)
