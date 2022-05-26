#Huerta Murillo Alejandro Saul 25/05/22
#Script que maneja con n numeros en un arreglos con funciones.

numeros=[]
numeros_ord=[]
opcion=1

#proceso
def capturar_valores():
    i=0
    #datos de salida
    numero_de_numeros=int(input("Numeros a ingresar: "))
    while i<numero_de_numeros:
        #entrada de datos
        #datos de salida
        n=float(input("Introduce el numero: "))
        if n<0:
            #datos de salida
            print("El numero no puede ser negativo")
        else: 
            numeros.append(n)
            i+=1

#proceso
def imprimir_valores_originales():
    print(numeros)

#proceso
def imprimir_valores_ordenados():
    print(numeros_ord)

#proceso
def ordenar_valores():
    numeros_ord.extend(numeros[::-1])

#proceso
while opcion!=5:
    #datos de salida
    print(""" 
    1. Capturar valores
    2. Ordenar valores al revez
    3. imprimir valores originales
    4. imprimir valores ordenados al revez
    5. Salir

    """)
    #datos de salida y entrada
    opcion=int(input("Ingrese una opcion: "))

    #Proceso de datos
    if opcion==1:
        capturar_valores()
    elif opcion==2:
        ordenar_valores()
    elif opcion==3:
        imprimir_valores_originales()
    elif opcion==4:
        imprimir_valores_ordenados()
    elif opcion==5:
        #datos de salida
        print("Saliendo...")
    else:
        #datos de salida
        print("Opcion no valida")
    
