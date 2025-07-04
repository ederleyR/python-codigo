numero = int(input("introduce un numero: "))
ancho = numero
for i in range(1,numero+1):
    print(("*"*i).rjust(ancho))