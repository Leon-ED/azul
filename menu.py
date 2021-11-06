from upemtk import *
from time import sleep

def fenetre():
    cree_fenetre(400, 400)

def accueil():
    rectangle(100, 150, 300, 200)
    texte(150, 160, "Jouer")

    rectangle(100, 250, 300, 300)
    texte(150, 260, "Quitter")

def clic():
    x,y,_ = attente_clic()
    return x,y

def clic_menu():
    clic_joueur = clic() 
    if 100<=clic_joueur[0]<=300 and 250<=clic_joueur[1]<=300: #Quitter
        print("Quitter")
        return False  #Pour que ça ferme la fenêtre dans le cas où on appuie sur quitter
    if 100 <=clic_joueur[0]<= 300 and 150<=clic_joueur[1]<=200:  #Jouer
        print("Jouer")
        return True  

def choix_mode():
    efface_tout()
    rectangle(100, 50, 300, 100)
    texte(130, 60, "Jouer à deux", taille = 20)

    rectangle(100, 150, 300, 200)
    texte(110, 160, "Jouer contre IA", taille=20)

    rectangle(100, 250, 300, 300)
    texte(160, 260, "Retour", taille = 20 )
    return True

def clic_mode():
    clic_joueur = clic()
    if 100 <=clic_joueur[0]<= 300 and 50<=clic_joueur[1]<=100:  #Jouer
        print("Jouer à deux")
        return 1   
    if 100<=clic_joueur[0]<=300 and 150<=clic_joueur[1]<=200: 
        print("Jouer contre IA")
        return 2  
    if 100<=clic_joueur[0]<=300 and 250<=clic_joueur[1]<=300: #Retour
        print("Retour")
        return False  #Pour que ça retourne dans la fenêtre de l'accueil

def recup_choix_joueur(a):
    choix_joueur = []
    if a == 2:
        choix_joueur.append(2)
    if a == 1:
        choix_joueur.append(1)
    return choix_joueur


def menu_azul():

    fenetre()
    accueil()
    while True:
        if clic_menu():
            choix_mode()
            while True:
                choix_j = clic_mode()
                if choix_j != False:
                    print(recup_choix_joueur(choix_j))
                    return choix_j
                else:
                    efface_tout()
                    accueil()     
                    break 
        else: 
            break 
    





if __name__ == '__main__':

    fenetre()
    accueil()
    while True:
        if clic_menu():
            choix_mode()
            while True:
                choix_j = clic_mode()
                if choix_j != False:
                    print(recup_choix_joueur(choix_j))
                    break
                else:
                    efface_tout()
                    accueil()     
                    break 
        else: 
            break 
            
            


        


    
''' Si on joue contre un bot, return une liste avec un 2. Puisque le joueur 2 est le bot
récupérer un choix joueur pour l'implémenter dans le main 

'''