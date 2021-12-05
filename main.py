# !/usr/bin/env python3
# -*- coding: utf-8 -*-
'''Module principal du jeu s'occupant de la partie logique et de l'interaction avec l'utilisateur'''

#---Imports
from upemtk import *
from graphiques import *
from time import sleep
from random import randint
from menu import *


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
    Remplit la liste de 4 couleurs parmis la liste sac et les supprime de celle-ci.

    :param list liste: Liste renvoyée avec 4 couleurs aléatoires

    :return: La liste remplie
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
    Evalue si la liste donnée est valide pour jouer.

    :param list fabrique: Fabrique ou liste à évaluer

    :return: False si on peut jouer avec. True si on ne peut pas jouer avec.
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
    Renvoie quelle fabrique a été sélectionnée

    :param int x: Position x du clic
    :param int y: Position y du clic

    :return list: Liste sélectionnée par le joueur
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
    Renvoie les tuiles choisie par le joueur

    :param int i:
    :param int j:
    :param list fabrique:

    :return int: -10 si la sélection est invalide
    :return tuple: ('couleur',compteur,fabrique) > (str,int,list)

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
    

def un_select_fabrique(type_clic):
    '''Return True si le clic est un clic droit. False sinon.'''
    if type_clic == 'ClicDroit':
        return True
    return False


    
