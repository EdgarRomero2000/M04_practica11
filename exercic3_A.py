import random
"""Se li demanara a l'usuari que doni un numero que el programma comparara amb un numero generat entre 0 i 100
per cada vegada que l'usuari s'equivoqui el rang de numeros es fara més petit"""
def randomNum():
    num1 = (int)(input("Introdueix un numero del 0 al 100: "))
    num2 = random.randrange(0,100)
    superior = 100;
    inferior = 0;
    trobat = False
    while(trobat == False):

        if(num1 == num2):
            print("Molt bé! Has endevinat el número {num1}!".format(num1=num1))
            trobat = True
        elif(num1 > num2):
            print("El número és més petit que {num1}".format(num1=num1))
            superior = num1;
            num1 = (int)(input("Introdueix un numero del {inferior} al {superior}: ".format(inferior=inferior,superior=superior)))
        elif(num1 < num2):
            print("El número és més gran que  {num1}".format(num1=num1))
            inferior = num1;
            num1 = (int)(input("Introdueix un numero del {inferior} al {superior}: ".format(inferior=inferior,superior=superior)))


