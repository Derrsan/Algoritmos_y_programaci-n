dividendo = int(input("ingrese el dividendo"))
divisor = int(input("ingrese el divisor"))
contador = 0
while True:
    dividendo = dividendo-divisor
    contador = contador +1
    if dividendo<divisor:
        break
print(f"Residuo:{dividendo}")
print(f"Cociente:{contador}")