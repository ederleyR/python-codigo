import random
puntaje1 = 0
puntaje2 = 0
ronda = 0
opciones = ["piedra","papel","tigera"]
print("bienvenido a piedra papel y tijera")
juegos = int(input("agrege la cantidad de veces que quieres jugar: "))

while True:
    if ronda == juegos:
        print("gracias por jugar")
        break
    movimientos = input("que vas a jugar ? : ")
    eleccion = random.choice(opciones)
    print("jugador elejiste",movimientos)
    print("maquina eligio",eleccion)
    if movimientos == eleccion:
        print("empate")
        print("jugador tiene :",puntaje1,"puntos el bot : ",puntaje2,"puntos")
        ronda += 1
        print(ronda,"de",juegos)
    elif (movimientos == "piedra" and eleccion == "tijera") \
     or (movimientos == "papel" and eleccion == "piedra") \
     or (movimientos == "tijera" and eleccion == "papel"):
        print("ganaste")
        puntaje1 +=1
        print("jugador tiene :",puntaje1,"puntos el bot : ",puntaje2,"puntos")
        ronda +=1
        print(ronda,"de",juegos)
    else:
        print("el bot gana")
        puntaje2 +=1
        print("jugador tiene :",puntaje1,"puntos el bot : ",puntaje2,"puntos")
        ronda += 1
        print("ronda: ",ronda,"de",juegos)
        
    



