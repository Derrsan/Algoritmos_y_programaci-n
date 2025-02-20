# Pedir al usuario el capital inicial
Inversion = float(input("Ingrese el dinero a invertir: "))

# Calcular la ganancia
Interes = Inversion*0.02

# Calcular el total después de un mes
Ganancia_al_mes = Inversion+Interes

# Mostrar el resultado
print("Su ganancia despues de un mes es:", Ganancia_al_mes, " COP")
