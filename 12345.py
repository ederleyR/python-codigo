
#6200
#12400
#18600
#248.000
#347.200
horas_trabajadas = int(input("cuantas horas trabajaste esta semana  : "))

 
if horas_trabajadas > 48:
    salario_semisemifinal = (horas_trabajadas-48)
    salario_semifinal = (salario_semisemifinal*18600)
    salario_final= (salario_semifinal+347200)
    print("salario minimo",40*620)
    print("horas salario doble",8*12400)
    print("horas triple salario ",salario_semifinal)
    print("salario final",salario_final)
elif 40 <= horas_trabajadas <=48:
    salario_semisemifinal = (horas_trabajadas-40)
    salario_semifinal = (salario_semisemifinal*12400)
    salario_final= (salario_semifinal+248000)
    print("salario minimo",40*620)
    print("dinero de horas extras",salario_semifinal)
    print("salario final",salario_final)
elif horas_trabajadas < 0:
    print("3rr0r")
else:
    print("salario minimo",horas_trabajadas*6200)














