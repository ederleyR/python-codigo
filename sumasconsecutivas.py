num1= int(input("ingrese un numero: "))
num2= int(input("ingrese otro numero: "))
suma = num1+num2
while True:
    siyno= int(input("quieres agregar otro numero\n1.si\n2.no\n"))
    match siyno:
        case 1:
            agregado= int(input("numero: "))
            suma = suma+agregado
        case 2:
            print(f"el resultado es {suma}")
            break