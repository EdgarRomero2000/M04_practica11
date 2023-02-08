"""Aquesta funció et demana la teva edat i els teus ingressos
i et diu si tens o no que fer la declaració a partir de la teva edat"""

def decHisenda():
    edat = input("Introdueix la teva edat: ")
    ingressos = input("Introdueix els teus ingressos: ")
    edat = int(edat)
    ingressos = int(ingressos)

    if(edat >= 18 and ingressos > 1200):
        print("És necessari que facis la declaració d’hisenda perque tens {edat} i {ingressos} euros d'ingressos " .format(edat=edat ,ingressos=ingressos))
    else:
        print("Encara no pots fer la declaració perque tens {edat} i {ingressos} euros d'ingressos " .format(edat=edat ,ingressos=ingressos))


