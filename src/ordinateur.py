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

    print("resum",resume)
    return resume



def ordinateur_choisir_fabrique_couleur_2(liste_des_fabriques,grille_ordi,palais_ordi,resume,liste_lignes):
    '''
    Analyse par ligne jouable, la place restante et les couleurs jouables et cherche au mieux parmis
    les fabriques les meilleur coup pour l'ordinateur
    '''
    selection_secondaire = None
    selection_ter = None
    shuffle(liste_lignes)
    # shuffle(resume)
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
                    print(f'Taille : {len_fabrique}; j reset à {j}, i maintenant {i}')
                    j = 0
                    i += 1
                print(f'{tuiles} correspond vrament à {real_fabrique[i][j]}')

                if tuiles != 'vide' and tuiles in couleurs and fabriques.count(tuiles) == taille:
                    print("Un elem a ete trouve",ligne)
                    selection = select_tuiles(i,j,real_fabrique,ordinateur=True)
                    print(ligne,taille,couleurs)
                    return selection,ligne
                
                if tuiles != 'vide' and tuiles in couleurs:
                    selection_secondaire = select_tuiles(i,j,real_fabrique,ordinateur=True)
                    ligne_second = ligne
                elif tuiles != 'vide':
                    selection_ter = select_tuiles(i,j,real_fabrique,ordinateur=True)
                    ligne_ter = 5
                j += 1
    if selection_secondaire != None:
        print("selec secon",ligne)
        print(ligne,taille,couleurs)
        return selection_secondaire,ligne_second
    elif selection_ter != None:
        return selection_ter,ligne_ter
    else:
        return False,False

