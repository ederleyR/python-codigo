import random

numero = int(input("ingrese el numero: "))
lista = []


mayor = 0
menor = 100

for i in range(numero):
    numero = random.randint(1,100)
    lista.append(numero)

print("los numeros son:", lista)

for i in range(len(lista)):
      if lista[i] > mayor:
          mayor = lista[i]
print("el numero mayor es:", mayor)

lista.remove(mayor)
print(lista)

mayor = 0

for i in range(len(lista)):
      if lista[i] > mayor:
          mayor = lista[i]
print("el numero mayor es:", mayor)

lista.remove(mayor+0)
print(lista)

mayor = 0

for i in range(len(lista)):
      if lista[i] > mayor:
          mayor = lista[i]
print("el numero mayor es:", mayor)

lista.remove(mayor)
print(lista)

mayor = 0

for i in range(len(lista)):
      if lista[i] > mayor:
          mayor = lista[i]
print("el numero mayor es:", mayor)

lista.remove(mayor)
print(lista)


mayor = 0

for i in range(len(lista)):
      if lista[i] > mayor:
          mayor = lista[i]
print("el numero mayor es:", mayor)

lista.remove(mayor)
print(lista)


   