Algoritmo Ejercicio_Seis
	escribir "Escriba el año"
	Leer año
	si (año mod 4 == 0) y (año mod 100 <> 0) o (año mod 400 = 0) Entonces
		Escribir "El año es bisiesto"
	SiNo
		Escribir"El año no es bisiesto"
	FinSi
	
FinAlgoritmo