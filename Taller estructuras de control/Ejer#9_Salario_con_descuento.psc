Algoritmo Calculo_salario_con_impuesto
    Escribir "Ingrese horas trabajadas: "
    Leer Horas_trabajadas
    Escribir "Ingrese el precio por hora: "
    Leer Precio_hora
    Sueldo_base = Horas_trabajadas*Precio_hora
    Descuento = Sueldo_base*0.20
    Salario_neto = Sueldo_base-Descuento
    Escribir "El salario neto es: ", Salario_neto
FinAlgoritmo