Nota_uno= float(input( "ingrese nota uno: "))
Nota_dos= float(input( "ingrese nota dos: "))
Nota_tres= float(input("ingrese nota tres: "))
Nota_examen_final=float(input("ingrese nota examen final: "))
Nota_trabajo_final=float(input("ingrese nota trabajo final: "))
Promedio_notas=(Nota_uno+Nota_dos+Nota_tres)/3
Calificacion_final=(Promedio_notas*0.55)+(Nota_examen_final*0.30)+(Nota_trabajo_final*0.15)
print("Calificacion final es de:", Calificacion_final)
