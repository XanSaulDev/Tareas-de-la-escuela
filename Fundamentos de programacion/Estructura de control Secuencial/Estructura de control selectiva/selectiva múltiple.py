#Python 3.8.5
#Scrpit que imprime el mes correspondiente al numer ingresado
#Huerta Murillo Alejandro Saul 21/02/22

# Codigo hecho de una manera mejor

# meses={
#     1:"Enero", 
#     2:"Febrero",
#     3:"Marzo", 
#     4:"Abril", 
#     5:"Mayo", 
#     6:"Junio", 
#     7:"Julio", 
#     8:"Agosto", 
#     9:"Septiembre", 
#     10:"Octubre", 
#     11:"Noviembre", 
#     12:"Diciembre"
# }

# #Entrada de datos
# print()
# numero=int(input("Introduce un número: "))
# print()

# #Salida de datos
# if numero in range(1,12+1):
#     print(meses.get(numero))
#     print()


#Entrada de datos
print()
numero=int(input("Introduce un número: "))
print()

#Salida de datos
if numero==1:
    print("Enero")
elif numero==2:
    print("Febrero")
elif numero==3:
    print("Marzo")
elif numero==4:
    print("Abril")
elif numero==5:
    print("Mayo")
elif numero==6:
    print("Junio")
elif numero==7:
    print("Julio")
elif numero==8:
    print("Agosto")
elif numero==9:
    print("Septiembre")
elif numero==10:
    print("Octubre")
elif numero==11:
    print("Noviembre")
elif numero==12:
    print("Diciembre")