def remove_couleur(selection):
    '''
    Supprime toutes les occurences de la couleur présente dans cette fabrique.

    :param tuple selection: ('couleur',compteur,fabrique) > (str,int,list)

    :return int: -10 si invalide
    :return None: si valide
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
    Place dans la liste de la grille les éléments sélectionnés
    Si besoin appelle la fonction remplir_plancher en cas de trop-plein.

    :param tuple selection: ('couleur',compteur,fabrique) > (str,int,list)
    :param list grille: Grille du joueur
    :param int y: position du clic y
    :param bool ordinateur: Entrer true si l'ordinateur joue

    :return int: -10 en cas d'erreur
    '''

    couleur,nombre,_ = selection
    if ordinateur == False:
        if (y//60)-6 != 6:
            if (y < positions_grille[4] or y > positions_grille[5]): #Detecte sur la position y n'est pas bonne
                return -10 
            if  (x<positions_grille[2] or x>positions_grille[3]): #Detecte si la position x n'est pas bonne

                return -10


            if 'vide' not in grille[(y//60)-6]: #Detecte s'il n'y a plus de place dans la ligne et retourne -10 si c'est le cas

                return -10
        y = (y//60)-6
    if y == 6: #Si le joueur sélectionne la ligne du plancher alors on le remplit et on arrête la fonction
        remplir_plancher(couleur, nombre, plancher)
        return

    longueur = 0
    for colors in grille[y]: #Detecte si une couleur autre est déja présente et si c'est le cas retourne -10
        if colors == 'vide':
            longueur += 1   
            continue
        if colors != couleur:

            return -10
    reste = 0

    for i in range(0,nombre):
        if nombre> longueur: #Si la place sur la ligne est inférieure au nombre de tuiles
            reste = nombre-longueur
            if i == longueur-1:
                remplir_plancher(couleur,reste,plancher) #Les tuiles en trop sont déplacées sur le plancher du joueur
                j=0
                while j< len(grille[y])-1 and grille[y][j] != 'vide': #Trouve une place où mettre la tuile sur la ligne
                    j+=1
                grille[y][j] = couleur
                return
            j=0
            while j< len(grille[y])-1 and grille[y][j] != 'vide':  #Trouve une place où mettre la tuile sur la ligne
                j+=1
            grille[y][j] = couleur 

        else: #S'il y a assez de place pour les tuiles sur la ligne
            j=0
            while j< len(grille[y])-1 and grille[y][j] != 'vide':  #Trouve une place où mettre la tuile sur la ligne
                j+=1
            grille[y][j] = couleur
            

def remplir_plancher(couleur,reste,grille_plancher):
    '''
    Si son plancher n'est pas plein elle ajoute les tuiles à celui-ci.

    :param str couleur: Couleur de la tuile
    :param int reste: Nombre de tuiles à placer
    :param list grille_plancher: Liste du plancher du joueur qui joue

    :return: rien
    '''
    if len(grille_plancher) >= 7:
        return
    
    for i in range(min(7-len(grille_plancher),reste)):
        grille_plancher.append(couleur)


def deplacer_vers_centre(selection):
    '''
    La fonction ajoute les éléments de la fabrique à la liste composant les tuilesdu centre de la table avant de remplacer celle-ci par la liste [-10]

    :param tuple selection: couleur, nombre, fabrique

    :return: rien

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


def grille_pleine(grille_joueur,couleur):
    '''
    Permet de savoir s'il est possible de placer une couleur donnée dans la grille du joueur

    :param list grille_joueur: Grille de jeu du joueur qui a le tour
    :param str couleur: Couleur sélectionnée par le joueur

    :return bool: True si impossible de joueur le coup
    :return bool: True si possible de joueur le coup

    '''
    lignes_prises = 0
    for i in range (len(grille_joueur)):
        if 'vide' not in grille_joueur[i]:
            lignes_prises += 1
            continue
        for elems in grille_joueur[i]:
            if elems == 'vide':
                continue
            if elems != couleur:
                print(grille_joueur[i],couleur)
                lignes_prises += 1               
                break
                
    if lignes_prises == len(grille_joueur):
        return True
    return False


#---------------------------------Ordinateur---------------------------------#
def tour_ordinateur(num_joueur,liste_joueurs_ia):
    '''
    Permet de savoir si l'ordinateur doit jouer

    :param int num_joueur: numéro du joueur qui joue
    :param list liste_joueurs_ia: liste des joueurs contrôlés par l'ordinateur

    :return: True si l'ordinateur doit jouer. False sinon.
    '''
    if num_joueur in liste_joueurs_ia:
        return True
    return False


def ordinateur_choisir_fabrique(liste_des_fabriques):
    '''
    Permet à l'ordinateur de choisir aléatoirement une fabrique.

    :param list liste_des_fabriques: Liste de toutes les fabriques disponibles (non vides) et des tuiles au milieu

    :return: la fabrique choisie
    '''

    position_hasard = randint(1,len(liste_des_fabriques)-1)
    fabrique_hasard = liste_des_fabriques[position_hasard]
    while liste_invalide(fabrique_hasard):
        position_hasard = randint(1,len(liste_des_fabriques)-1)
        fabrique_hasard = liste_des_fabriques[position_hasard]  

    return fabrique_hasard


def ordinateur_choisir_couleur(fabrique):
    '''
    L'ordinateur choisit une tuile au hasard parmi la fabrique donnée

    :param list fabrique: Fabrique dans laquelle l'ordinateur va choisir aléatoirement

    :return tuple selection_ordinateur: ('couleur',nombre,[fabrique]) 
    '''
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
    '''
    L'ordinateur choisit une ligne aléatoirement parmi grille_joueur et y place ses tuiles

    :param tuple selection_ordinateur: ('couleur',nombre,[fabrique])
    :param list grille_joueur: Grille dans laquelle l'ordinateur va placer ses tuiles (selection_ordinateur)
    '''
    colors = ["black", "yellow", "green","orange","blue"] 
    couleur, nombre, fabrique = selection_ordinateur
    colors.remove(couleur)
    i_min = 0
    i_max = 4
    if grille_pleine(grille_joueur,couleur):
        i = 6
    else:
        while True :
            i = randint(i_min,i_max)
            if 'vide' not in grille_joueur[i]:
                continue
            for a in range(0,len(colors)):
                if colors[a] in grille[i]:
                    break
            else:
                break
    remplir_cases(selection_ordinateur, grille_joueur, i,ordinateur=True)


if __name__ == "__main__":
    fermeture = False

    joueur_ia = menu_azul()
    if joueur_ia == None:
        fermeture = True
        ferme_fenetre()
    else:
        ferme_fenetre()
        cree_fenetre(1800,900)

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
        positions_plancher_j1 = (10,730)

        positions_grille_j2 = (1400,360,1160,1450,360,650)
        positions_plancher_j2 = (1160,730)
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
    
    
   
    positions_tuiles_centre = [650,350]

    joueurs_passes = 0 
    tours = 0
    joueur = 1
    grille = grille_j1
    plancher = ligne_plancher_j1
    Tour_fini = False
    malus_centre = True


    #-------Boucle principale------#
    while fermeture == False:

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
                texte((1800/2)-100, 900/2, 'Manche terminée',police='Arial')
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


        texte(positions_tuiles_centre[0]+120,positions_tuiles_centre[1]-50,"Au tour du joueur: "+str(joueur),police='Arial') #Affiche quel joueur joue pour plus de clarté

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

                        if tour_valide == False: #Permet de revenir au début de la phase de sélection de la tuile. Sinon on continue
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
            sleep(0.9)      
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



if fermeture:
    print("Menu fermé")
else:
    print("Fin du jeu")
    attente_clic()
    ferme_fenetre()