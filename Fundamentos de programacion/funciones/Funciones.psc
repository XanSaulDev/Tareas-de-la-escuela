Funcion ordenar_valores (  )
	Escribir "utilizar extend(numeros[::-1]) para invertir el arreglo"
Fin Funcion

Funcion imprimir_valores_ordenados (  )
	Escribir numeros_ord
Fin Funcion

Funcion imprimir_valores_originales (  )
	Escribir numeros
Fin Funcion

Funcion capturar_valores ( )
	i<-0
	Escribir "Numeros a ingresar: "
	Leer numero_de_numeros
	Mientras i<numero_de_numeros Hacer
		Escribir "Introduce el numero: "
		Leer n
		Si n<0 Entonces
			Escribir "El numero no puede ser negativo"
		SiNo
			Escribir "Utilizar la funcion append() para agregar los datos a la lista"
			i<-i+1
		Fin Si
	Fin Mientras
Fin Funcion


Algoritmo Funciones
	opcion<-1
	Definir numeros como entero;
	Definir numeros_ord como entero;
	Mientras opcion<>5 Hacer
		Escribir "1. Capturar valores"
		Escribir "2. Ordenar valores"
		Escribir "3. imprimir valores originales"
		Escribir "4. imprimir valores ordenados"
		Escribir "5. Salir"
		Escribir "Ingrese una opcion:"
		Leer opcion
		Si opcion==1 Entonces
			capturar_valores()
		SiNo
			Si opcion==2 Entonces
				ordenar_valores()
			SiNo
				Si opcion==3 Entonces
					imprimir_valores_originales()
				SiNo
					Si opcion==4 Entonces
						imprimir_valores_ordenados()
					SiNo
						Si opcion==5 Entonces
							Escribir "Saliendo."
						SiNo
							Escribir "Opcion no valida"
						Fin Si
					Fin Si
				Fin Si
			Fin Si
		Fin Si
	Fin Mientras
FinAlgoritmo
