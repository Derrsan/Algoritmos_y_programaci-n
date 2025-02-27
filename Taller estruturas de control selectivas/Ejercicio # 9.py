Nombre = input("Ingrese nombre de comprador")
Compra = float(input("Ingrese el valor de la compra"))
if(Compra<50000):
    print("No aplica descuento")
elif(50000<Compra<100000):
    Descuento = Compra * 0.5
    TotalPagar = Compra - Descuento
    print(Nombre + " su compra fue de",Compra, " y su descuento fue de ", Descuento,"y debe pagar: ",TotalPagar, "COP")    
elif(100000<Compra<700000):
    Descuento = Compra * 0.11
    TotalPagar = Compra - Descuento
    print(Nombre + " su compra fue de",Compra, " y su descuento fue de ", Descuento,"y debe pagar: ",TotalPagar, "COP")        
elif(700000<Compra<1500000):
    Descuento = Compra * 0.18
    TotalPagar = Compra - Descuento
    print(Nombre + " su compra fue de",Compra, " y su descuento fue de ", Descuento,"y debe pagar: ",TotalPagar, "COP")    
elif(Compra>1500000):
    Descuento = Compra * 0.25
    TotalPagar = Compra - Descuento
    print(Nombre + " su compra fue de",Compra, " y su descuento fue de ", Descuento,"y debe pagar: ",TotalPagar, "COP")   