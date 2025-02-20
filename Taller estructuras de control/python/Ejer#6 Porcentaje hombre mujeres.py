x_hombres = int(input("Escriba cuantos hombres hay"))
x_mujeres = int(input("Escriba cuantas mujeres hay"))
Total_estudiantes = x_hombres+x_mujeres
PorcentajeHombres = (x_hombres/Total_estudiantes*100)
PorcentajeMujeres = (x_mujeres/Total_estudiantes*100)
print("El porcentaje de Hombres en clase son: ", PorcentajeHombres,"%")
print("El porcentaje de Mujeres en clase son: ", PorcentajeMujeres,"%")
