Algoritmo Porcentaje_Interess
	anios=4
	Escribir "Ingrese el monto inicial del préstamo (Bolívares X): "
	Leer monto_inicial
	Escribir "Ingrese el total de intereses pagados (Bolívares Y): "
	Leer intereses
    porcentaje_interes=(intereses/(monto_inicial*anios))*100
	Escribir "El porcentaje de interés anual es: ", porcentaje_interes, "%"
FinAlgoritmo