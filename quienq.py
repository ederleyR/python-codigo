import random
preguntas = {
  1: [
      {'pregunta': "¿De qué color es una zanahoria común?",
       'opciones': ["A. Azul", "B. Naranja", "C. Amarillo", "D. Verde"], 
       'respuesta': "B. Naranja",
       'incorrectas': ["A. Azul", "C. Amarillo", "D. Verde"]},
      {'pregunta': "¿Qué usamos para ver con nuestros ojos si está oscuro?", 
       'opciones': ["A. Lámpara", "B. Almohada", "C. Televisor", "D. Paraguas"], 
       'incorrectas':["B. Almohada", "C. Televisor", "D. Paraguas"],
       'respuesta': "A. Lámpara"
       }
  ],
  2: [
      {'pregunta': "¿Cuántos minutos tiene una hora?", 
       'opciones': ["A. 30", "B. 45", "C. 60", "D. 90"], 
       'respuesta': "C. 60",
       'incorrectas': ["A. 30", "B. 45", "D. 90"]},

      {'pregunta': "¿Qué usamos para cortar papel?", 
       'opciones': ["A. Cuchara", "B. Tijeras", "C. Pegamento", "D. Pincel"], 
       'respuesta': "B. Tijeras",
       'incorrectas':["A. Cuchara", "B. Tijeras", "C. Pegamento", "D. Pincel"]}
  ],
  3: [
      {'pregunta': "¿Qué planeta está más cerca del Sol?", 
       'opciones': ["A. Venus", "B. Marte", "C. Mercurio", "D. Saturno"], 
       'respuesta': "C. Mercurio",
       'incorrectas':["A. Venus", "B. Marte", "D. Saturno"]},

      {'pregunta': "¿Qué parte del cuerpo usamos para escuchar?", 
       'opciones': ["A. Manos", "B. Nariz", "C. Orejas", "D. Pies"], 
       'respuesta': "C. Orejas",
       'incorrectas':["A. Manos", "B. Nariz", "D. Pies"]}
  ],
  4: [
      {'pregunta': "¿Quién fue el primer ser humano en viajar al espacio?", 
       'opciones': ["A. Neil Armstrong", "B. Yuri Gagarin", "C. Buzz Aldrin", "D. Alan Shepard"], 
       'respuesta': "B. Yuri Gagarin",
       'incorrectas':["A. Neil Armstrong", "C. Buzz Aldrin", "D. Alan Shepard"]},

      {'pregunta': "¿Qué continente es el más grande del mundo?", 
       'opciones': ["A. Europa", "B. América", "C. Asia", "D. África"], 
       'respuesta': "C. Asia",
       'incorrectas':["A. Europa", "B. América", "D. África"]}
  ],
  5: [
      {'pregunta': "¿Qué tipo de animal es una ballena?", 
       'opciones': ["A. Reptil", "B. Mamífero", "C. Ave", "D. Pez"], 
       'respuesta': "B. Mamífero",
       'incorrectas':["A. Reptil", "C. Ave", "D. Pez"]},

      {'pregunta': "¿Cuál es el número romano que representa al 100?", 
       'opciones': ["A. L", "B. C", "C. D", "D. M"], 
       'respuesta': "B. C",
       'incorrectas':["A. L", "C. D", "D. M"]}
  ],
  6: [
      {'pregunta': "¿Qué país inventó el papel?", 
       'opciones': ["A. Egipto", "B. China", "C. Grecia", "D. India"], 
       'respuesta': "B. China",
       'incorrectas':["A. Egipto", "C. Grecia", "D. India"]},

      {'pregunta': "¿En qué ciudad está el Coliseo?", 
       'opciones': ["A. Atenas", "B. París", "C. Roma", "D. Londres"], 
       'respuesta': "C. Roma",
       'incorrectas':["A. Atenas", "B. París", "D. Londres"]}
  ],
  7: [
      {'pregunta': "¿Cuál es el principal gas que causa el efecto invernadero?", 
       'opciones': ["A. Nitrógeno", "B. Oxígeno", "C. Dióxido de carbono", "D. Helio"], 
       'respuesta': "C. Dióxido de carbono",
       'incorrectas':["A. Nitrógeno", "B. Oxígeno", "D. Helio"]},

      {'pregunta': "¿Cuál es el río más largo del mundo?", 
       'opciones': ["A. Amazonas", "B. Nilo", "C. Yangtsé", "D. Misisipi"], 
       'respuesta': "A. Amazonas",
       'incorrectas':["B. Nilo", "C. Yangtsé", "D. Misisipi"]}
    ],
  8: [
      {'pregunta': "¿Qué científico descubrió la penicilina?", 
       'opciones': ["A. Albert Einstein", "B. Isaac Newton", "C. Alexander Fleming", "D. Marie Curie"], 
       'respuesta': "C. Alexander Fleming",
       'incorrectas':["A. Albert Einstein", "B. Isaac Newton"]},

      {'pregunta': "¿Qué continente no tiene desiertos?", 
       'opciones': ["A. Asia", "B. Europa", "C. África", "D. Oceanía"], 
       'respuesta': "B. Europa",
       'incorrectas':["A. Asia", "C. África", "D. Oceanía"]}
  ],
  9: [
      {'pregunta': "¿Qué autor escribió *Crimen y castigo*?", 
       'opciones': ["A. Fiódor Dostoyevski", "B. León Tolstói", "C. Franz Kafka", "D. Anton Chéjov"], 
       'respuesta': "A. Fiódor Dostoyevski",
       'incorrectas':["B. León Tolstói", "C. Franz Kafka", "D. Anton Chéjov"]},

      {'pregunta': "¿En qué año cayó el Muro de Berlín?", 
       'opciones': ["A. 1985", "B. 1987", "C. 1989", "D. 1991"], 
       'respuesta': "C. 1989",
       'incorrectas':["B. 1987", "C. 1989", "D. 1991"]}
  ],
  10: [
      {'pregunta': "¿Qué unidad se usa para medir la intensidad de una corriente eléctrica?", 
       'opciones': ["A. Voltios", "B. Ohmios", "C. Amperios", "D. Vatios"], 
       'respuesta': "C. Amperios",
       'incorrectas':["A. Voltios", "B. Ohmios", "D. Vatios"]},

      {'pregunta': "¿Qué científico propuso la mecánica cuántica?", 
       'opciones': ["A. Max Planck", "B. Niels Bohr", "C. Werner Heisenberg", "D. Albert Einstein"], 
       'respuesta': "A. Max Planck",
       'incorrectas':["B. Niels Bohr", "C. Werner Heisenberg", "D. Albert Einstein"]}
  ]
}
comodines = {1:["1.llama a un amigo"],
             2:["2.cambio de pregunta"],
             3:["3.50/50"],
             4:["4.NO"]}
