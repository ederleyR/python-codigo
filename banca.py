import random
cartas = random.randint(1,13)
banca = random.randint(1,13)
ganadas = 0
perdidas = 0
ganar= 5
perder = 3


while True:

    print("tienes un valor de",cartas,"en tus cartas")
    
    print("quieres continuar ?\n\t1-SI\n\t2-NO\n")
    if ganadas == ganar:
         print("ganaste el juego")
         break
    elif perdidas == perder:
            print("perdiste el juego")
            break   
    continuar = int(input("dijite una opcion: "))

    match continuar:
        case 1:
            if cartas > banca:
                print("usted gano esta ronda")
                ganadas += 1
                print("tienes partidas",perdidas,"perdidas y",ganadas,"ganadas")
                if cartas != banca:
                     cartas= random.randint(1,13)
                     banca= random.randint(1,13)
            else:
                print("ronda perdida")
                perdidas += 1
                print("tienes partidas",perdidas,"perdidas y",ganadas,"ganadas")
                if cartas != banca:
                    cartas= random.randint(1,13)
                    banca= random.randint(1,13)
        case 2:
                print("retirado")
                break
         