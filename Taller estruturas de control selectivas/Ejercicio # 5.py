Sueldo=float(input("Ingrese el sueldo del trabajador: "))
n=input("Ingrese Ventas de los tres departamentos: ")
(a,b,c)=n.split(" ")
Dep_uno = float(a)
Dep_dos = float(b)
Dep_tres = float(c)

Importe_global = Dep_uno + Dep_dos + Dep_tres
Cantidad_extra = Importe_global * 0.33
if(Cantidad_extra<Dep_uno):
    Extra = Sueldo * 0.20
    Sueldo_extra = Extra + Sueldo
    print("El departamento uno gana a final de mes:", Sueldo_extra, "demas departamentos se mantienen con el sueldo base")
if(Cantidad_extra<Dep_dos):
    Extra = Sueldo * 0.20
    Sueldo_extra = Extra + Sueldo
    print("El departamento dos gana a final de mes:", Sueldo_extra, "demas departamentos se mantienen con el sueldo base")
if(Cantidad_extra<Dep_tres):
    Extra = Sueldo * 0.20
    Sueldo_extra = Extra + Sueldo
    print("El departamento tres gana a final de mes:", Sueldo_extra, "demas departamentos se mantienen con el sueldo base")
else:
    print("Ninguno gana extras")            

