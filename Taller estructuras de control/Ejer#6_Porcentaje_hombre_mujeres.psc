Algoritmo Hombre_y_mujeres
	Escribir "Escriba cuantos hombres hay"
	Leer x_hombres
	Escribir "Escriba cuantas mujeres hay"
	Leer x_mujeres
	Total_estudiantes<-x_hombres+x_mujeres
	PorcentajeHombres<-(x_hombres/Total_estudiantes*100)
	PorcentajeMujeres<-(x_mujeres/Total_estudiantes*100)
	Escribir "El porcentaje de Hombres en clase son: ", PorcentajeHombres,"%"
	Escribir "El porcentaje de Mujeres en clase son: ", PorcentajeMujeres, "%"
FinAlgoritmo