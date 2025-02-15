Algoritmo Recargo_Computador
	Escribir "Ingrese el precio al contado del computador: "
	Leer P
	Escribir "Ingrese el valor de cada cuota: "
	Leer T
	total_cuotas=T*12
	porcentaje_recargo=((total_cuotas-P)/P)*100
	Escribir "El porcentaje de recargo por pagar a cuotas es: ", porcentaje_recargo, "%"
FinAlgoritmo