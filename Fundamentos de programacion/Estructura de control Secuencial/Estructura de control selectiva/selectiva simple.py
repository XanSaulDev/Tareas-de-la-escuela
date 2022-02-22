#Python 3.8.5
#Scrpit que calcula el 20% en la compra de un numero de libros
#Huerta Murillo Alejandro Saul 21/02/22

#Entrada de datos
print()
cantidad_de_libros=int(input("Cantidad de libros comprada: "))

print()
precio=float(input("Introduzca el precio del libro: "))
subtotal=precio*cantidad_de_libros

#Declarar variables necesarias
iva=0
descuento=0
iva=(15/100)*subtotal
total=subtotal+iva

#Aplicar descuento si se da la condicion
if subtotal >= 700:
    descuento=(20/100)*subtotal
    total=total-descuento

#Salida de datos
print()
print(f"Subtotal a pagar--->{subtotal}$")
print(f"Descuento --->{descuento}$")
print(f"IVA a pagar--->{iva}$")
print()
print(f"Total a pagar--->{total}$")

