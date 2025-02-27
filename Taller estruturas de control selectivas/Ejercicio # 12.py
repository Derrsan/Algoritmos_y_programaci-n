def desglose_monedas(cantidad):
    # Desglosamos los billetes y monedas
    if cantidad >= 100000:
        print(f"{cantidad // 100000} billetes de 100.000 COP")
        cantidad %= 100000
    
    if cantidad >= 50000:
        print(f"{cantidad // 50000} billetes de 50.000 COP")
        cantidad %= 50000
    
    if cantidad >= 20000:
        print(f"{cantidad // 20000} billetes de 20.000 COP")
        cantidad %= 20000
    
    if cantidad >= 10000:
        print(f"{cantidad // 10000} billetes de 10.000 COP")
        cantidad %= 10000
    
    if cantidad >= 5000:
        print(f"{cantidad // 5000} billetes de 5.000 COP")
        cantidad %= 5000
    
    if cantidad >= 2000:
        print(f"{cantidad // 2000} billetes de 2.000 COP")
        cantidad %= 2000
    
    if cantidad >= 1000:
        print(f"{cantidad // 1000} billetes de 1.000 COP")
        cantidad %= 1000
    
    if cantidad >= 500:
        print(f"{cantidad // 500} monedas de 500 COP")
        cantidad %= 500
    
    if cantidad >= 200:
        print(f"{cantidad // 200} monedas de 200 COP")
        cantidad %= 200
    
    if cantidad >= 100:
        print(f"{cantidad // 100} monedas de 100 COP")
        cantidad %= 100
    
    if cantidad >= 50:
        print(f"{cantidad // 50} monedas de 50 COP")
        cantidad %= 50

# Ejemplo de uso
cantidad = int(input("Ingrese la cantiad:"))  # Monto a desglosar
desglose_monedas(cantidad)
