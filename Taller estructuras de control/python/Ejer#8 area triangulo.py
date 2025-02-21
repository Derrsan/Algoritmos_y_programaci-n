a = int(input("Ingrese la longitud del lado a: "))
b = int(input("Ingrese la longitud del lado b: "))
c = int(input("Ingrese la longitud del lado c: "))
s=(a+b+c)/2
Area=(s*(s-a)*(s-b)*(s-c))**1/2
print("El área del triángulo es: ",Area)
