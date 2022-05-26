#Huerta Murillo Alejandro Saul 01/03/22
#Script que maneja con n numeros en un arreglo y los ordena


from pip import main


numeros=[]
numeros_ord=[]

def menu():

    print(""" 
    1. Capturar valores
    2. Ordenar valores
    3. imprimir valores originales
    4. imprimir valores ordenados
    5. Salir

    """)
    #entrada de datos
    opcion=int(input("opcion: "))
    print()
    if opcion in range(1,5):
        while opcion!=5:
            for o,function in funciones.items():
                if o==opcion:
                    function()
            print(""" 
    1. Capturar valores
    2. Ordenar valores
    3. imprimir valores originales
    4. imprimir valores ordenados
    5. Salir

                """)
            opcion=int(input("opcion: "))
            print()
        


def capturar_valores():
    numero_de_numeros=int(input("Numeros a ingresar: "))
    for i in range(0,numero_de_numeros):
        n=float(input("Introduce el numero: "))
        numeros.append(n)


def ordenar_valores():
    numeros_ord.extend(numeros)

def imprimir_valores_ordenados():
    print(sorted(numeros_ord))

def imprimir_valores_originales():
    print(numeros)


funciones={
    1: capturar_valores,
    2: ordenar_valores,
    3: imprimir_valores_originales,
    4: imprimir_valores_ordenados,
}
main()