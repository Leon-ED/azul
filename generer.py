# !/usr/bin/env python3
# -*- coding: utf-8 -*-
from random import shuffle,randint
import copy
from upemtk import *
'''Module générant les variables du jeu'''




'''============ Variables globales ============'''

palais = [[["blue",False],["yellow",False],["red",False],["black",False],["green",False]],
        [["green",False],["blue",False],["yellow",False],["red",False],["black",False]],
        [["black",False],["green",False],["blue",False],["yellow",False],["red",False]],
        [["red",False],["black",False],["green",False],["blue",False],["yellow",False]],
        [["yellow",False],["red",False],["black",False],["green",False],["blue",False]]]

global centre_table
centre_table = [["vide","vide","vide","vide","vide","vide","vide","vide","vide","vide"],
                ["vide","vide","vide","vide","vide","vide","vide","vide","vide","vide"],
                ["vide","vide","vide","vide","vide","vide","vide","vide","vide","vide"]]

global COULEURS_JEU;COULEURS_JEU = ["black", "yellow", "green","red","blue"]
global sac;sac = []
global tour_fini; tour_fini = False
global couvercle; couvercle = []
global malus_centre; malus_centre = True
global partie_finie; partie_finie = False
global low_graphismes; low_graphismes = False
global joueurs_passes; joueurs_passes = 0
global tours; tours = 0
global joueur; joueur = 1
global positions_tuiles_centre; positions_tuiles_centre = [650,350]
global liste_score; liste_score = [0,0,0,0]
global manche_finie;manche_finie = False


'''==========================================='''


def sac_plein():
    '''
    Retourne une liste de taille 100 comportant 20 elements de chaque couleurs: black,yellow,green,orange,blue.
    '''
    for colors in COULEURS_JEU:
        for _ in range(20):
            sac.append(colors)
    
    shuffle(sac)

def sac_est_vide():
    '''
    Retourne True si le taille du sac est nulle ou False si elle ne l'est pas.
    '''
    return len(sac) == 0

def fabriques_plein(liste):
    global sac
    taille = len(sac)
    # print("Le couvercle est :",couvercle)
    # print("Le sac est: ",sac,"\n Sa taille est de :",taille)
    for i in range(2):
        for j in range(2):
            if sac_est_vide() and couvercle != []:
                # print("Le sac est vide, on va le remplir")
                # print("Le couvercle est :",couvercle)
                sac = copy.deepcopy(couvercle)
                # print("Le sac est maintenant :",sac)
                couvercle.clear()
                # print("Le couvercle est maintenant :",couvercle)
            elif sac_est_vide() and couvercle == [] and liste[0][0] in COULEURS_JEU:
                print("Plus de tuiles !!!!!")
                liste[i][j] = 'vide'
                continue

            taille = len(sac)
            position = randint(0,taille-1)
            liste[i][j] = sac[position]
            # print("On a ajouté : ",liste[i][j]," à la liste")
            sac.pop(position)

    # print("La fabrique est mainteantn : ",liste)
    return liste

def generer_grilles_joueurs(nombre_joueurs):
    liste_grilles_joueurs = []
    if nombre_joueurs >=2:

        global grille_j1
        grille_j1 = [["vide"], ["vide", "vide"], ["vide", "vide", "vide"], ["vide", "vide", "vide", "vide"], ["vide", "vide", "vide", "vide", "vide"]]
        global grille_j2
        grille_j2 = [["vide"], ["vide", "vide"], ["vide", "vide", "vide"], ["vide", "vide", "vide", "vide"], ["vide", "vide", "vide", "vide", "vide"]]

        liste_grilles_joueurs = [grille_j1,grille_j2]
    if nombre_joueurs >=3:
        global grille_j3
        grille_j3 = [["vide"], ["vide", "vide"], ["vide", "vide", "vide"], ["vide", "vide", "vide", "vide"], ["vide", "vide", "vide", "vide", "vide"]]
        liste_grilles_joueurs.append(grille_j3)
    if nombre_joueurs >=4:
        global grille_j4
        grille_j4 = [["vide"], ["vide", "vide"], ["vide", "vide", "vide"], ["vide", "vide", "vide", "vide"], ["vide", "vide", "vide", "vide", "vide"]]
        liste_grilles_joueurs.append(grille_j4)
    return liste_grilles_joueurs

