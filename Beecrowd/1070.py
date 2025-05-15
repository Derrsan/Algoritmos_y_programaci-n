listas = []

numeros = int(input())

for i in range(6):
    if numeros % 2 == 0:
        numeros += 1
    listas.append(numeros)
    numeros += 2  
for valor in listas:
    print(valor)