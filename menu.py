# !/usr/bin/env python3
# -*- coding: utf-8 -*-
'''Module permettant de créer les menus pour permettre au joueur de choisir ses paramètres de jeu'''

#---Imports
from upemtk import *
from time import sleep

def fenetre():
    cree_fenetre(400, 400)

def accueil():
    rectangle(100, 140, 300, 190)
    texte(160, 150, "Jouer",police='Arial')

    rectangle(100, 210, 300, 260)
    texte(150, 220, "Quitter",police='Arial')
    rectangle(10, 380, 20, 390)


def clic_menu():
    x,y,_ = attente_clic()
    if 100<=x<= 300 and 140<=y<=190:  #Jouer
        return True  
    if 100<=x<=300 and 210<=y<=260: #Quitter
        return False  #Pour que ça ferme la fenêtre dans le cas où on appuie sur quitter
    if 10<=x<=20 and 380<=y<=390:
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

'''
def affiche_boutons():
    rectangle(1600, 840, 1700, 880)
    texte(1603, 840, "Quitter")
'''





def menu_azul():

    fenetre()
    accueil()
    while True:
        clic_accueil = clic_menu()
        if clic_accueil == -1:
            return [1,2]
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
    
