# !/usr/bin/env python3
# -*- coding: utf-8 -*-
'''Module principal du jeu s'occupant de la partie logique et de l'interaction avec l'utilisateur'''

#---Imports
from upemtk import *
from graphiques import *
from time import sleep
from random import randint


cree_fenetre(1800, 900)
#---------------------------------Sac---------------------------------#
def sac_plein():
    '''
    Retourne une liste de taille 100 comportant 20 elements de chaque couleurs: black,yellow,green,orange,blue.
    '''
    couleurs = ["black", "yellow", "green","orange","blue"]
    sac = []
    for colors in couleurs:
        for i in range(20):
            sac.append(colors)
    return sac

def sac_est_vide():
    '''
    Retourne True si le taille du sac est nulle ou False si elle ne l'est pas.
    '''
    return len(sac) != 0

#------------------------------Fabriques-------------------------------#


def fabriques_plein(liste):
    '''
    Prends en paramètre une liste et la retourne en ayant ajouté 4 couleurs aléatoires présentes dans le sac en supprimant l'élément
    choisit de la liste sac.
    '''
    for i in range(2):
        for j in range(2):
            taille = len(sac)
            r = randint(0,taille-1)
            liste[i][j] = sac[r]
            sac.pop(r)

    return liste


def liste_invalide(fabrique):
    '''
    Prend en paramètre une liste(fabrique) et renvoie True si elle est invalide
    c'est à dire si sa taille est nulle ou que son type n'est pas une liste sinon renvoie False.
    '''
    if fabrique == centre_table:
        for lines in fabrique:
            for colors in lines:
                if colors != 'vide':
                    return False
        return True


    for i in range(len(fabrique)):
        if type(fabrique[i]) != list:
            return True

        if -10 in fabrique:
            return True
    
    return False

