#programa que realiza operaciones con dos numeros
#Huerta Murillo Alejandro Saul 16/02/03

from math import sqrt

#proceso
def operaciones(n,n2):
    """ Esta funcion realiza la suma, resta, division, multiplicación y raiz cuadrada

        toma dos argumentos
        n: float
        n2: float

        return: dict    
     """
    suma=n+n2
    resta= n-n2
    multiplicacion= n*n2
    division= n/n2
    raiz_cuadrada= lambda n: sqrt(n)

    return {
        "suma":suma,
        "resta":resta,
        "multiplicacion":multiplicacion,
        "division":division,
        "raiz cuadrada numero1":raiz_cuadrada(n),
        "raiz cuadrada numero2":raiz_cuadrada(n2),
    }

#datos de entrada
numero=float(input("Ingrese el primer numero: "))
numero2=float(input("Ingrese el segundo numero: "))

resultados=operaciones(numero,numero2)

#datos de salida
print()
for key,value in resultados.items():
    print(f"{key}: {value}")
print()
