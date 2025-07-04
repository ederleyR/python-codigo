print("bienvenido al tribunal de impuestos")

edad = int(input("ingrese su edad : "))

ingresos = int(input("ingrese sus ingresos : "))

ingresos_minimos = int(4270500)

if edad < 18:
    print("no puedes ingresar nene ")
else:
    if ingresos <= ingresos_minimos:
        print("debes tributar")
    else:
        print("no debes tributar")
