"""L'usuari inserta 2 números i el programa  els compara i diu
quin és el més gran i quin el més petit. Si son iguals sortirà que son iguals."""
def ordenaNum():
    numero1 = (int)(input("Introdueix un numero:"))
    numero2 = (int)(input("Introdueix un altre numero:"))
    if (numero1 > numero2):
        print('El {numero1} es el més gran i el {numero2} es el més petit.'.format(numero1=numero1,numero2=numero2))
    elif (numero1 < numero2):
        print('El {numero2} es el més gran i el {numero1} es el més petit.'.format(numero1=numero1,numero2=numero2))
    else:
        print('El {numero1} i el {numero2} son iguals.'.format(numero1=numero1,numero2=numero2))