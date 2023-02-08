"""L'usuari haura d'escollir un de cinc noms d'una llista i depenent del que agafi rebra una resposta diferent
en cas de posar un nom que no estigui a la llista se li demanara que oh intenti una altra vegada"""
def noms():
    llistaNoms = input("Escull un dels noms seguents: Washington, Lincoln, Escobar, Gandalf o Aatrox.")

    if(llistaNoms == "Washington"):
        print("{llistaNoms}: Vamos soldado hay que liberar america.".format(llistaNoms=llistaNoms))
    elif(llistaNoms == "Lincoln"):
        print("{llistaNoms}: Oh que bonita obra de teatro. Bam....".format(llistaNoms=llistaNoms))
    elif (llistaNoms == "Escobar"):
        print("{llistaNoms}: Plata o plomo.".format(llistaNoms=llistaNoms))
    elif (llistaNoms == "Gandalf"):
        print("{llistaNoms}: You shall not pass.".format(llistaNoms=llistaNoms))
    elif (llistaNoms == "Aatrox"):
        print("{llistaNoms}: Am I the abyss? Or did I gaze into it?".format(llistaNoms=llistaNoms))
    else:
        print("Vaya no has escoguido un nombre de la lista intenta otra vez.")