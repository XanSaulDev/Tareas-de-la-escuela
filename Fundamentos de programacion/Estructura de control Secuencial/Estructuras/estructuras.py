#Actividad 3. Estructuras de control
#Python 3.8.5
#Scrpit que calcula la edad y calcula el factorial de 7
#Huerta Murillo Alejandro Saul 16/02/22

from math import factorial

#menu
opcion=1
while opcion!=0:
    print("""
    1. Calcular la edad
    2. Calcular el factorial de 7
    0. Salir
    """)
    opcion=int(input("Ingrese una opcion: "))
    if opcion==1:
        numero_de_edades=int(input("¿Cuantas edades quieres calcular? "))
        i=0
        while i<numero_de_edades:
            fecha=int(input(f"Ingresa el año de nacimiento {i+1}: "))
            edad=2022-fecha
            print("Edad: ",edad)
            if edad<=17:
                print("Eres menor de edad.")
            elif edad>=25 and edad<=50:
                print("Eres una persona joven.")
            elif edad>=50 and edad<=100:
                print("Eres una persona mayor.")
            elif edad <=0:
                print("Ingresa un año valido.")
            i+=1
    elif opcion==2:
        print("El factorial de 7 es: ",factorial(7))
    elif opcion==0:
        print("Saliendo...")
    else:
        print("Opcion no valida")