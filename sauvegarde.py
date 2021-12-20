# !/usr/bin/env python3
# -*- coding: utf-8 -*-
'''Module qui s'occupe de sauvegarder les fichiers'''

def copy_file(chemin):
    file_list = []
    with open(chemin,'r') as files:
        for lines in files:
            file_list.append(eval(lines.strip()))

    return file_list

def ecrire_config(liste,chemin):
    with open(chemin,'w') as files:
        for elems in liste:
            files.write(str(elems)+'\n')
    return True


def ecrire_save(nombre_joueurs,joueur,jours_ia,joueurs_passes,liste_grilles,liste_planchers,tuiles_centres,liste_fabriques,liste_palais,malus_centre):
    liste_save = [True,nombre_joueurs,joueur,jours_ia,joueurs_passes,liste_grilles,liste_planchers,tuiles_centres,liste_fabriques,liste_palais,malus_centre]
    return ecrire_config(liste_save,'./files/save.txt')

