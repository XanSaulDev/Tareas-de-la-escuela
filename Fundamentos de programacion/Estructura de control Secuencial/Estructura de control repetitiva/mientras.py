#Python 3.8.5
#Scrpit que muestra las 10 primeras potencias de un nummero
#Huerta Murillo Alejandro Saul 21/02/22

#Entrada de datos
print()
numero=int(input("Introduce un número: "))
print()

if numero>0:
    i=1
    #Salida de datos
    while i<=10:
        print(f"{numero}^{i}={numero**i}")
        i+=1
else:
    print("El numero tiene que ser mayor o difetente que 0")
    
