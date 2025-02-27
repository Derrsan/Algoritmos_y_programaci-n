Categoria = int(input("Ingrese la categoria"))
SalarioUno = 5000000
SalarioDos = 4300000
SalarioTres = 3600000
SalarioCuatro = 2000000
SalarioCinco = 900000
if(Categoria == 1):
    Aumento = SalarioUno * 0.1
    SalarioTotal = Aumento + SalarioUno
    print("El Salario de la categoria ",Categoria, "es ",SalarioTotal)
elif(Categoria == 2):
    Aumento = SalarioDos * 0.15
    SalarioTotal = Aumento + SalarioDos
    print("El Salario de la categoria ",Categoria, "es ",SalarioTotal)
elif(Categoria == 3):
    Aumento = SalarioTres * 0.2
    SalarioTotal = Aumento + SalarioTres
    print("El Salario de la categoria ",Categoria, "es ",SalarioTotal)
elif(Categoria == 4):
    Aumento = SalarioCuatro * 0.4
    SalarioTotal = Aumento + SalarioCuatro
    print("El Salario de la categoria ",Categoria, "es ",SalarioTotal)
elif(Categoria == 5):
    Aumento = SalarioUno * 0.6
    SalarioTotal = Aumento + SalarioCinco
    print("El Salario de la categoria ",Categoria, "es ",SalarioTotal)
            