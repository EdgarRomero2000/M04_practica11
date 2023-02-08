#Aquesta funció et demana un numero i et diu si es parell o senar

def parellSenar():
    parSen = input("Escriu un numero parell o senar = ")
    parSen = int(parSen)
    if (parSen % 2 == 0):
        print('{parSen} es un numero parell '.format(parSen=parSen))
    else:
        print('{parSen} es un numero senar '.format(parSen=parSen))

