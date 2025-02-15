Algoritmo Porcentaje_Gananciaa
	Escribir "Ingrese la cantidad de naranjas compradas: "
	Leer Naranjas
	Escribir "Ingrese el costo por docena (Bs. Y): "
	Leer Docena_Naranjas
	Escribir "Ingrese el monto total obtenido por las ventas (Bs. K): "
	Leer K
	costo_inversion=(Naranjas/12)*Docena_Naranjas
	ganancia=K-costo_inversion
	porcentaje_ganancia=(ganancia/costo_inversion)*100
	Escribir "El porcentaje de ganancia obtenido es: ", porcentaje_ganancia, "%"
FinAlgoritmo