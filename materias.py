materias = []
Numveces = int(input("ingrese el numero de materias: "))
for i in range(Numveces):
    materia = input("ingrese las materias: ")
    materias.append(materia)
print(materias)   
reprobados = []
for mat in (materias):
    notas= float(input(f"ingrese la materia {mat}: "))
    if notas <3:
        reprobados.append(mat)
print("reprobaste: ",reprobados)
