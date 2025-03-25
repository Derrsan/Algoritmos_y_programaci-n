N_estudiantes = int(input("Escriba numeros de estudiantes"))
max_altura = 0
for i in range(1,N_estudiantes+1):
    altura = float(input("Ingrese la altura de los estudiantes:"))
    if altura > max_altura:
        max_altura = altura
print(f"la mayor altura es {max_altura}")        

    