import random
pedir = int(input("dame un numero: "))
lista = []
mayor = 0
menor =100
for i in range(pedir):
    nale = random.randint(1,100)
    lista.append(nale)

print("numero:",lista)

for i in range(len(lista)):
    if lista[i] > mayor:
        mayor = lista[i]       
print("mayor:",mayor)
lista.remove(mayor)
print(lista)
mayor=0
print("numero:",lista)

for i in range(len(lista)):
    if lista[i] > mayor:
        mayor = lista[i]       
print("mayor:",mayor)
lista.remove(mayor)
print(lista)
mayor=0
print("numero:",lista)

for i in range(len(lista)):
    if lista[i] > mayor:
        mayor = lista[i]       
print("mayor:",mayor)
lista.remove(mayor)
print(lista)
mayor=0
print("numero:",lista)

for i in range(len(lista)):
    if lista[i] > mayor:
        mayor = lista[i]       
print("mayor:",mayor)
lista.remove(mayor)
print(lista)
mayor=0
print("numero:",lista)

for i in range(len(lista)):
    if lista[i] > mayor:
        mayor = lista[i]       
print("mayor:",mayor)
lista.remove(mayor)
print(lista)
































