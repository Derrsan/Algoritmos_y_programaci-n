Algoritmo Pago_Luz
	Escribir "Ingrese la lectura anterior: "
	Leer Lectura_Anterior
	Escribir "Ingrese la lectura actual: "
	Leer Lectura_Actual
	Escribir "Ingrese el costo por kilovatio: "
	Leer Costo_Kw
	Total_Pagar=(Lectura_Actual-Lectura_Anterior)*Costo_Kw
	Total=abs(Total_Pagar)
	Escribir "El total a pagar por consumo de energia electrica es: ", Total
FinAlgoritmo