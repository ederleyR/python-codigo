# En una máquina expendedora, los usuarios pueden seleccionar bebidas múltiples veces: 1. café ($3.000), 2. té ($2.500) o 3. jugo ($3.500); 
# cada vez que el usuario ingresa una opción(1, 2, o 3), se muestra el valor del producto y se acumula el total a pagar; el programa termina cuando el usuario ingresa el 
# número 0; usar un bucle while, match-case y break.

total = 0

print("Bienvenido a mi tienda de objetos raros elija un objeto con un precio unico \nObjetos\n\t1- Flecha stand($3.000)\n\t2- Mascara de piedra($2.500)\n\t3- Piedra de jade($3.500)\n\t4-leche de mipalo($1.000)\n\t elije 0 para terminar la compra\n")

while True:
    
    objeto_opcion = int(input("dijite alguna de las opciones: "))

    match objeto_opcion :

        case 1 : 
            print("has seleccionado la fleha stand con un valor de $3.000")
            total += 3000  
        case 2 :
            print("has seleccionado la mascara de piedra con un valor de $2.500")
            total += 2500
        case 3:
            print("has seleccionado la Piedra de jade con un valor $3.500")
            total += 3500
        case 4:
            print("has seleccionado la leche de mipalo con un costo de $1.000")
            total += 1000   
        case 0:
            print("gracias por su compra")
            break
        case _:
            print("no se de que hablas")

print("total a pagar",total)
