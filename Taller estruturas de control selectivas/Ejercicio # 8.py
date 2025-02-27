P = int(input("Ingrese dato para P "))
Q = int(input("Ingrese dato para Q "))

if((P**3)+(Q**4)-2*(P**2)>680):
    print("Los datos" + str(P) + "y" + str(Q) + "satisfacen la expresion ")
else:
    print("Los datos " + str(P) + " y " +str(Q) + " no satisfacen la expresion ")
