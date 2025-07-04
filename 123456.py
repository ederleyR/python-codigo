#153
#370
#407
#1634

numero = input("ingresa un numero narcizista: ")

numeral = len(numero)

if numeral < 3:
    numeros1 = int(numero[0])
    numeros2 = int(numero[1])
    numeros3 = int(numero[2])
    numeros4 = int(numero[3])

    num1=(numeros1*pow)
    num2=(numeros2*pow)
    num3=(numeros3*pow)
    num4=(numeros4*pow)

    print("primera elevacion",num1)
    print("segunda elevacion",num2)
    print("tercera elevacion",num3)
    print("cuarta elevacion",num4)

    n = (num1+num2+num3+num4)
    print("el numero final es", n)
    if numero == n:
        print(n,"es un numero narzicista")
    else:
        print(n,"no es numero narzicista")
