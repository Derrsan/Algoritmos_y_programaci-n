Monto_total = int(input("Ingrese el monto total de la compra: "))
if(Monto_total>5000000):
    Diferencia = Monto_total * 0.55
    Prestamo = Monto_total * 0.30
    Credito_fabricante = Monto_total * 0.15
    Interes_credito_fabricante = Credito_fabricante * 0.22
    Pago_interes_fabricante = Interes_credito_fabricante + Credito_fabricante 
    print("Inversion: ", Diferencia, "Prestamo banco:", Prestamo, "Credito a predir al fabricante:", Credito_fabricante, "Pago con interes al fabricante:", Pago_interes_fabricante)
else:
    Diferencia = Monto_total * 0.70
    Credito_fabricante = Monto_total * 0.30
    Interes_credito_fabricante = Credito_fabricante * 0.22
    Pago_interes_fabricante = Interes_credito_fabricante + Credito_fabricante 
    print("Inversion: ", Diferencia, "Credito a predir al fabricante:", Credito_fabricante, "Pago con interes al fabricante:", Pago_interes_fabricante)
