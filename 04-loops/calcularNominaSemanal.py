# int(input("De que hora a que hora has trabajado? (7-23)"))
from ast import Return
from errno import ESOCKTNOSUPPORT
from pickle import LIST


dias = {
        "lunes":0,
        "martes":0,
        "miercoles":0,
        "jueves":0,
        "viernes":0,
        "sabado":0,
        "domingo":0
    }


def preguntarHoras(list):
    for dia in list:
        if(dia=="lunes"):
            ans=input(f"Has trabajado el {dia}? (Y/N)").upper()
            if(ans == "Y"):
                n1=float(input(f"A que hora empezaste el {dia}? "))
                n2=float(input(f"A que hora acabaste el {dia}? "))
                if(n2>21.5):
                    horaNocturna = n2-21.5
                    horaDiurna = 21.5-n1
                    list[f"{dia}"]=horaDiurna*6+horaNocturna*9
                    dineroDiario = list[f"{dia}"]
                else:
                    list[f"{dia}"]=(n2-n1)*6
                    dineroDiario = list[f"{dia}"]
                print(f"Has hecho {dineroDiario}€ el {dia}")
            else: print()
        elif(dia=="martes"):
            ans=input(f"Has trabajado el {dia}? (Y/N)").upper()
            if(ans == "Y"):
                n1=float(input(f"A que hora empezaste el {dia}? "))
                n2=float(input(f"A que hora acabaste el {dia}? "))
                if(n2>21.5):
                    horaNocturna = n2-21.5
                    horaDiurna = 21.5-n1
                    list[f"{dia}"]=horaDiurna*6+horaNocturna*9
                    dineroDiario = list[f"{dia}"]
                else:
                    list[f"{dia}"]=(n2-n1)*6
                    dineroDiario = list[f"{dia}"]
                print(f"Has hecho {dineroDiario}€ el {dia}")
            else: print()
        elif(dia=="miercoles"):
            ans=input(f"Has trabajado el {dia}? (Y/N)").upper()
            if(ans == "Y"):
                n1=float(input(f"A que hora empezaste el {dia}? "))
                n2=float(input(f"A que hora acabaste el {dia}? "))
                if(n2>21.5):
                    horaNocturna = n2-21.5
                    horaDiurna = 21.5-n1
                    list[f"{dia}"]=horaDiurna*6+horaNocturna*9
                    dineroDiario = list[f"{dia}"]
                else:
                    list[f"{dia}"]=(n2-n1)*6
                    dineroDiario = list[f"{dia}"]
                print(f"Has hecho {dineroDiario}€ el {dia}")
            else: print()
        elif(dia=="jueves"):
            ans=input(f"Has trabajado el {dia}? (Y/N)").upper()
            if(ans == "Y"):
                n1=float(input(f"A que hora empezaste el {dia}? "))
                n2=float(input(f"A que hora acabaste el {dia}? "))
                if(n2>21.5):
                    horaNocturna = n2-21.5
                    horaDiurna = 21.5-n1
                    list[f"{dia}"]=horaDiurna*6+horaNocturna*9
                    dineroDiario = list[f"{dia}"]
                else:
                    list[f"{dia}"]=(n2-n1)*6
                    dineroDiario = list[f"{dia}"]
                print(f"Has hecho {dineroDiario}€ el {dia}")
            else: print()
        elif(dia=="viernes"):
            ans=input(f"Has trabajado el {dia}? (Y/N)").upper()
            if(ans == "Y"):
                n1=float(input(f"A que hora empezaste el {dia}? "))
                n2=float(input(f"A que hora acabaste el {dia}? "))
                if(n2>21.5):
                    horaNocturna = n2-21.5
                    horaDiurna = 21.5-n1
                    list[f"{dia}"]=horaDiurna*6+horaNocturna*9
                    dineroDiario = list[f"{dia}"]
                else:
                    list[f"{dia}"]=(n2-n1)*6
                    dineroDiario = list[f"{dia}"]
                print(f"Has hecho {dineroDiario}€ el {dia}")
            else: print()
        elif(dia=="sabado"):
            ans=input(f"Has trabajado el {dia}? (Y/N)").upper()
            if(ans == "Y"):
                n1=float(input(f"A que hora empezaste el {dia}? "))
                n2=float(input(f"A que hora acabaste el {dia}? "))
                if(n2>21.5):
                    horaNocturna = n2-21.5
                    horaDiurna = 21.5-n1
                    list[f"{dia}"]=horaDiurna*6+horaNocturna*9
                    dineroDiario = list[f"{dia}"]
                else:
                    list[f"{dia}"]=(n2-n1)*6
                    dineroDiario = list[f"{dia}"]
                print(f"Has hecho {dineroDiario}€ el {dia}")
            else: print()
        if(dia=="domingo"):
            ans=input(f"Has trabajado el {dia}? (Y/N)").upper()
            if(ans == "Y"):
                n1=float(input(f"A que hora empezaste el {dia}? "))
                n2=float(input(f"A que hora acabaste el {dia}? "))
                if(n2>21.5):
                    horaNocturna = n2-21.5
                    horaDiurna = 21.5-n1
                    list[f"{dia}"]=horaDiurna*6+horaNocturna*9
                    dineroDiario = list[f"{dia}"]
                else:
                    list[f"{dia}"]=(n2-n1)*6
                    dineroDiario = list[f"{dia}"]
                print(f"Has hecho {dineroDiario}€ el {dia}")
            else: print()
    return list

def calcularComputo(list):
    computo = 0
    for dia in list:
        computo+=list[f"{dia}"]
    return computo

dias=preguntarHoras(dias)

print(f"Has hecho {calcularComputo(dias)}€")




# input("Has trabajado el lunes?: ")