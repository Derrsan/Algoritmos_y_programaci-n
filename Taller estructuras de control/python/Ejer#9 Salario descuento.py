Horas_trabajadas = int(input("Ingrese horas trabajadas: ")) 
Precio_hora = int(input("Ingrese el precio por hora: "))
Sueldo_base = Horas_trabajadas*Precio_hora
Descuento = Sueldo_base*0.20
Salario_neto = Sueldo_base-Descuento
print("El salario neto es: ", Salario_neto)
