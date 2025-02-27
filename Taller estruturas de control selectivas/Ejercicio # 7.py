Distancia = int(input("Ingrese distancia recorrida:"))
if(Distancia<300):
    print("Cancele $50.000 COP")
elif(300<Distancia<1000):
    Extra = Distancia - 300
    Total = 70000 + (30000*Extra)
    print("cancele",Total, "COP")  
elif(Distancia>1000):
    Extra = Distancia - 1000
    Total = 150000+(9000*Extra)
    print("Cancele", Total, "COP")      