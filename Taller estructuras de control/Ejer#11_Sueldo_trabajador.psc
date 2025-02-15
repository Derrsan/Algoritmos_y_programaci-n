Algoritmo Sueldo_Trabajador
	Escribir "Ingrese nombre del trabajador: "
	Leer nombre
	Escribir "Ingrese horas ordinarias trabajadas: "
	Leer horas_ordinarias
	Escribir "Ingrese el valor por hora ordinaria: "
	Leer Valor_hora
	Escribir "Ingrese el número de horas extras: "
	Leer horas_extras
	Escribir "Ingrese cantidad de hijos: "
	Leer hijos
	
	sueldo_base=horas_ordinarias*Valor_hora
	pago_extras=horas_extras*(Valor_hora*1.25)
	
	asignaciones=pago_extras+250000+(173000*hijos)+180000
	
	deducciones=(sueldo_base*0.05)+(sueldo_base*0.02)+(sueldo_base*0.07)
	
	sueldo_neto=sueldo_base+asignaciones-deducciones
	
	Escribir "El pago del mes de Diciembre son: Asignaciones:",asignaciones," COP","; Deducciones:",deducciones," COP", "; Sueldo neto:", sueldo_neto," COP"
	
	
FinAlgoritmo