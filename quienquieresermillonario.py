import random
import time
preguntas = {
    1: [
        {'pregunta': "¿De qué color es una zanahoria común?", 'opciones': ["A. Azul", "B. Naranja", "C. Amarillo", "D. Verde"], 'respuesta': "B", 'correcta': "B. Naranja", 'incorrectas': ["A. Azul", "C. Amarillo", "D. Verde"]},
        {'pregunta': "¿Qué usamos para ver con nuestros ojos si está oscuro?", 'opciones': ["A. Lámpara", "B. Almohada", "C. Televisor", "D. Paraguas"], 'respuesta': "A", 'correcta': "A. Lámpara", 'incorrectas': ["B. Almohada", "C. Televisor", "D. Paraguas"]}
    ],
    2: [
        {'pregunta': "¿Cuántos minutos tiene una hora?", 'opciones': ["A. 30", "B. 45", "C. 60", "D. 90"], 'respuesta': "C", 'correcta': "C. 60", 'incorrectas': ["A. 30", "B. 45", "D. 90"]},
        {'pregunta': "¿Qué usamos para cortar papel?", 'opciones': ["A. Cuchara", "B. Tijeras", "C. Pegamento", "D. Pincel"], 'respuesta': "B", 'correcta': "B. Tijeras", 'incorrectas': ["A. Cuchara", "C. Pegamento", "D. Pincel"]}
    ],
    3: [
        {'pregunta': "¿Qué planeta está más cerca del Sol?", 'opciones': ["A. Venus", "B. Marte", "C. Mercurio", "D. Saturno"], 'respuesta': "C", 'correcta': "C. Mercurio", 'incorrectas': ["A. Venus", "B. Marte", "D. Saturno"]},
        {'pregunta': "¿Qué parte del cuerpo usamos para escuchar?", 'opciones': ["A. Manos", "B. Nariz", "C. Orejas", "D. Pies"], 'respuesta': "C", 'correcta': "C. Orejas", 'incorrectas': ["A. Manos", "B. Nariz", "D. Pies"]}
    ],
    4: [
        {'pregunta': "¿Quién fue el primer ser humano en viajar al espacio?", 'opciones': ["A. Neil Armstrong", "B. Yuri Gagarin", "C. Buzz Aldrin", "D. Alan Shepard"], 'respuesta': "B", 'correcta': "B. Yuri Gagarin", 'incorrectas': ["A. Neil Armstrong", "C. Buzz Aldrin", "D. Alan Shepard"]},
        {'pregunta': "¿Qué continente es el más grande del mundo?", 'opciones': ["A. Europa", "B. América", "C. Asia", "D. África"], 'respuesta': "C", 'correcta': "C. Asia", 'incorrectas': ["A. Europa", "B. América", "D. África"]}
    ],
    5: [
        {'pregunta': "¿Qué tipo de animal es una ballena?", 'opciones': ["A. Reptil", "B. Mamífero", "C. Ave", "D. Pez"], 'respuesta': "B", 'correcta': "B. Mamífero", 'incorrectas': ["A. Reptil", "C. Ave", "D. Pez"]},
        {'pregunta': "¿Cuál es el número romano que representa al 100?", 'opciones': ["A. L", "B. C", "C. D", "D. M"], 'respuesta': "B", 'correcta': "B. C", 'incorrectas': ["A. L", "C. D", "D. M"]}
    ],
    6: [
        {'pregunta': "¿Qué país inventó el papel?", 'opciones': ["A. Egipto", "B. China", "C. Grecia", "D. India"], 'respuesta': "B", 'correcta': "B. China", 'incorrectas': ["A. Egipto", "C. Grecia", "D. India"]},
        {'pregunta': "¿En qué ciudad está el Coliseo?", 'opciones': ["A. Atenas", "B. París", "C. Roma", "D. Londres"], 'respuesta': "C", 'correcta': "C. Roma", 'incorrectas': ["A. Atenas", "B. París", "D. Londres"]}
    ],
    7: [
        {'pregunta': "¿Cuál es el principal gas que causa el efecto invernadero?", 'opciones': ["A. Nitrógeno", "B. Oxígeno", "C. Dióxido de carbono", "D. Helio"], 'respuesta': "C", 'correcta': "C. Dióxido de carbono", 'incorrectas': ["A. Nitrógeno", "B. Oxígeno", "D. Helio"]},
        {'pregunta': "¿Cuál es el río más largo del mundo?", 'opciones': ["A. Amazonas", "B. Nilo", "C. Yangtsé", "D. Misisipi"], 'respuesta': "A", 'correcta': "A. Amazonas", 'incorrectas': ["B. Nilo", "C. Yangtsé", "D. Misisipi"]}
    ],
    8: [
        {'pregunta': "¿Qué científico descubrió la penicilina?", 'opciones': ["A. Albert Einstein", "B. Isaac Newton", "C. Alexander Fleming", "D. Marie Curie"], 'respuesta': "C", 'correcta': "C. Alexander Fleming", 'incorrectas': ["A. Albert Einstein", "B. Isaac Newton"]},
        {'pregunta': "¿Qué continente no tiene desiertos?", 'opciones': ["A. Asia", "B. Europa", "C. África", "D. Oceanía"], 'respuesta': "B", 'correcta': "B. Europa", 'incorrectas': ["A. Asia", "C. África", "D. Oceanía"]}
    ],
    9: [
        {'pregunta': "¿Qué autor escribió *Crimen y castigo*?", 'opciones': ["A. Fiódor Dostoyevski", "B. León Tolstói", "C. Franz Kafka", "D. Anton Chéjov"], 'respuesta': "A", 'correcta': "A. Fiódor Dostoyevski", 'incorrectas': ["B. León Tolstói", "C. Franz Kafka", "D. Anton Chéjov"]},
        {'pregunta': "¿En qué año cayó el Muro de Berlín?", 'opciones': ["A. 1985", "B. 1987", "C. 1989", "D. 1991"], 'respuesta': "C", 'correcta': "C. 1989", 'incorrectas': ["B. 1987", "D. 1991"]}
    ],
    10: [
        {'pregunta': "¿Qué unidad se usa para medir la intensidad de una corriente eléctrica?", 'opciones': ["A. Voltios", "B. Ohmios", "C. Amperios", "D. Vatios"], 'respuesta': "C", 'correcta': "C. Amperios", 'incorrectas': ["A. Voltios", "B. Ohmios", "D. Vatios"]},
        {'pregunta': "¿Qué científico propuso la mecánica cuántica?", 'opciones': ["A. Max Planck", "B. Niels Bohr", "C. Werner Heisenberg", "D. Albert Einstein"], 'respuesta': "A", 'correcta': "A. Max Planck", 'incorrectas': ["B. Niels Bohr", "C. Werner Heisenberg", "D. Albert Einstein"]}
    ]
}
comodines = {1:["1.llama a un amigo"],
             2:["2.cambio de pregunta"],
             3:["3.50/50"]}
