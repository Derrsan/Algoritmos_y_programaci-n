Inversion = int(input("Ingrese inversion"))
Intereses = 4 # interes del 4%
Rentabilidad = (Inversion * Intereses)/100
Total = Rentabilidad+Inversion
if(Rentabilidad>100000):
    print("Saldo en cuenta bancaria va hacer de:", Total)
else:
    print("No quiero invertir")   


