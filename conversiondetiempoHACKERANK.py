horaI = int(input("ingrese la hora para convertirla: "))
minutos = int(input("minutos: "))
pregunta = int(input("1(AM) o 2(PM)? \n"))
match pregunta:
    case 1:
        if horaI == 12:
            horamilitar= 00
            horanormal = 12
            print(f"hora militar {horamilitar}:{minutos} A.M, hora normal {horanormal}:{minutos} A.M")
        else:
            horanormal = horaI
            horamilitar = horaI
            print(f"hora militar {horamilitar}:{minutos} A.M, hora normal {horanormal}:{minutos} A.M")
    case 2:
        if horaI == 12:
            horamilitar = horaI
            horanormal = horaI
            print(f"hora militar {horamilitar}:{minutos} P.M, hora normal {horanormal}:{minutos} P.M")
        else:
            horamilitar = horaI+12
            horanormal=horaI
            print(f"hora militar {horamilitar}:{minutos} P.M, hora normal {horanormal}:{minutos} P.M")
                    





