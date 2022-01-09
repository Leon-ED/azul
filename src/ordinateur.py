# !/usr/bin/env python3
# -*- coding: utf-8 -*-
from random import shuffle
from main import select_tuiles,remplir_cases,compteur_ligne
'''Module s'occupant de choisir quoi et où l'ordinateur doit jouer.'''
COULEURS_JEU = ["black", "yellow", "green","red","blue"]



def resume_fabriques(liste_fabriques):
    '''Combine les matrices de fabrique en une seule liste'''
    resume = []
    for fabriques in liste_fabriques[1:]:
        sous_liste = []
        for lignes in fabriques:
            sous_liste += lignes
        resume.append(sous_liste)

    return resume

def ordinateur_choisir_fabrique_couleur_2(liste_des_fabriques,grille_ordi,palais_ordi,resume,liste_lignes):
    '''
    Analyse par ligne jouable, la place restante et les couleurs jouables et cherche au mieux parmis
    les fabriques les meilleur coup pour l'ordinateur
    '''
    print("JOUER ")
    print("JOUER ")
    print("JOUER ")
    choix_possibles = None
    selec_plancher = None
    shuffle(liste_lignes)
    for ligne,taille,couleurs in liste_lignes:
        if couleurs == 'all':
            couleurs = COULEURS_JEU

        numero_fabrique = 0
        for fabriques in resume:
            numero_fabrique += 1
            real_fabrique = liste_des_fabriques[numero_fabrique]
            len_fabrique = len(real_fabrique[0])
            i = 0
            j = 0
            for tuiles in fabriques:
                if j == len_fabrique:
                    # #print(f'Taille : {len_fabrique}; j reset à {j}, i maintenant {i}')
                    j = 0
                    i += 1
                # #print(f'{tuiles} correspond vrament à {real_fabrique[i][j]}')

                if tuiles != 'vide' and tuiles in couleurs and fabriques.count(tuiles) == taille:
                    # #print("Un elem a ete trouve",ligne)
                    selection = select_tuiles(i,j,real_fabrique,ordinateur=True)
                    #print(ligne,taille,couleurs)
                    return selection,ligne
                if tuiles != 'vide' and tuiles in couleurs:
                    choix_possibles = []
                    element = (i,j,numero_fabrique,tuiles,ligne,taille,couleurs,taille-fabriques.count(tuiles))
                    if element not in choix_possibles:
                        choix_possibles.append(element)
                    # selection_secondaire = select_tuiles(i,j,real_fabrique,ordinateur=True)
                    # ligne_second = ligne
                elif tuiles != 'vide':
                    selec_plancher = (i,j,real_fabrique,ligne)
                
                j += 1

    if choix_possibles != None:
        return analayse_choix(choix_possibles,liste_des_fabriques)
    elif selec_plancher != None:
        i,j,real_fabrique,ligne = selec_plancher
        return select_tuiles(i,j,real_fabrique,ordinateur=True),ligne
    else:
        return False,False

def analayse_choix(set_possibilites,fabriques_disponibles):
    print("ANALYSE CHOIX")
    print("ANALYSE CHOIX")
    print("ANALYSE CHOIX")
    print("ANALYSE CHOIX")
    choix = [None,None]
    solution = []
    pos = -1
    print(set_possibilites)
    for i,j,num_fabrique,tuiles,lignes,taille,couleurs,ecart in set_possibilites:
        pos += 1
        if tuiles != 'vide' and (choix[0] == None or abs(ecart) < abs(choix[0])):
            choix = [ecart,pos]
            solution = [i,j,num_fabrique,lignes]
    i,j,num_fabrique,lignes = solution
    selection = select_tuiles(i,j,fabriques_disponibles[num_fabrique],ordinateur=True),lignes
    return selection
