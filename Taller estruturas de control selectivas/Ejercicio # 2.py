Sueldo = int(input("Ingrese sueldo del trabajador: "))
if(Sueldo<900000):
    Aumento = Sueldo * 0.15
    Nuevo_sueldo = Sueldo + Aumento 
    
else:
    Aumento = Sueldo * 0.12
    Nuevo_sueldo = Sueldo + Aumento

print("el nuevo sueldo es de:", Nuevo_sueldo)    