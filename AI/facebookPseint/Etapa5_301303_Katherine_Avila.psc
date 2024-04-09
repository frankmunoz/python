Algoritmo Facebook
	Dimension cumpleanos[12] // Vector con los meses
	sumaEdad <- 0 // acumulador de edades para calcular el promedio
	// Fecha de hoy
	dHoy <- 11 
	mHoy <- 12
	aHoy <- 2019
	Escribir Sin Saltar "Cantidad de empleados: "
	Leer empleados
	Para i<-1 Hasta empleados Con Paso 1 Hacer
		Escribir "Fecha de nacimiento (d’a mes a–o): "
		Escribir "Dia de nacimiento"
		Leer d
		Escribir "Mes de nacimiento"
		Leer m
		Escribir "A–o de nacimiento"
		Leer a
		edad <- aHoy - a
		si mHoy < m o ( mHoy = m y dHoy < d) Entonces
			edad <- edad - 1
		FinSi
		Si edad >= 18 y edad < 65 Entonces
			cumpleanos[m] <- cumpleanos[m] + 1
		Fin Si
		sumaEdad <- sumaEdad + edad
	Fin Para
	Escribir "Edad promedio: " sumaEdad / empleados
	bonificados <- 0
	Para i<-1 Hasta 12 Con Paso 1 Hacer
		Escribir "Mes: " i " Empleados: " cumpleanos[i] " Monto: " cumpleanos[i] * 50000
		bonificados <- bonificados + cumpleanos[i]
	Fin Para
	Escribir "Monto total a abonar: " bonificados * 50000
FinAlgoritmo