Algoritmo Ejercicio_Seis
	escribir "Escriba el a�o"
	Leer a�o
	si (a�o mod 4 == 0) y (a�o mod 100 <> 0) o (a�o mod 400 = 0) Entonces
		Escribir "El a�o es bisiesto"
	SiNo
		Escribir"El a�o no es bisiesto"
	FinSi
	
FinAlgoritmo