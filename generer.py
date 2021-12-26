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
            if 'vide' not in grilles[i]:
                grilles[i][:] = ['vide']*len(grilles[i])


    return liste_grilles

def generer_palais(nombre_joueurs,palais):
    liste_palais= []

    if nombre_joueurs >=2:
        global palais_j1
        palais_j1 = palais.copy()
        global palais_j2
        palais_j2 = palais.copy()
        liste_palais=[palais_j1,palais_j2]
    if nombre_joueurs >=3:
        global palais_j3
        palais_j3 = palais.copy()
        liste_palais.append(palais_j3)
    if nombre_joueurs >=4:
        global palais_j4
        palais_j4 = palais.copy()
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
