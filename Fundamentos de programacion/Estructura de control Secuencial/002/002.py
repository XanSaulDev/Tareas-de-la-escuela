#Python 3.8.5
#Scrpit que calcula la edad y calcula el factorial de 7
#Huerta Murillo Alejandro Saul 16/02/22

#Funciones
import datetime

def factorial_de_7():
    """
        Esta funcion calcula el factorial de 7
    """
    resultado=1
    for i in range(1,8):
       resultado=resultado*i 
    #Datos de salida
    print()
    print(f"EL factorial de 7 es {resultado}")

def calcular_edad():

    #datos de entrada
    numero_de_edades=int(input("¿Cuantas edades quieres calcular? "))
    print()

    #obteniendo al año actual sin importar en que momento veas esto
    fecha_nacimiento=[]
    fecha_actual = datetime.datetime.now()
    fecha = fecha_actual.date()
    ano_actual = int(fecha.strftime("%Y"))

    edades=[]

    #declarando rango de edades
    rangos_de_edad={      
        "1":{
            "min":1,
            "max":17,
            "value": "Eres menor de edad."
        },
        "2":{
            "min":25,
            "max":50,
            "value": "Eres una persona joven."
        },
        "3":{
            "min":50,
            "max":100,
            "value": "Eres una persona mayor."
        },
    }

    #datos de entrada
    for i in  range(1,numero_de_edades+1):
        fecha=int(input(f"Ingresa el año de nacimiento {i}: "))
        fecha_nacimiento.append(fecha)

    #haciendo la operacion para sacar la edad (restar la fecha de nacimiento al año actual)
    print()
    for fecha in fecha_nacimiento:
        edad=ano_actual-fecha
        if edad<=0 or edad>=120:
            print("Error fecha introducida incorrecta.")
            return
        edades.append(edad)

    #comprobando el correspondiente rango de edad
    for edad in edades:
        print("------------------------")
        if edad>=18:
            print(f"{edad} es mayor de edad")
        for _,rangos in rangos_de_edad.items():
            if edad in range(rangos.get("min"),rangos.get("max")+1):
                print(rangos.get('value'))
        print("------------------------")

#agregando funciones a las opciones
opciones={
    1:calcular_edad,
    2:factorial_de_7,  
}

def menu():
    """ 
        Menu que determina el flujo del script
    """
    #mostrar opciones
    print()
    print("1. Calcula edad")
    print("2. Calcula el factorial de 7")
    print("3. Salir")

    #datos de entrada
    opcion=int(input("Ingrese la opción: "))
    print()

    #identificando la opcion y corriendo la funcion correspondiente
    for o,funcion in opciones.items():
        if o==opcion:
            funcion()
            return

menu()