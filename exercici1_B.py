#Aquesta funció et demana dos numeros i et diu quin numero es mes gran o mes petit
def granPetit():
    num1 = input("Escriu un numero del 1 al 9 = ")
    num2 = input("Escriu un numero del 1 al 9 = ")
    num1 = str(num1)
    num2 = str(num2)
    
    if (num1 > num2):
        print('{numero1} es mes gran que {numero2}'.format(numero1=num1, numero2=num2))
    elif(num1 < num2):
        print('{numero1} es mes petit que {numero2}'.format(numero1=num1, numero2=num2))
    if (num1 == num2):
        print("")