def select_fabrique(x,y):
    '''
    Prends en paramètres les coordonnées d'un clic puis renvoie la fabrique correspondante au clic
    selon le nombre de fabriques (lié au nombre de joueur) et renvoie l'indice i et j ainsi que la liste (fabrique)
    sélectionnée. 
    '''
    i = (x//50)-1
    j = (y//50)-1
    fabrique = []
    selection = []
    emplacements = []
    if i < 0 or j<0:
        return -10,-10,-10
    if nombre_joueurs >=2:
        if i == 0 or i==1:
            fabrique = fabrique1

        if i == 4 or i==5:
            i-=4
            fabrique = fabrique2

        if i == 8 or i==9:
            i-=8
            fabrique = fabrique3

        if i == 12 or i==13:
            i-=12
            fabrique = fabrique4

        if i == 16 or i==17:
            i-=16
            fabrique = fabrique5

    if nombre_joueurs >=3:
        if i == 20 or i==21:
            i-=20
            fabrique = fabrique6

        if i == 24 or i==25:
            i-=24
            fabrique = fabrique7

    if nombre_joueurs >= 4:

        if i == 28 or i==29:
            i-=28
            fabrique = fabrique8
        
        if i == 32 or i==33:
            i-=32
            fabrique = fabrique9
    return i,j,fabrique


def select_tuiles(i,j,fabrique):
    '''
    Prend en paramètres les indices i et j et une liste (fabrique) renvoie la couleur ainsi que le nombre
    d'occurence de la couleur dans la fabrique ainsi que la fabrique. Si cela ne correspond à rien la fonction renvoie
    -10
    '''
    if fabrique != centre_table and ( i>1 or liste_invalide(fabrique) or j>1):
        return -10
    if fabrique == centre_table and (j>=len(fabrique[i])):
        return -10
    compteur = 0
    couleur = fabrique[i][j]
    if couleur == 'vide':
        return -10
    for lines in fabrique:
        for elems in lines:
            if elems == couleur:
                compteur+=1
    return couleur,compteur,fabrique
    

def liste_non_valide(liste):
    if -10 in liste:
        return True
    return False

def un_select_fabrique(type_clic):
    if type_clic == 'ClicDroit':
        return True
    return False


    
def remove_couleur(selection):
    '''
    Prends en paramètre la sélection composée de la couleur de la tuile, du nombre d'occurence de cette couleur et la liste (fabrique)
    d'où viennent ces tuiles. La fonction renvoie -10 si la liste ne peut pas être traitée sinon elle supprime toutes les occurences de la couleur
    présente dans cette liste.
    '''
    couleur,nombre,fabrique = selection
    if liste_invalide(fabrique):
        return -10

    if fabrique == centre_table:
        for i in range(len(fabrique)):
            for j in range(len(fabrique[i])):
                if fabrique[i][j] == couleur:
                    fabrique[i][j] = 'vide'
        return

    for i in range(len(fabrique)):
        while couleur in fabrique[i]:
            fabrique[i].remove(couleur)       

def remplir_cases(selection,grille,y,ordinateur=False):
    '''
    Prends en paramètre la sélection composée de la couleur de la tuile, du nombre d'occurence de cette couleur et la liste (fabrique)
    d'où viennent ces tuiles. Ainsi que la grille du joueur en train de jouer et la position y du clic de l'utilisateur.
    La fonction renvoie -10 si les coordonnées du clic de sont pas bonnes. Sinon elle place dans la liste de la grille les éléments sélectionnés
    et s'il le faut appelle la fonction remplir_plancher afin de traiter les cas où plus de tuiles sont sélectionnées qu'il n'y a de place sur la ligne choisie.
    '''
    couleur,nombre,_ = selection
    if ordinateur == False:
        if (y < positions_grille[4] or y > positions_grille[5]): #Detecte sur la position y n'est pas bonne
            return -10 
        if  (x<positions_grille[2] or x>positions_grille[3]): #Detecte si la position x n'est pas bonne

            return -10
        y = (y//60)-6

        if 'vide' not in grille[y]: #Detecte s'il n'y a plus de place dans la ligne et retourne -10 si c'est le cas

            return -10

    longueur = 0
    for colors in grille[y]: #Detecte si une couleur autre est déja présente et si c'est le cas retourne -10
        if colors == 'vide':
            longueur += 1   
            continue
        if colors != couleur:

            return -10
    reste = 0

    for i in range(0,nombre):
        if nombre> longueur:
            reste = nombre-longueur
            if i == longueur-1:
                remplir_plancher(couleur,reste,plancher)
                j=0
                while j< len(grille[y])-1 and grille[y][j] != 'vide':
                    j+=1
                grille[y][j] = couleur
                return
            j=0
            while j< len(grille[y])-1 and grille[y][j] != 'vide':
                j+=1
            grille[y][j] = couleur           
        else:
            j=0
            while j< len(grille[y])-1 and grille[y][j] != 'vide':
                j+=1
            grille[y][j] = couleur
            

def remplir_plancher(couleur,reste,grille_plancher):
    '''
    Prends en paramètre, la couleur de la tuile, le nombre restant et la grille du plancher du joueur en train de jouer.
    La fonction si la grille de plancher n'est pas pleine ajoute les éléments à celle-ci
    '''
    if len(grille_plancher) != 7:
        for i in range(reste):
            grille_plancher.append(couleur)


def deplacer_vers_centre(selection):
    '''
    Prends en paramètre la sélection composée de la couleur de la tuile, du nombre d'occurence de cette couleur et la liste (fabrique)
    d'où viennent ces tuiles.
    La fonction ajoute les éléments de la fabrique à la liste composant les tuilesdu centre de la table avant de remplacer celle-ci par la liste [-10]
    '''    
    _,_,fabrique = selection
    i,j = 0,0
    if fabrique == centre_table:
        return
    for lignes in fabrique:
        for elements in lignes:
            while i <= len(centre_table)-1:
                if j == len(centre_table[i]):
                    j = 0
                    i+=1
                if centre_table[i][j] == 'vide':
                    centre_table[i][j] = elements
                    break
                j+=1
    fabriques_disponibles.remove(fabrique)
    fabrique[:] = [-10]

#---------------------------------Ordinateur---------------------------------#
def tour_ordinateur(num_joueur,liste_joueurs_ia):
    if num_joueur in liste_joueurs_ia:
        return True
    return False


def ordinateur_choisir_fabrique(liste_des_fabriques):

    position_hasard = randint(1,len(liste_des_fabriques)-1)
    fabrique_hasard = liste_des_fabriques[position_hasard]
    while liste_invalide(fabrique_hasard):
        position_hasard = randint(1,len(liste_des_fabriques)-1)
        fabrique_hasard = liste_des_fabriques[position_hasard]  

    return fabrique_hasard


def ordinateur_choisir_couleur(fabrique):
    if fabrique == [-10]:
        return -10
    i = randint(0,len(fabrique)-1)
    j = randint(0,len(fabrique[i])-1)


    while fabrique[i][j] == 'vide':
        i = randint(0,len(fabrique)-1)
        j = randint(0,len(fabrique[i])-1)

    selection_ordinateur = select_tuiles(i, j, fabrique)

    remove_couleur(selection_ordinateur)
    deplacer_vers_centre(selection_ordinateur)
    dessiner_selection(selection_ordinateur,positions_plancher)
    return selection_ordinateur

def ordinateur_coup(selection_ordinateur,grille_joueur):
    colors = ["black", "yellow", "green","orange","blue"] 
    couleur, nombre, fabrique = selection_ordinateur
    colors.remove(couleur)

    while True:
        i = randint(0,len(grille_joueur)-1)
        j = randint(0,len(grille_joueur[i])-1)

        if 'vide' not in grille_joueur[i]:
            continue
        for a in range(0,len(colors)):
            if colors[a] in grille[i]:
                break
        else:
            break
    remplir_cases(selection_ordinateur, grille_joueur, i,ordinateur=True)






if __name__ == "__main__":

    #------Initialisation-------#

    nombre_joueurs = 2

    sac = sac_plein()
    centre_table = [["vide","vide","vide","vide","vide","vide","vide","vide","vide","vide"],
                    ["vide","vide","vide","vide","vide","vide","vide","vide","vide","vide"]]



                
    #Initialise les données selon le nombre de joueurs
    if nombre_joueurs >= 2:
        fabrique1 = fabriques_plein([["vide","vide"],["vide","vide"]])
        fabrique2 = fabriques_plein([["vide","vide"],["vide","vide"]])
        fabrique3 = fabriques_plein([["vide","vide"],["vide","vide"]])
        fabrique4 = fabriques_plein([["vide","vide"],["vide","vide"]])
        fabrique5 = fabriques_plein([["vide","vide"],["vide","vide"]])
        fabriques_disponibles = ['vide',fabrique1,fabrique2,fabrique3,fabrique4,fabrique5,centre_table]
        nombre_fabriques = 5

        ligne_plancher_j1 = []
        ligne_plancher_j2 = []

        grille_j1 = [["vide"], ["vide", "vide"], ["vide", "vide", "vide"], ["vide", "vide", "vide", "vide"], ["vide", "vide", "vide", "vide", "vide"]]
        grille_j2 = [["vide"], ["vide", "vide"], ["vide", "vide", "vide"], ["vide", "vide", "vide", "vide"], ["vide", "vide", "vide", "vide", "vide"]]
        positions_grille_j1 = (250,360,10,300,360,650)
        positions_plancher_j1 = (150,700)

        positions_grille_j2 = (1400,360,1160,1450,360,650)
        positions_plancher_j2 = (1300,700)
    if nombre_joueurs >= 3:
        fabrique6 = fabriques_plein([["vide","vide"],["vide","vide"]])
        fabrique7 = fabriques_plein([["vide","vide"],["vide","vide"]])
        fabriques_disponibles = [fabrique1,fabrique2,fabrique3,fabrique4,fabrique5,fabrique6,fabrique7]
        nombre_fabriques = 7
        
        ligne_plancher_j3 = []

        grille_j3 = [["vide"], ["vide", "vide"], ["vide", "vide", "vide"], ["vide", "vide", "vide", "vide"], ["vide", "vide", "vide", "vide", "vide"]]
        
    if nombre_joueurs == 4:

        fabrique8 = fabriques_plein([["vide","vide"],["vide","vide"]])
        fabrique9 = fabriques_plein([["vide","vide"],["vide","vide"]])
        fabriques_disponibles = [fabrique1,fabrique2,fabrique3,fabrique4,fabrique5,fabrique6,fabrique7,fabrique8,fabrique9]
        nombre_fabriques = 9

        ligne_plancher_j4 = []

        grille_j4 = [["vide"], ["vide", "vide"], ["vide", "vide", "vide"], ["vide", "vide", "vide", "vide"], ["vide", "vide", "vide", "vide", "vide"]]

    positions = position(nombre_fabriques)
    
    
    
    joueur_ia = [1,2]
    positions_tuiles_centre = [650,350]

    joueurs_passes = 0 
    tours = 0
    joueur = 1
    grille = grille_j1
    plancher = ligne_plancher_j1
    Tour_fini = False
    malus_centre = True


    #-------Boucle principale------#
    while True:
        dessiner_plateau(nombre_joueurs=nombre_joueurs,nombre_fabriques=nombre_fabriques)
        dessiner_tuiles_centre(centre_table)


        #Detecte si tous les joueurs sont passés alors on remet à zéro les variables nécessaires
        if joueurs_passes == nombre_joueurs:
            tours += 1
            joueurs_passes = 0
            joueur = 1
        
        #Affiche et de met à jour le nombre de fabriques selon le nombre de joueurs
        if nombre_joueurs >= 2:
            dessiner_tuiles_fabriques(fabrique1,1,positions)
            dessiner_tuiles_fabriques(fabrique2,2,positions)
            dessiner_tuiles_fabriques(fabrique3,3,positions)
            dessiner_tuiles_fabriques(fabrique4,4,positions)
            dessiner_tuiles_fabriques(fabrique5,5,positions)

            dessiner_tuiles_plancher(ligne_plancher_j1,positions_plancher_j1)
            dessiner_tuiles_plancher(ligne_plancher_j2,positions_plancher_j2)

            dessine_tuiles_lignes(grille_j1, positions_grille_j1)
            dessine_tuiles_lignes(grille_j2, positions_grille_j2)


            if fabrique1 == fabrique2 == fabrique3 == fabrique4 == fabrique5 == [-10] and liste_invalide(centre_table):
                texte(500, 500, 'FINI')
                break


            #Met à jour les variables en fonction du joueur qui doit jouer
            if joueur == 1:

                positions_grille = positions_grille_j1
                positions_plancher = positions_plancher_j1

                grille = grille_j1
                plancher = ligne_plancher_j1

            if joueur == 2:

                grille = grille_j2
                plancher = ligne_plancher_j2
                
                positions_grille = positions_grille_j2
                positions_plancher = positions_plancher_j2

        if nombre_joueurs >= 3:
            dessiner_tuiles_fabriques(fabrique6,6,positions)
            dessiner_tuiles_fabriques(fabrique7,7,positions)

            if joueur == 3:
                grille = grille_j3
                plancher = ligne_plancher_j3

        if nombre_joueurs >= 4:
            dessiner_tuiles_fabriques(fabrique8,8,positions)
            dessiner_tuiles_fabriques(fabrique9,9,positions)

            if joueur == 4:
                grille = grille_j1
                plancher = ligne_plancher_j4


        texte(positions_tuiles_centre[0]+120,positions_tuiles_centre[1]-50,"Au tour du joueur: "+str(joueur)) #Affiche quel joueur joue pour plus de clarté

        if tour_ordinateur(joueur, joueur_ia) == False: #Cas où c'est un humain qui doit jouer

            x,y,_ = attente_clic()

            if 1>=(y//50)-1 >=0:   #Si le clic se trouve dans la zone des fabriques on appelle la fonction select_fabrique
                x,y,fabrique_selectionnee = select_fabrique(x,y)
                if x == -10:
                    continue
                selection = select_tuiles(y, x, fabrique_selectionnee)

            #Si le joueur souhaite prendre des tuiles dans la zone du milieu seulement possible après le premier coup de la partie
            elif 1 >= ((y-350)//50) >= 0 and 10>=(x-650)//50>=0 and (tours != 0 or joueurs_passes !=0): 
                i = (y-350)//50
                j = (x-650)//50

                selection = select_tuiles(i,j,centre_table)
                           
            else: #Tous les autres cas on fait rien
                continue

            if selection != -10: #Si la selection est valide
                dessiner_selection(selection, positions_plancher)
                x,y,type_clic = attente_clic()
                if un_select_fabrique(type_clic): #Pour déselectionner ce qu'on a sélectionné on revient au début pour resélectionner des tuiles
                    efface_tout()
                    selection = -10
                    continue
                    
                else:
                    tour_valide = None                
                    if remplir_cases(selection,grille,y) == -10: #Détecte si la zone où le joueur veut poser ses tuiles est invalide
                        while selection !=-10: 
                            #Dans ce cas la tant que c'est invalide on garde la sélection et on attends que le joueur fasse un choix valide
                            if selection[0] == 'vide':
                                break
                            x,y,type_clic = attente_clic()
                            if un_select_fabrique(type_clic): #Il efface sa sélection on sort de la boucle
                                efface_tout()
                                tour_valide = False
                                break
                            if remplir_cases(selection, grille, y) != -10: #Son choix est valide on sort 
                                break

                        if tour_valide == 9999:
                            continue

                    efface_tout()
                    dessine_tuiles_lignes(grille, positions_grille)         

                    remove_couleur(selection) #Enleve les tuiles de la couleurs posée de la liste de la fabrique
                    deplacer_vers_centre(selection) # Vide la fabrique et déplace les tuiles restantes vers le centre

                    if selection[2] == centre_table and malus_centre == True:
                        plancher.append(-1)
                        malus_centre = False
                    Tour_fini = True
            else:
                continue

        elif tour_ordinateur(joueur, joueur_ia): #Cas où le joueur est contrôlé par l'ordinateur
            dessine_tuiles_lignes(grille, positions_grille)
            ordinateur_fabrique = ordinateur_choisir_fabrique(fabriques_disponibles)
            selection_ordinateur = ordinateur_choisir_couleur(ordinateur_fabrique)
            dessiner_selection(selection_ordinateur, positions_plancher)
            mise_a_jour()
            sleep(1)      
            ordinateur_coup(selection_ordinateur, grille)
            if selection_ordinateur[2] == centre_table and malus_centre == True:
                plancher.append(-1)
                malus_centre = False
            Tour_fini = True

        if Tour_fini:
            efface_tout()
            joueurs_passes += 1
            joueur += 1
            Tour_fini = False


attente_clic()
ferme_fenetre()
