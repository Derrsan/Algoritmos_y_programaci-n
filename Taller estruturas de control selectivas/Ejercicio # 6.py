Datos=input("Ingrese datos: ")
(a,b,c,d)=Datos.split(" ")
a = int(a)
b = int(b)
c = int(c)
d = int(d)
N = 1000 * a + 100 * b + 10 * c + d
N_redondeado = (N + 50) // 100 * 100
print(f"El número redondeado es: {N_redondeado}")