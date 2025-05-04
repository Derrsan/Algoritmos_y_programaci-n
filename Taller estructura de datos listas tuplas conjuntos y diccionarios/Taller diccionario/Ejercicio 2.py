#Recorre un diccionario y crea una lista solo con los valores que contiene, sin añadir valores duplicados.
Lista = []
Dic = {'Mikel': 3, 'Ane': 8, 'Amaia': 12, 'Unai': 5, 'Jon': 8, 'Ainhoa': 7,'Maite': 5}
for i in Dic.values():
    Lista.append(i)
NuevaLista = list(dict.fromkeys(Lista))
print(NuevaLista)


# Resultado: [3, 8, 12, 5, 7]