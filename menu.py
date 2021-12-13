# !/usr/bin/env python3
# -*- coding: utf-8 -*-
'''Module permettant de créer les menus pour permettre au joueur de choisir ses paramètres de jeu'''

#---Imports
from upemtk import *
from time import sleep

def fenetre():
    cree_fenetre(400, 400)

def accueil():
    texte(140,60,"Jeu : Azul",police="Arial")
    texte(350,380,"v1.9.0-b",police="Arial",taille=10)

    rectangle(100, 140, 300, 190)
    texte(160, 150, "Jouer",police='Arial')

    rectangle(100, 210, 300, 260)
    texte(150, 220, "Quitter",police='Arial')


    rectangle(100, 280, 300, 330)
    texte(150, 290, "Options",police='Arial')


    rectangle(10, 380, 20, 390)

def clic_menu():
    x,y,_ = attente_clic()
    print(x,y)
    if 100<=x<=300 and 280<=y<=330: #options
        return "settings"
    if 100<=x<= 300 and 140<=y<=190:  #Jouer
        return True  
    if 100<=x<=300 and 210<=y<=260: #Quitter
        return False  #Pour que ça ferme la fenêtre dans le cas où on appuie sur quitter
    if 10<=x<=20 and 380<=y<=390: #Mode bot vs bot
        return -1 



    return

def choix_mode():
    efface_tout()
    rectangle(100, 105, 300, 155)
    texte(125, 115, "Jouer à deux", taille = 20,police='Arial')

    rectangle(100, 175, 300, 225)
    texte(110, 185, "Jouer contre IA", taille=20,police='Arial')

    rectangle(100, 245, 300, 295)
    texte(160, 255, "Retour", taille = 20 ,police='Arial')


def show_settings():
    pass
    '''
    efface_tout()
    texte(120,60,"Paramètres",police="Arial")
    texte(360,380,"v1.9.0",police="Arial",taille=10)
    settings = open("./files/settings.txt","r")
    lignes = settings.readlines()
    etat = lignes[0][:-1]
    #settings.seek(0)

    rectangle(90, 140, 310, 190)
    texte(100,150,"Graphiques bas :"+str(etat),police="Arial",taille=15)

    rectangle(100, 245, 300, 295)
    texte(160, 255, "Retour", taille = 20 ,police='Arial')


    while True:
        x,y,_ = attente_clic()
        print(x,y)
        if 100<=x<=300 and 245<=y<=295: #Retour
            print("retour")
            settings.close()
            return "accueil"

        if 90<=x<=310 and 140<=y<=190: #Graphiques
            settings = open("./files/settings.txt","w")
            new_lignes = ""
            new_etat = not bool(etat)
            print(new_etat)
            lignes[0] = str(new_etat)
            for mots in lignes:
                new_lignes+=mots
            print(new_lignes)
            settings.write(new_lignes)
            settings.close()
            break
            '''

def clic_mode():
    x,y,_ = attente_clic()
    if 100 <=x<= 300 and 105<=y<=155:  #Jouer à 2
        return 1   
    if 100<=x<=300 and 175<=y<=225: #Jouer contre l'ordinateur
        return 2  
    if 100<=x<=300 and 245<=y<=295: #Retour
        return False  
    
    return #Clics qui correspondent à rien

def recup_choix_joueur(a):
    choix_joueur = []
    if a == 2:
        choix_joueur.append(2)
    return choix_joueur




def menu_azul():

    fenetre()
    accueil()
    while True:
        clic_accueil = clic_menu()
        if clic_accueil == -1:
            return [1,2]

        if clic_accueil == "settings":
            print("Erreur : Les paramètres ne sont pas encore implémentés ! ")
            #show_settings()
        if clic_accueil:
            choix_mode()

            while True:
                choix_j = clic_mode()
                if choix_j != None and choix_j != False:
                    choix_j = recup_choix_joueur(choix_j)
                    return choix_j
                elif choix_j == None:
                    continue
                else:
                    efface_tout()
                    accueil()     
                    break

        elif clic_accueil == False:
            return

        else:
            continue 
    


if __name__ =="__main__":
    fenetre()
    show_settings()