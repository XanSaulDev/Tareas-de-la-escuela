Algoritmo Estructuras_de_control
	opcion <- 1
	Mientras opcion<>0 Hacer
		Escribir '1. Calcular la edad'
		Escribir '2. Calcular el factorial de 7'
		Escribir '0. Salir'
		Escribir 'Ingrese una opcion: '
		Leer opcion
		Segun opcion  Hacer
			1:
				Escribir '¿Cuantas edades quieres calcular? '
				Leer numero_de_edades
				i <- 0
				Mientras i<numero_de_edades Hacer
					Escribir 'Ingresa el año de nacimiento ',i+1,':'
					Leer fecha
					edad <- 2022-fecha
					Escribir 'edad ',edad
					Si edad<=17 Entonces
						Escribir 'Eres menor de edad.'
					SiNo
						Si edad>=25 Y edad<=50 Entonces
							Escribir 'Eres una persona joven.'
						SiNo
							Si edad>=50 Y edad<=100 Entonces
								Escribir 'Eres una persona mayor.'
							SiNo
								Si edad<=0 Entonces
									Escribir 'Ingresa un año valido.'
								FinSi
							FinSi
						FinSi
					FinSi
					i <- i+1
				FinMientras
			2:
				Escribir 'El factorial de 7 es: 5040'
			0:
				Escribir 'Saliendo...'
			De Otro Modo:
				Escribir 'opcion no valida.'
		FinSegun
	FinMientras
FinAlgoritmo
