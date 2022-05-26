Algoritmo arreglos
	
	Definir numeros como entero;
	Definir numeros_ord como entero;
	opcion<-1
	Mientras opcion<>5 Hacer
		Escribir "1. Capturar valores"
		Escribir "2. Ordenar valores"
		Escribir "3. imprimir valores originales"
		Escribir "4. imprimir valores ordenados"
		Escribir "5. Salir"
		Escribir "Ingrese una opcion:"
		Leer opcion
		Si opcion==1 Entonces
			Escribir "Numeros a ingresar:"
			Leer numero_de_numeros
			Para i<-1 Hasta numero_de_numeros Con Paso 1 Hacer
				Escribir i,". Introduce el numero: "
				Escribir "utilizar funcion append()"
			Fin Para
		SiNo
			Si opcion==2 Entonces
				Escribir "utilizar funcion extend() y sorted()"
			SiNo
				Si opcion==3  Entonces
					Escribir numeros
				SiNo
					Si opcion==4  Entonces
						Escribir numeros_ord
					SiNo
						Si opcion==5  Entonces
							Escribir "Saliendo ..."
						SiNo
							Escribir "Opcion no valida"
						Fin Si
					Fin Si
				Fin Si
			Fin Si
		Fin Si
	Fin Mientras
	
FinAlgoritmo
