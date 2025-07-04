nombre = input("ingrese su nombre : ")
genero = input("ingrese su genero : " )

primera_letra = nombre [0].upper ()

if genero == ("M"):
    print("usted es mujer")
    if primera_letra <= ("N"): 
       print("usted es del grupo A")
    else: 
       print("usted es del grupo B")
else: 
    print("usted es hombre") 
    if primera_letra <= ("M"): 
        print(" usted es del grupo A") 
    else: 
        print("usted es del grupo B")
