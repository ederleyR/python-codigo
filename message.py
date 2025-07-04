import random

# Diccionario de preguntas y respuestas
preguntas = {
    1: [
        {'pregunta': "¿De qué color es una zanahoria común?",
         'opciones': ["A. Azul", "B. Naranja", "C. Amarillo", "D. Verde"],
         'respuesta': "B. Naranja"},

        {'pregunta': "¿Qué usamos para ver con nuestros ojos si está oscuro?",
         'opciones': ["A. Lámpara", "B. Almohada", "C. Televisor", "D. Paraguas"],
         'respuesta': "A. Lámpara"}
    ],
    2: [
        {'pregunta': "¿Cuántos minutos tiene una hora?",
         'opciones': ["A. 30", "B. 45", "C. 60", "D. 90"],
         'respuesta': "C. 60"},

        {'pregunta': "¿Qué usamos para cortar papel?",
         'opciones': ["A. Cuchara", "B. Tijeras", "C. Pegamento", "D. Pincel"],
         'respuesta': "B. Tijeras"}
    ],
    3: [
        {'pregunta': "¿Qué planeta está más cerca del Sol?",
         'opciones': ["A. Venus", "B. Marte", "C. Mercurio", "D. Saturno"],
         'respuesta': "C. Mercurio"},

        {'pregunta': "¿Qué parte del cuerpo usamos para escuchar?",
         'opciones': ["A. Manos", "B. Nariz", "C. Orejas", "D. Pies"],
         'respuesta': "C. Orejas"}
    ],
    4: [
        {'pregunta': "¿Quién fue el primer ser humano en viajar al espacio?",
         'opciones': ["A. Neil Armstrong", "B. Yuri Gagarin", "C. Buzz Aldrin", "D. Alan Shepard"],
         'respuesta': "B. Yuri Gagarin"},

        {'pregunta': "¿Qué continente es el más grande del mundo?",
         'opciones': ["A. Europa", "B. América", "C. Asia", "D. África"],
         'respuesta': "C. Asia"}
    ]
}

comodines = {
    1: ["1.llama a un amigo"],
    2: ["2.cambio de pregunta"],
    3: ["3.50/50"],
    4: ["4.NO"]
}

# Función para obtener respuestas incorrectas automáticamente
def obtener_respuestas_incorrectas(opciones, respuesta_correcta):
    return [opcion for opcion in opciones if opcion != respuesta_correcta]

ganar = 0

for nivel, lista_preguntas in preguntas.items():
    print(preguntas[nivel][0]["pregunta"])
    print(preguntas[nivel][0]["opciones"])
    print(comodines)
    comodin = int(input("¿Quieres usar algún comodín?: "))

    match comodin:
        case 4:
            pregunta = input("¿Cuál es la respuesta correcta?: ")
            if pregunta == preguntas[nivel][0]["respuesta"]:
                print("Correcto")
            else:
                print("Incorrecto. PERDISTE")
                break

        case 1:
            respuesta_aleatoria = random.choice(preguntas[nivel][0]["opciones"])
            print("Juan: hola amigo, yo digo que elijas", respuesta_aleatoria)
            del comodines[1]
            print(comodines)
            comodin = int(input("¿Quieres usar otro comodín?: "))

            match comodin:
                case 2:
                    print(preguntas[nivel][1]["pregunta"])
                    print(preguntas[nivel][1]["opciones"])
                    del comodines[2]
                    print(comodines)
                    comodin = int(input("¿Quieres usar tu último comodín?: "))

                    match comodin:
                        case 3:
                            opciones = preguntas[nivel][1]["opciones"]
                            correcta = preguntas[nivel][1]["respuesta"]
                            incorrecta = random.choice(obtener_respuestas_incorrectas(opciones, correcta))
                            print(correcta, incorrecta)
                            respuesta_usuario = input("¿Cuál es la respuesta correcta?: ")
                            del comodines[3]
                            if respuesta_usuario == correcta:
                                print("Correcto")
                            else:
                                print("Incorrecto. PERDISTE")
                                break
                        case 4:
                            respuesta_usuario = input("¿Cuál es la respuesta correcta?: ")
                            if respuesta_usuario == preguntas[nivel][1]["respuesta"]:
                                print("Correcto")
                            else:
                                print("Incorrecto. PERDISTE")
                                break

                case 3:
                    opciones = preguntas[nivel][0]["opciones"]
                    correcta = preguntas[nivel][0]["respuesta"]
                    incorrecta = random.choice(obtener_respuestas_incorrectas(opciones, correcta))
                    print(correcta, incorrecta)
                    del comodines[3]
                    print(comodines)
                    comodin = int(input("¿Quieres usar tu último comodín?: "))

                    match comodin:
                        case 2:
                            print(preguntas[nivel][1]["pregunta"])
                            print(preguntas[nivel][1]["opciones"])
                            del comodines[2]
                            respuesta_usuario = input("¿Cuál es la respuesta correcta?: ")
                            if respuesta_usuario == preguntas[nivel][1]["respuesta"]:
                                print("Correcto")
                            else:
                                print("Incorrecto. PERDISTE")
                                break
                        case 4:
                            respuesta_usuario = input("¿Cuál es la respuesta correcta?: ")
                            if respuesta_usuario == preguntas[nivel][0]["respuesta"]:
                                print("Correcto")
                            else:
                                print("Incorrecto. PERDISTE")
                                break
    print("ganaste 100.000")
    ganar+= 100000
    retirarse =int(input(f"quieres retirarte con el valor de {ganar} pesos ? (1.SI 2.NO): "))
    match retirarse :
        case 1:
                print(f"gracias por jugar quien quiere ser millonario, ganaste {ganar} pesos ")
                break
        case 2:
                print("Bien a seguir jugando")  