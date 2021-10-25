from upemtk import *
from time import sleep

def fenetre():
    cree_fenetre(1920, 1080)

def accueil():
    rectangle(100, 200, 400, 250)
    texte(220, 205, "Jouer")

    rectangle(100, 260, 400, 310)
    texte(215, 265, "Quitter")

def clic():
    x,y,_ = attente_clic()
    return x,y

def clic_menu():
    if 100<=clic()[0]<=400 and 260<=clic()[1]<=310: #Quitter
        print("Quitter")
        return False
    if 100 <=clic()[0]<= 400 and 200<=clic()[1]<=250:  #Jouer
        print("Jouer")
        return True

def piste():
    pass

def choix_mode():
    efface_tout()
    rectangle(100, 200, 400, 250)
    texte(220, 205, "Joueur à deux")

    rectangle(100, 260, 400, 310)
    texte(215, 265, "Jouer contre ordinateur")

    return True

if __name__ == '__main__':
    fenetre()
    accueil()
    while True:
        clic_menu()
 

ferme_fenetre()

    
