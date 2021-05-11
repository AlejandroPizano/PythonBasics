import random
def calcularEdad():
    age =int(input("Cual es tu edad?\n"))
    decadas=age//10
    años=age % 10
    print("Tienes "+str(round(decadas))+" decadas y "+str(años)+" años vivo")

def guess():
    machineopc= random.randint(1,6)
    userans=int(input("Introduce el numero que quieras adivinar.\n"))
    if(machineopc==userans):
        print("Ganaste!!")
    else:
        print("Perdiste:( el numero era:  "+str(machineopc))
        guess()

guess()