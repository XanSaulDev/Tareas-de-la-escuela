#Huerta Murillo Alejandro Saul 01/03/22
#Script que maneja con n numeros en un arreglo y los ordena

numeros=[]
numeros_ord=[]
opcion=1

while opcion!=5:
    #datos de salida
    print(""" 
    1. Capturar valores
    2. Ordenar valores
    3. imprimir valores originales
    4. imprimir valores ordenados
    5. Salir

    """)

    #Proceso de datos
    #datos de salida y entrada
    opcion=int(input("Ingrese una opcion: "))
    if opcion==1:
        #datos de salida y entrada
        numero_de_numeros=int(input("Numeros a ingresar: "))
        for i in range(0,numero_de_numeros):
            #datos de salida y entrada
            n=float(input("Introduce el numero: "))
            numeros.append(n)
    elif opcion==2:
        numeros_ord.extend(sorted(numeros))
    elif opcion==3:
        print(numeros)
    elif opcion==4:
        print(numeros_ord)
    elif opcion==5:
        #datos de salida
        print("Saliendo...")
    else:
        #datos de salida
        print("Opcion no valida")
    
