# !/usr/bin/env python3
# -*- coding: utf-8 -*-
'''Ancien code de l'ancienne version de l'ordinateur jouant au hasard et plus utilisée.'''

def ordinateur_choisir_fabrique(liste_des_fabriques):
    '''
    Permet à l'ordinateur de choisir aléatoirement une fabrique.

    :param list liste_des_fabriques: Liste de toutes les fabriques disponibles (non vides) et des tuiles au milieu

    :return: la fabrique choisie
    '''

    # print(len(liste_des_fabriques)-1)
    # print(liste_des_fabriques)
    position_hasard = randint(1,len(liste_des_fabriques)-1)
    fabrique_hasard = liste_des_fabriques[position_hasard]
    erreur = 0
    while fabrique_invalide(fabrique_hasard):
        position_hasard = randint(1,len(liste_des_fabriques)-1)
        fabrique_hasard = liste_des_fabriques[position_hasard]
        if erreur == 50:
            # print(f"/!\  Jeu : Ordinateur choisir fabrique : Erreur l'ordinateur ne sait pas ou choisir après {erreur} essais")
            fabrique_hasard = centre_table
            break
        erreur += 1
    # print(fabrique_hasard)
    return fabrique_hasard


def ordinateur_choisir_couleur(fabrique):
    '''
    L'ordinateur choisit une tuile au hasard parmi la fabrique donnée

    :param list fabrique: Fabrique dans laquelle l'ordinateur va choisir aléatoirement

    :return tuple selection_ordinateur: ('couleur',nombre,[fabrique])
    '''
    i = randint(0,len(fabrique)-1)
    j = randint(0,len(fabrique[i])-1)
    # print(fabrique)
    while fabrique[i][j] not in COULEURS_JEU:
        # print(fabrique[i][j])
        i = randint(0,len(fabrique)-1)
        j = randint(0,len(fabrique[i])-1)
    selection_ordinateur = select_tuiles(i, j, fabrique,ordinateur=True)
    # print("selec ordi",selection_ordinateur)
    remove_couleur(selection_ordinateur)
    if len(fabrique)>2:
        centre = True
    else:
        centre = False
    deplacer_vers_centre(selection_ordinateur,centre)
    dessiner_selection(selection_ordinateur,positions_tuiles_centre,low_graphismes)
    return selection_ordinateur

def ordinateur_coup(selection_ordinateur,grille_joueur,pos_grille,palais_ordi):
    '''
    L'ordinateur choisit une ligne aléatoirement parmi grille_joueur et y place ses tuiles

    :param tuple selection_ordinateur: ('couleur',nombre,[fabrique])
    :param list grille_joueur: Grille dans laquelle l'ordinateur va placer ses tuiles (selection_ordinateur)
    '''
    print("ELEM JOUABLES")
    print(lignes_jouables(grille_joueur,palais_ordi))
    colors = ["black", "yellow", "green","red","blue"]
    couleur, nombre, fabrique = selection_ordinateur
    colors.remove(couleur)
    i_min = 0
    i_max = 4
    fail = 0
    if jouer_couleur_grille(grille_joueur,couleur):
        i = 5
    else:
        while True :
            if fail == 60:
                # print(f"/!\  Jeu : L'ordinateur n'a pas pu trouver de ligne après {fail} essais.")
                i = 5
                break
            i = randint(i_min,i_max)
            fail += 1

            if 'vide' not in grille_joueur[i]:
                continue

            j = cherche_couleur_palais(palais_ordi,couleur,i) #Cherche si la couleur est deja dans le palais
            if palais_ordi[i][j][1]:
                continue

            for a in range(0,len(colors)):
                if colors[a] in grille[i]:
                    break
            else:
                break
    remplir_cases(selection_ordinateur, grille_joueur,0,i,pos_grille,ordinateur=True)