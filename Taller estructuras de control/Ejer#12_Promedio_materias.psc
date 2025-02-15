Algoritmo Promedio_Alumno
	// Promedio Matematicas
	Escribir "Ingrese la nota del examen de Matemática: "
	Leer Examen_Mate
	Escribir "Ingrese las tres notas de tareas de Matemática: "
	Leer nota_mate1, nota_mate2, nota_mate3
	Promedio_Mate=(Examen_Mate*0.9)+(((nota_mate1+nota_mate2+nota_mate3)/3)*0.1)
	// Promedio Fisica
	Escribir "Ingrese la nota del examen de Física: "
	Leer Examen_Fisica
	Escribir "Ingrese las dos notas de tareas de Física: "
	Leer Nota_fisi1, Nota_fisi2
	Promedio_Fisica=(Examen_Fisica*0.8)+(((Nota_fisi1+Nota_fisi2)/2)*0.2)
	// Promedio Quimica
	Escribir "Ingrese la nota del examen de Química: "
	Leer Examen_Quimica
	Escribir "Ingrese las tres notas de tareas de Química: "
	Leer Nota_Quimica1, Nota_Quimica2, Nota_Quimica3
	
	Promedio_Quimica=(Examen_Quimica*0.85)+(((Nota_Quimica1+Nota_Quimica2+Nota_Quimica3)/3)*0.15)
	
	Promedio_General=(Promedio_Mate+Promedio_Fisica+Promedio_Quimica)/3
	
	Escribir "Promedio Matemática: ", Promedio_Mate
	Escribir "Promedio Física: ", Promedio_Fisica
	Escribir "Promedio Química: ", Promedio_Quimica
	Escribir "Promedio General: ", Promedio_General
FinAlgoritmo