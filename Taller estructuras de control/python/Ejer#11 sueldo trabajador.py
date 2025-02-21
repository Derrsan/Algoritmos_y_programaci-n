nombre = input("Ingrese nombre del trabajador: ")
horas_ordinarias = int(input("Ingrese horas ordinarias trabajadas: "))
Valor_hora =int(input("Ingrese el valor por hora ordinaria: "))
horas_extras= int(input("Ingrese el número de horas extras: "))
hijos = int(input("Ingrese cantidad de hijos: "))
sueldo_base=horas_ordinarias*Valor_hora
pago_extras=horas_extras*(Valor_hora*1.25)
asignaciones=pago_extras+250000+(173000*hijos)+180000
deducciones=(sueldo_base*0.05)+(sueldo_base*0.02)+(sueldo_base*0.07)
sueldo_neto=sueldo_base+asignaciones-deducciones
print("El pago del mes de Diciembre son: Asignaciones:",asignaciones," COP","; Deducciones:",deducciones," COP", "; Sueldo neto:", sueldo_neto," COP")
