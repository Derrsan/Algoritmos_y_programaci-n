valores = []
contador = 0
contador2 = 0

for i in range(6):
    numero = float(input())
    if numero > 0:
        contador += 1
        valores.append(numero)
    else:
        contador2 += 1
    
promedio = sum(valores) / contador

print(f"{contador} valores positivos")
print(f"{promedio:.1f}")