ganar= 0
for nivel, lista_preguntas in preguntas.items():
    print(preguntas[nivel][0]["pregunta"])
    print(preguntas[nivel][0]["opciones"])
    print(comodines)
    comodin = int(input("quieres usar algun comodin?: "))
    match comodin :
        case 4:
            pregunta=input("¿cual es la respuesta correcta?: ")
            if pregunta == preguntas[nivel][0]["respuesta"]:
                print("correcto")
            else:
                print("incorrecto PERDISTE")
                break
        case 1:
                respuesta_Aleatoria= random.choice(preguntas[nivel][0]["opciones"])
                print("juan: hola amigo yo digo que elijas",respuesta_Aleatoria)
                del comodines[1]
                print(comodines)
                comodin = int(input("quieres usar otro comodin?: "))
                match comodin:
                    case 2:
                        print(preguntas[nivel][1]["pregunta"])
                        print(preguntas[nivel][1]["opciones"])
                        del comodines[2]
                        print(comodines)
                        comodin = int(input("quieres usar tu ultimo comodin?: "))
                        match comodin:
                            case 3:
                                pregunta_aletoria= random.choice(preguntas[nivel][1]["incorrectas"])
                                print(preguntas[nivel][1]["respuesta"],pregunta_aletoria)
                                pregunta1=input("¿cual es la respuesta correcta?: ")
                                del comodines[3]
                                if pregunta1 == preguntas[nivel][1]["respuesta"]:
                                    print("correcto")
                                else:
                                    print("incorrecto PERDISTE")
                                    break
                            case 4:
                                pregunta1 = input("¿cual es la respuesta correcta?: ")
                                if pregunta1 == preguntas[nivel][1]["respuesta"]:
                                    print("correcto")
                                else:
                                    print("incorrecto PERDISTE")
                                    break
                    case 3:
                        pregunta_aletoria= random.choice(preguntas[nivel][0]["incorrectas"])
                        print(preguntas[nivel][0]["respuesta"],pregunta_aletoria)
                        del comodines[3]
                        print(comodines)
                        comodin = int(input("quieres usar tu ultimo comodin?: "))
                        match comodin:
                            case 2:
                                print(preguntas[nivel][1]["pregunta"])
                                print(preguntas[nivel][1]["opciones"])
                                del comodines[2]
                                pregunta1 = input("¿cual es la respuesta correcta?: ")                              
                                if pregunta1 == preguntas[nivel][1]["respuesta"]:
                                    print("correcto")
                                else:
                                    print("incorrecto PERDISTE")
                                    break
                            case 4:
                                pregunta=input("¿cual es la respuesta correcta?: ")
                                if pregunta == preguntas[nivel][0]["respuesta"]:
                                    print("correcto")
                                else:
                                    print("incorrecto PERDISTE")
                                    break
                    case 4:         
                        pregunta=input("¿cual es la respuesta correcta?: ")
                        if pregunta == preguntas[nivel][0]["respuesta"]:
                            print("correcto")
                        else:
                            print("incorrecto PERDISTE")
                            break
        case 2:
                print(preguntas[nivel][1]["pregunta"])
                print(preguntas[nivel][1]["opciones"])
                del comodines[2]
                print(comodines)
                comodin = int(input("quieres usar otro comodin?: "))
                match comodin:
                    case 4:
                        pregunta1 = input("¿cual es la respuesta correcta?: ")
                        if pregunta1 == preguntas[nivel][1]["respuesta"]:
                            print("correcto")
                        else:
                            print("incorrecto PERDISTE")
                            break
                    case 1:
                        respuesta_Aleatoria= random.choice(preguntas[nivel][1]["opciones"])
                        print("juan: hola amigo yo digo que elijas",respuesta_Aleatoria)
                        del comodines[1]
                        print(comodines)
                        comodin = int(input("quieres usar otro comodin?: "))
                        match comodin:
                            case 4:
                                pregunta1 = input("cual es la correcta: ")
                                if pregunta1 == preguntas[nivel][1]["respuesta"]:
                                    print("correcto")
                                else:
                                    print("incorrecto PERDISTE")
                                    break
                            case 3:
                                pregunta_aletoria= random.choice(preguntas[nivel][0]["incorrectas"])
                                print(preguntas[nivel][1]["respuesta"],pregunta_aletoria)
                                del comodines[3]
                                pregunta1 = input("cual es la correcta: ")
                                if pregunta1 == preguntas[nivel][1]["respuesta"]:
                                    print("correcto")
                                else:
                                    print("incorrecto PERDISTE")
                                    break
                    case 3:
                        pregunta_aletoria= random.choice(preguntas[nivel][1]["incorrectas"])
                        print(preguntas[nivel][1]["respuesta"],pregunta_aletoria)
                        del comodines[3]
                        print(comodines)
                        comodin = int(input("quieres usar tu ultimo comodin?: "))
                        match comodin:
                            case 1:
                                respuesta_Aleatoria= random.choice(preguntas[nivel][1]["opciones"])
                                print("juan: hola amigo yo digo que elijas",respuesta_Aleatoria)
                                pregunta1 = input("cual es la correcta: ")
                                if pregunta1 == preguntas[nivel][1]["respuesta"]:
                                    print("correcto")
                                else:
                                    print("incorrecto PERDISTE")
                                    break
                            case 4:
                                pregunta1 = input("cual es la correcta: ")
                                if pregunta1 == preguntas[nivel][1]["respuesta"]:
                                    print("correcto")
                                else:
                                    print("incorrecto PERDISTE")
                                    break                 
        case 3:
                pregunta_aletoria= random.choice(preguntas[nivel][0]["incorrectas"])
                print(preguntas[nivel][0]["respuesta"],pregunta_aletoria)
                del comodines[3]
                print(comodines)
                comodin = int(input("quieres usar tu ultimo comodin?: "))
                match comodin:
                    case 4:
                        pregunta=input("¿cual es la respuesta correcta?: ")
                        if pregunta == preguntas[nivel][0]["respuesta"]:
                            print("correcto")
                        else:
                            print("incorrecto PERDISTE")
                            break
                    case 1:
                        respuesta_Aleatoria= random.choice(preguntas[nivel][0]["opciones"])
                        print("juan: hola amigo yo digo que elijas",respuesta_Aleatoria)
                        del comodines[1]
                        print(comodines)
                        comodin = int(input("quieres usar otro comodin?: "))
                        match comodin:
                            case 4:
                                pregunta=input("¿cual es la respuesta correcta?: ")
                                del comodines[3]
                                if pregunta == preguntas[nivel][0]["respuesta"]:
                                    print("correcto")
                                else:
                                    print("incorrecto PERDISTE")
                                    break
                            case 2:
                                print(preguntas[nivel][1]["pregunta"])
                                print(preguntas[nivel][1]["opciones"])
                                pregunta1 = input("¿cual es la respuesta correcta?: ")
                                del comodines[2]
                                if pregunta1 == preguntas[nivel][1]["respuesta"]:
                                    print("correcto")
                                else:
                                    print("incorrecto PERDISTE")
                                    break
                    case 2:
                         print(preguntas[nivel][1]["pregunta"])
                         print(preguntas[nivel][1]["opciones"])
                         del comodines[2]
                         print(comodines)
                         comodin = int(input("quieres usar tu ultimo comodin?: "))
                         match comodin:
                            case 3:
                                pregunta_aletoria= random.choice(preguntas[nivel][1]["incorrectas"])
                                print(preguntas[nivel][1]["respuesta"],pregunta_aletoria)
                                pregunta1=input("¿cual es la respuesta correcta?: ")
                                del comodines[3]
                                pregunta1 = input("¿cual es la respuesta correcta?: ")
                                if pregunta1 == preguntas[nivel][1]["respuesta"]:
                                    print("correcto")
                                else:
                                    print("incorrecto PERDISTE")
                                    break
                            case 4:
                                pregunta1 = input("¿cual es la respuesta correcta?: ")
                                if pregunta1 == preguntas[nivel][1]["respuesta"]:
                                    print("correcto")
                                else:
                                    print("incorrecto PERDISTE")
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