def re_generer_grilles(liste_grilles):
    for grilles in liste_grilles:
        for i in range(len(grilles)):
            if 'vide' not in grilles[i]: #Si la ligne est remplie alors on la vide
                grilles[i][:] = ['vide']*len(grilles[i])
    return liste_grilles


def generer_palais(nombre_joueurs):
    liste_palais= []
    if nombre_joueurs >=2:
        global palais_j1
        palais_j1 = palais[:]
        global palais_j2
        palais_j2 = palais[:]
        liste_palais=[palais_j1,palais_j2]
    if nombre_joueurs >=3:
        global palais_j3
        palais_j3 = palais[:]
        liste_palais.append(palais_j3)
    if nombre_joueurs >=4:
        global palais_j4
        palais_j4 = palais[:]
        liste_palais.append(palais_j4)

    return liste_palais

def generer_planchers(nombre_joueurs):
    liste_planchers = []
    if nombre_joueurs >=2:
        global ligne_plancher_j1
        ligne_plancher_j1 = []
        global ligne_plancher_j2
        ligne_plancher_j2 = []
        liste_plancher = [ligne_plancher_j1,ligne_plancher_j2]
    if nombre_joueurs >=3:
        global ligne_plancher_j3
        ligne_plancher_j3 = []
        liste_plancher.append(ligne_plancher_j3)
    if nombre_joueurs >=4:
        global ligne_plancher_j4
        ligne_plancher_j4 = []
        liste_plancher.append(ligne_plancher_j4)
    return liste_plancher

def generer_fabriques(nombre_joueurs):

    if nombre_joueurs >=2:
        global fabrique1
        fabrique1 = fabriques_plein([[None,None],[None,None]])
        global fabrique2
        fabrique2  = fabriques_plein([[None,None],[None,None]])
        global fabrique3
        fabrique3 = fabriques_plein([[None,None],[None,None]])
        global fabrique4
        fabrique4 = fabriques_plein([[None,None],[None,None]])
        global fabrique5
        fabrique5 = fabriques_plein([[None,None],[None,None]])
        lst_fabriques = ["vide",fabrique1,fabrique2,fabrique3,fabrique4,fabrique5]
    if nombre_joueurs >=3:
        global fabrique6
        fabrique6 = fabriques_plein([[None,None],[None,None]])
        global fabrique7
        fabrique7 = fabriques_plein([[None,None],[None,None]])
        lst_fabriques.extend([fabrique6,fabrique7])
    if nombre_joueurs >=4:
        global fabrique8
        fabrique8 = fabriques_plein([[None,None],[None,None]])
        global fabrique9
        fabrique9 = fabriques_plein([[None,None],[None,None]])
        lst_fabriques.extend([fabrique8,fabrique9])

    lst_fabriques.append(centre_table)
    return lst_fabriques

def generer_fin_manche(liste_planchers,couvercle,liste_palais,liste_grilles_joueurs,nombre_joueurs,tours):
    import main;import time
    print(len(couvercle))
    for plancher in liste_planchers:
        main.remplir_couvercle(plancher,0,liste_planchers,True)
        print(couvercle)
    print(len(couvercle))
    print("Jeu : La manche est terminée")
    mise_a_jour()
    time.sleep(0.3)
    main.remplir_palais(liste_palais,liste_grilles_joueurs,liste_planchers)
    mise_a_jour()
    efface("fin_manche")
    tours+=1

if __name__ == "__main__":
    print(generer_grilles_joueurs(3))