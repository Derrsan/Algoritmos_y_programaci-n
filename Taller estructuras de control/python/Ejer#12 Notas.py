#Promedio Matematicas
Examen_Mate = float(input("Ingrese la nota del examen de Matemática: "))
	
nota_mate1, nota_mate2, nota_mate3 = map(float(input("Ingrese las tres notas de tareas de Matemática: ")).split()) 
Promedio_Mate=(Examen_Mate*0.9)+(((nota_mate1+nota_mate2+nota_mate3)/3)*0.1)
#Promedio Fisica
Examen_Fisica = map(float(input("Ingrese la nota del examen de Física: ")).split()) 
Nota_fisi1, Nota_fisi2 = map(float(input("Ingrese las dos notas de tareas de Física: ")).split())
Promedio_Fisica=(Examen_Fisica*0.8)+(((Nota_fisi1+Nota_fisi2)/2)*0.2)
#Promedio Quimica
Examen_Quimica = map(float(input("Ingrese la nota del examen de Química: ")).split())
Nota_Quimica1, Nota_Quimica2, Nota_Quimica3 = map(float(input("Ingrese las tres notas de tareas de Química: ")).split()) 
Promedio_Quimica=(Examen_Quimica*0.85)+(((Nota_Quimica1+Nota_Quimica2+Nota_Quimica3)/3)*0.15)
Promedio_General=(Promedio_Mate+Promedio_Fisica+Promedio_Quimica)/3
print("Promedio Matemática: ", Promedio_Mate)
print("Promedio Física: ", Promedio_Fisica)
print("Promedio Química: ", Promedio_Quimica)
print("Promedio General: ", Promedio_General)
