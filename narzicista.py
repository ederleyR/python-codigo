numero = input("Introduce un número (como cadena): ")
numeros = int(numero)
digitos = len(numero)  
resultados = []
for caracter in numero:
     potencia = int(caracter) ** digitos
     resultados.append(potencia)
     suma = sum(resultados)
if suma == numeros:
     print("es numero narzicista")
else:
     print("no es narzicista el resultado fue",suma,"y el numero que diste fue",numero)