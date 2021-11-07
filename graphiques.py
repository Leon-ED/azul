# !/usr/bin/env python3
# -*- coding: utf-8 -*-
'''Module qui a pour but d'afficher tous les graphismes à l'écran en fonction des données envoyées'''

#---Imports
from upemtk import *

cote_carre = 50
largeur_fenetre = 1800
hauteur_fenetre = 900

def dessiner_fabriques(nombre_fabriques):
    '''
    Dessine les  cercles des fabriques en haut de l'écran
    '''
    ecart = largeur_fenetre/nombre_fabriques
    for i in range(nombre_fabriques):
        cercle(100+ecart*i,75,60,epaisseur=1)


def dessiner_lignes_motif(nombre_joueurs): #Affiche les lignes du motif
    '''
    Dessine les lignes de motif des deux joueurs.
    '''
    for nb_lignes in range(0,6):
        for nb_colonnes in range(0,nb_lignes):
            rectangle(250-60*nb_colonnes, 300+60*nb_lignes, 300-60*nb_colonnes, 350+60*nb_lignes) #Joueur 1
            rectangle(1400-60*nb_colonnes, 300+60*nb_lignes, 1450-60*nb_colonnes, 350+60*nb_lignes) #Joueur 2

def dessiner_murs_palais(nombre_joueurs):
    '''
    Dessine les murs du palais des deux joueurs.
    '''   
    for nb_lignes in range(0,5):
        for nb_colonnes in range(0,5):
            rectangle(350+60*nb_colonnes, 360+60*nb_lignes, 400+60*nb_colonnes, 410+60*nb_lignes)
            rectangle(1500+60*nb_colonnes, 360+60*nb_lignes, 1550+60*nb_colonnes, 410+60*nb_lignes)


def dessiner_plancher(nombre_joueurs):
    '''
    Dessine les lignes de plancher des deux joueurs
    '''
    malus = [-1,-1,-2,-2,-2,-3,-3]
    for i in range(7):
        texte(25+60*i,710,str(malus[i]),taille=15)
        rectangle(10+60*i, 730 , 60+60*i, 780)

        texte(1175+60*i,710,str(malus[i]),taille=15)
        rectangle(1160+60*i, 730, 1210+60*i, 780)

def dessiner_tuiles_plancher(liste_plancher,index_plancher):
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
    nb_elem = 0
    nb_ligne = 0

    for i in range(len(liste_centre)):
        for j in range(len(liste_centre[i])):

            if liste_centre[i][j] == 'vide':
                nb_elem+=1
                continue
            rectangle(650+50*nb_elem, 400+50*nb_ligne, 700+50*nb_elem, 350+50*nb_ligne,remplissage=liste_centre[i][j],couleur='black')
            nb_elem +=1
            if nb_elem == len(liste_centre[i]):
                nb_elem = 0
                nb_ligne +=1
            

def dessiner_selection(selection,index_plancher):
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
    '''
    if -10 in fabrique:
        return
    ecart = 200
    j = 0
    ligne = 0
    x = liste_positions[i-1]
    for line in fabrique:
        for colors in line:
            if j == 2:
                j = 0
                ligne = 1
            rectangle(x+50*j, 50+50*ligne, (x+50)+50*j, 100+50*ligne,remplissage=colors,couleur='black',epaisseur=2)
            
            j+=1   

def dessine_tuiles_lignes(grille,index):
    for i in range(len(grille)):
        for j in range(i+1):
            if grille[i][j] == "vide":
                continue
            rectangle(index[0]-60*j, index[1]+60*i, (index[0]+50)-60*j, (index[1]+50)+60*i,remplissage=grille[i][j])


def dessiner_plateau(nombre_joueurs,nombre_fabriques):
    '''
    Permet de dessiner tous les éléments du jeu en une seule fois en regroupant
    toutes les autres fonctions.
    '''
    dessiner_lignes_motif(nombre_joueurs)
    dessiner_murs_palais(nombre_joueurs)
    dessiner_plancher(nombre_joueurs)


def position(nombre_fabriques):
    ecart = 200
    liste_positions = [50]
    for i in range(1,nombre_fabriques):
        liste_positions.append(liste_positions[i-1]+ecart)
    return liste_positions