ganar= 0
nombre = input("cual es tu nombre? ")
time.sleep(2)
print(f"Bienvenido jugador {nombre} a quien quiere ser millonario ")
time.sleep(1)
print("👏" *30)
time.sleep(5)
print("BIEN EMPEZEMOS")
for nivel, lista_preguntas in preguntas.items():
    print("*" * 100)
    print(f"Nivel {nivel}")
    print("*" * 100)
    pregunta_actual = preguntas[nivel][0]
    time.sleep(1)
    while True:
        print(pregunta_actual["pregunta"])
        for opcion in pregunta_actual["opciones"]:
            time.sleep(1)
            print(opcion)
            time.sleep(1)
        eleccion = int(input("Selecciona:\n1. Si sabes la respuesta correcta\n2. Si quieres usar un comodín\n"))
        if (eleccion == 1):
            respuesta = input("Dime la respuesta: ").upper()
            if respuesta == pregunta_actual["respuesta"]:
                ganar += 1000000
                print(f" Correcto,Felicidades ganaste ${ganar}")
                break  
            else:
                time.sleep(1)
                print("y la respuesta es \n🥁🥁🥁🥁🥁🥁🥁🥁🥁🥁🥁🥁🥁🥁🥁🥁🥁🥁🥁🥁🥁🥁")
                time.sleep(5)
                print("INCORRECTA Perdiste\nGracias por jugar VAMOS A COMERCIALES")
                break    
        else:
            if not comodines:
                print("Ya no tienes comodines disponibles.")
                continue
            print("Comodines disponibles:")
            for komodin, Comolist in comodines.items():
                time.sleep(1)
                print(Comolist[0])
                time.sleep(1)
            eleccion = int(input("Elige el número del comodín: "))
            if eleccion not in comodines:
                print("Comodín no válido.")
                continue                
            if(eleccion== 1):
                sugerencia = random.choice(pregunta_actual["opciones"])
                print(f"Juan: Yo creo que es '{sugerencia}'")
                del comodines[1]
            elif(eleccion== 2):
                pregunta_actual = preguntas[nivel][1]  
                print("\n Cambiaste de pregunta.")
                del comodines[2]                    
            elif(eleccion==3):
                incorrecta = random.choice(pregunta_actual["incorrectas"])
                print("50/50: Las opciones son:")
                pregunta_actual["opciones"] = [pregunta_actual["correcta"], incorrecta]
                del comodines[3]
    if respuesta.upper() != pregunta_actual["respuesta"]:
        break
    time.sleep(1)
    seguirjugando= int(input("quieres retirarte con lo que ya tienes o seguir jugado?\n1.seguir jugando\n2.salir con lo que tengo\n"))
    if(seguirjugando==2):
        print(f"Bien gracias por jugar\nGanaste: {ganar}")
        break