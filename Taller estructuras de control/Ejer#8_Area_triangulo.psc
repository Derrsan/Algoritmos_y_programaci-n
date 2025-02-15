Algoritmo Area_Triangulo
    Escribir "Ingrese la longitud del lado a: "
    Leer a
    Escribir "Ingrese la longitud del lado b: "
    Leer b
    Escribir "Ingrese la longitud del lado c: "
    Leer c
    s=(a+b+c)/2
    Area=Raiz(s*(s-a)*(s-b)*(s-c))
    Escribir "El área del triángulo es: ",Area
FinAlgoritmo