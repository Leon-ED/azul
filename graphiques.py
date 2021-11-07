# !/usr/bin/env python3
# -*- coding: utf-8 -*-
'''Module qui a pour but d'afficher tous les graphismes à l'écran en fonction des données envoyées'''

#---Imports
from upemtk import *
from menu import *

cote_carre = 50
largeur_fenetre = 1800
hauteur_fenetre = 900

def dessiner_lignes_motif(nombre_joueurs): #Affiche les lignes du motif
    '''
    Dessine les lignes de motif des deux joueurs.

    :param int nombre_joueurs: Pas implémenté
    '''
    for nb_lignes in range(0,6):
        for nb_colonnes in range(0,nb_lignes):
            rectangle(250-60*nb_colonnes, 300+60*nb_lignes, 300-60*nb_colonnes, 350+60*nb_lignes) #Joueur 1
            rectangle(1400-60*nb_colonnes, 300+60*nb_lignes, 1450-60*nb_colonnes, 350+60*nb_lignes) #Joueur 2

def dessiner_murs_palais(nombre_joueurs):
    '''
    Dessine les murs du palais des deux joueurs.

    :param int nombre_joueurs: Pas implémenté
    '''   
    for nb_lignes in range(0,5):
        for nb_colonnes in range(0,5):
            rectangle(350+60*nb_colonnes, 360+60*nb_lignes, 400+60*nb_colonnes, 410+60*nb_lignes)
            rectangle(1500+60*nb_colonnes, 360+60*nb_lignes, 1550+60*nb_colonnes, 410+60*nb_lignes)


def dessiner_plancher(nombre_joueurs):
    '''
    Dessine les lignes de plancher des deux joueurs

    :param int nombre_joueurs: Pas implémenté
    '''
    malus = [-1,-1,-2,-2,-2,-3,-3]
    for i in range(7):
        texte(25+60*i,710,str(malus[i]),taille=15)
        rectangle(10+60*i, 730 , 60+60*i, 780)

        texte(1175+60*i,710,str(malus[i]),taille=15)
        rectangle(1160+60*i, 730, 1210+60*i, 780)

def dessiner_tuiles_plancher(liste_plancher,index_plancher):
    '''
    Dessine les tuiles présentes dans le plancher du joueur

    :param list liste_plancher: Liste contenant les couleurs des tuiles dans le plancher du joueur
    :param list index_plancher : Liste des positions du plancher du joueur (permet l'affichage)

    '''


    if "vide" in liste_plancher or len(liste_plancher) == 0:
        return
    i = 0   
    for colors in liste_plancher:
        if colors == -1:
            image(index_plancher[0]+60*i, index_plancher[1],'images/first.gif',ancrage='nw')
            i+=1
            continue
        rectangle(index_plancher[0]+60*i, index_plancher[1], (index_plancher[0]+50)+60*i, (index_plancher[1]+50),remplissage=colors)
        i+=1

def dessiner_tuiles_centre(liste_centre):
    '''
    Dessine les tuiles au centre du plateau

    :param list liste_centre: Liste contenant la couleur des tuiles au centre du plateau

    '''
    nb_elem = 0
    nb_ligne = 0
    print(liste_centre)
    for i in range(len(liste_centre)):
        for j in range(len(liste_centre[i])):

            if liste_centre[i][j] == 'vide':
                nb_elem+=1
            if nb_elem == 10:
                nb_elem = 0
                nb_ligne +=1
            if liste_centre[i][j] != 'vide':
                rectangle(650+50*nb_elem, 400+50*nb_ligne, 700+50*nb_elem, 350+50*nb_ligne,remplissage=liste_centre[i][j],couleur='black')
                nb_elem +=1

            

def dessiner_selection(selection,index_plancher):
    '''
    Dessine les tuiles actuellement sélectionnées par le joueur.

    :param tuple selection: ('couleur',compteur,fabrique) > (str,int,list)
    :param list index_plancher: Liste des positions du plancher du joueur (permet l'affichage)


    '''
    couleur,nombre,_ = selection
    if couleur == 'vide':
        return
    texte(index_plancher[0], index_plancher[1]-80, "Selection:",taille=23)
    texte(index_plancher[0], index_plancher[1]-50, "Clic droit pour effacer",taille=13)
    for i in range(nombre):
        rectangle((index_plancher[0]+170)+60*i, index_plancher[1]-75, (index_plancher[0]+220)+60*i, (index_plancher[1]-25),remplissage=couleur)
        pass




def dessiner_tuiles_fabriques(fabrique,i,liste_positions):
    '''
    Prend en paramètre une liste de couleur et dessine les rectangles
    de chaque couleur de cette liste.

    :param list fabrique: Liste de la fabrique a dessiner
    :param int i: Numéro de la fabrique
    :param list liste_positions: Position des fabriques dans la fenêtre
    '''
    ligne(-100,200,2200,200,epaisseur=3)
    x = liste_positions[i-1]
    cercle(x+50,100,60,epaisseur=2)
    if -10 in fabrique:
        return
    ecart = 200
    j = 0
    lignes = 0

    for line in fabrique:
        for colors in line:
            if j == 2:
                j = 0
                lignes = 1
            rectangle(x+50*j, 50+50*lignes, (x+50)+50*j, 100+50*lignes,remplissage=colors,couleur='black',epaisseur=2)
            
            j+=1   

def dessine_tuiles_lignes(grille,index):
    '''
    Dessine les tuiles dans la grille du joueur

    :param list grille: Grille du joueur qui joue
    :param list index: Position de la grille du joueur dans la fenêtre

    '''
    for i in range(len(grille)):
        for j in range(i+1):
            if grille[i][j] == "vide":
                continue
            rectangle(index[0]-60*j, index[1]+60*i, (index[0]+50)-60*j, (index[1]+50)+60*i,remplissage=grille[i][j])


def dessiner_plateau(nombre_joueurs,nombre_fabriques):
    '''
    Permet de dessiner tous les éléments du jeu en une seule fois en regroupant
    toutes les autres fonctions.

    :param int nombre_joueurs: Pas implémenté
    :param int nombre_fabriques: Nombre de fabriques à créer
    '''
    dessiner_lignes_motif(nombre_joueurs)
    dessiner_murs_palais(nombre_joueurs)
    dessiner_plancher(nombre_joueurs)


def position(nombre_fabriques):
    '''
    Calcule la positions des fabriques à dessiner

    :param int nombre_fabriques: Nombre de fabriques à créer

    :return list liste_positions: Liste ayant la positions de toutes les fabriques

    '''


    ecart = 200
    liste_positions = [50]
    for i in range(1,nombre_fabriques):
        liste_positions.append(liste_positions[i-1]+ecart)
    return liste_positions


