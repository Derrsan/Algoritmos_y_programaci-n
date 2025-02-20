A= int(input("ingrese el valor de A "))
B= int(input("ingrese el valor de B "))
C= int(input("ingrese el valor de C "))
D= int(input("ingrese el valor de D "))

Condicion_1 = (A-C)**2
Condicion_2 = ((A-B)**3/D)

if(D==0):
    Valor = Condicion_1
elif(D>0):
    Valor = Condicion_2

print("el resultado es igual a",Valor)        
