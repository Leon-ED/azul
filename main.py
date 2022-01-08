# !/usr/bin/env python3
# -*- coding: utf-8 -*-
'''Module principal du jeu s'occupant de la partie logique et de l'interaction avec l'utilisateur.'''

#---Imports
from src.upemtk import *
from src.fichiers import *
from src.graphiques import *
from time import sleep
from random import randint
from src.menu import *
from src.generer import *


def variables_debut_jeu(nombre_joueurs):
    global liste_palais; liste_palais = generer_palais(nombre_joueurs)
    global fabriques_disponibles;fabriques_disponibles = generer_fabriques(nombre_joueurs)
    global liste_planchers;liste_planchers = generer_planchers(nombre_joueurs)
    global liste_grilles_joueurs;liste_grilles_joueurs = generer_grilles_joueurs(nombre_joueurs)
    global grille; grille = liste_grilles_joueurs[joueur-1]  
    global plancher;plancher = liste_planchers[joueur-1]

def variables_nouvelle_manche(nombre_joueurs):
    global fabriques_disponibles;fabriques_disponibles = generer_fabriques(nombre_joueurs)
    global liste_planchers; liste_planchers = generer_planchers(nombre_joueurs)
    global liste_grilles_joueurs; liste_grilles_joueurs = re_generer_grilles(liste_grilles_joueurs)


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
    '''
    if len(fabrique[0]) > 2:
        for lines in fabrique:
            for colors in lines:
                if colors != 'vide':
                    return False
        return True
    '''
    for i in range(len(fabrique)):
        if type(fabrique[i]) != list:
            return True

        if -10 in fabrique:
            return True

    return False

def fabrique_invalide(fabrique):
    if fabrique == [-10] or -10 in fabrique or type(fabrique) != list:
        return True
    for i in range(len(fabrique)):
        for j in range(len(fabrique[i])):
            if fabrique[i][j] in COULEURS_JEU:
                return False
    return True


def fabriques_vides(liste_des_fabriques):
    for fabriques in liste_des_fabriques:
        if fabriques != [-10] or -10 not in fabriques:
            return False
    return True


def select_fabrique(liste_des_fabriques,positions_tuiles_centre=[650,350],taille=50):
    '''
    Renvoie quelle fabrique a été sélectionnée

    :param int x: Position x du clic
    :param int y: Position y du clic

    :return list: Liste sélectionnée par le joueur
    '''
    x,y,_ = attente_clic()
    print(x,y)
    if 2 >= ((y-positions_tuiles_centre[1])//taille) >= 0 and 10>=(x-positions_tuiles_centre[0])//taille>=0 and (tours != 0 or joueurs_passes !=0):
        i = (y-positions_tuiles_centre[1])//taille
        j = (x-positions_tuiles_centre[0])//taille
        print("Centre table directement")
        return i,j,centre_table    
    while (x//50)-1 < 0 or (y//50)-1 <0:
        x,y,_ = attente_clic()
    i = (x//50)-1
    j = (y//50)-1
    print(i,j)
    fabrique = []
    liste_des_fabriques = liste_des_fabriques[1:-1]
    print(liste_des_fabriques)
    emplacements = [0,4,8,12,16,20,24,28,32]
    for pos in range(len(liste_des_fabriques)):
        if i == emplacements[pos] or i == emplacements[pos]+1:
            print(liste_des_fabriques[pos])
            fabrique = liste_des_fabriques[pos]
            i -= emplacements[pos]
            break
    return j,i,fabrique


def select_tuiles(i,j,fabrique,ordinateur=False):
    '''
    Renvoie les tuiles choisie par le joueur

    :param int i:
    :param int j:
    :param list fabrique:

    :return int: -10 si la sélection est invalide
    :return tuple: ('couleur',compteur,fabrique) > (str,int,list)

    '''
    if not ordinateur:
        if fabrique != centre_table and ( i>1 or liste_invalide(fabrique) or j>1):
            print("Invalide 1")
            return -10
        if fabrique == centre_table and (j>=len(fabrique[i])):
            print("Invalide 2")
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


def remove_couleur(selection):
    '''
    Supprime toutes les occurences de la couleur présente dans cette fabrique.

    :param tuple selection: ('couleur',compteur,fabrique) > (str,int,list)

    :return int: -10 si invalide
    :return None: si valide
    '''
    print(selection)
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

def remplir_cases(selection,grille,x,y,pos_grille,ordinateur=False):
    '''
    Place dans la liste de la grille les éléments sélectionnés
    Si besoin appelle la fonction remplir_plancher en cas de trop-plein.

    :param tuple selection: ('couleur',compteur,fabrique) > (str,int,list)
    :param list grille: Grille du joueur
    :param int y: position du clic y
    :param bool ordinateur: Entrer true si l'ordinateur joue

    :return int: -10 en cas d'erreur
    '''
    couleur_selection,nombre_cases,_ = selection

    if not ordinateur: #(10,10,10,10,10,10)
        i = (y-pos_grille[1])//(cote+ecart)
        px,py = positions_plancher
        #print(px,py)
        if i == 5 and (x>=px and x<=px+(cote+ecart)*7):
            #print("===============",x,y,px,py)
            remplir_plancher(couleur_selection, nombre_cases, plancher)
            return True
        '''Detecte les conditions qui font que la zone choisie n'est pas bonne'''
        if x>pos_grille[4] or x<pos_grille[2] or y > pos_grille[5] or y < pos_grille[3]:
            #print(x,y,"Pos pas bonne")
            return False
        if 'vide' not in grille[i]:
            #print(x,y,"Pas de place")
            return False
        if not coup_possible(couleur_selection, i, liste_palais[joueur-1]):
            print(f'Coup pas possible: joueur {joueur}, i={i},palais={liste_palais[joueur-1]}')
            return False
    elif ordinateur:
        i = y
        if i == 5:
            remplir_plancher(couleur_selection, nombre_cases, plancher)
            return True

    '''Calcule la taille disponible dans la ligne choisie'''
    longueur_ligne = 0
    for colors in grille[i]:
        if colors != 'vide' and colors != couleur_selection:
            #print("Ligne deja occupée")
            return False
        if colors == 'vide':
            longueur_ligne += 1
    #print("La tailles est de",longueur_ligne)

    '''S'il y a plus de cases que de place'''
    if nombre_cases > longueur_ligne:
        reste = nombre_cases - longueur_ligne
        a_placer = nombre_cases - reste
        #print(f"reste {reste} a placer {a_placer}")
        remplir_plancher(couleur_selection, reste, plancher)
        for k in range(len(grille[i])):
            if a_placer == 0:
                #print(grille[i])
                return True
            if grille[i][k] == 'vide':
                grille[i][k] = couleur_selection
                a_placer -= 1
        return True

    elif nombre_cases <= longueur_ligne:
        cases_posees = 0
        for k in range(len(grille[i])):
            if cases_posees == nombre_cases:
                return True
            if grille[i][k] == 'vide':
                grille[i][k] = couleur_selection
                cases_posees +=1
                continue
        return True


def remplir_plancher(couleur,reste,grille_plancher):
    '''
    Si son plancher n'est pas plein elle ajoute les tuiles à celui-ci.

    :param str couleur: Couleur de la tuile
    :param int reste: Nombre de tuiles à placer
    :param list grille_plancher: Liste du plancher du joueur qui joue

    :return: rien
    '''
    if len(grille_plancher) >= 7: #Plus de place dans le plancher --> selon les règles du jeu on place ces tuiles dans le couvercle
        for i in range(reste):
            couvercle.append(couleur)
        return

    for i in range(min(7-len(grille_plancher),reste)): #On boucle selon ce qui est le plus petit : le reste ou le place disponible (7)
        if len(grille_plancher) >= 7: #Dans le cas où on dépasse la taille on va dans le couvercle
            couvercle.append(couleur)
            continue
        grille_plancher.append(couleur)


def deplacer_vers_centre(selection,centre=False):
    '''
    La fonction ajoute les éléments de la fabrique à la liste composant les tuilesdu centre de la table avant de remplacer celle-ci par la liste [-10]

    :param tuple selection: couleur, nombre, fabrique

    :return: rien

    '''
    _,_,fabrique = selection
    i,j = 0,0
    if fabrique == centre_table or centre: #Si la fabrique utilisée est celle du milieu
        print("Centre table")
        return

    print(fabrique,"eeeeeeeeeeee deplacer")
    for lignes in fabrique:
        for elements in lignes:
            while i < len(centre_table)-1:
                if j == len(centre_table[i]):
                    j = 0
                    i+=1
                print(i,j)
                if centre_table[i][j] == 'vide':
                    centre_table[i][j] = elements
                    break
                j+=1
    #fabriques_disponibles.remove(fabrique)
    fabriques_disponibles.remove(fabrique) #La fabrique est vide donc on la retire de la liste (cette ligne permet l'implémentation qui fait bouger les fabriques à leur suppression)
    fabrique[:] = [-10] #On la remplace par -10 pour signaler qu'elle est vide


def jouer_couleur_grille(grille_joueur,couleur=None):
    '''
    Permet de savoir s'il est possible de placer une couleur donnée dans la grille du joueur

    :param list grille_joueur: Grille de jeu du joueur qui a le tour
    :param str couleur: Couleur sélectionnée par le joueur

    :return bool: True si impossible de joueur le coup
    :return bool: True si possible de joueur le coup

    '''
    lignes_prises = 0
    if couleur != None:
        for i in range (len(grille_joueur)):
            if 'vide' not in grille_joueur[i]:
                lignes_prises += 1
                continue
            for elems in grille_joueur[i]:
                if elems == 'vide':
                    continue
                if elems != couleur:
                    lignes_prises += 1
                    break

        if lignes_prises == len(grille_joueur):
            return True
        return False
    else:
        for i in range(len(grille_joueur)):
            if 'vide' not in grille_joueur[i]:
                lignes_prises+=1
        return lignes_prises == len(grille_joueur)


def ligne_palais_complete(palais_j):
    for i in range(len(palais_j)):
        if all([palais_j[i][j][1] for j in range(len(palais_j[i]))]):
            print(i)
            print(palais_j)
            print([palais_j[i][j][1] for j in range(len(palais_j[i]))])
            return True
        else:
            continue
    return False




def jouer_tour(joueur,plancher,grille,positions_plancher_centre,positions_grille,liste_des_fabriques,malus):
    selection = -10
    while selection == -10:
            i,j, fabrique = select_fabrique(liste_des_fabriques)
            selection = select_tuiles(i, j, fabrique)
    dessiner_selection(selection,positions_tuiles_centre,low_graphismes)
    x,y,clic = attente_clic()
    if un_select_fabrique(clic):
        selection = -10
        return False
    cases_valides = remplir_cases(selection, grille, x,y,positions_grille)
    while cases_valides == False:
        if un_select_fabrique(clic):
            return False
        #print("PaS VLIDE")
        x,y,clic = attente_clic()
        cases_valides = remplir_cases(selection, grille, x,y,positions_grille)
    if selection[2] == centre_table and malus:
        if len(plancher) >= 7:
            plancher[-1] = -1
        else:
            plancher.append(-1)
            global malus_centre
        malus_centre = False
    remove_couleur(selection)
    deplacer_vers_centre(selection)
    dessiner_tuiles_plancher(plancher, return_positions(joueur, 1),low_graphismes)
    efface("fin_tour")
    efface("selection")
    return True

def un_select_fabrique(type_clic):
    '''Return True si le clic est un clic droit. False sinon.'''
    if type_clic == 'ClicDroit':
        efface("selection")
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
    print(len(liste_des_fabriques)-1)
    print(liste_des_fabriques)
    position_hasard = randint(1,len(liste_des_fabriques)-1)
    fabrique_hasard = liste_des_fabriques[position_hasard]
    erreur = 0
    while fabrique_invalide(fabrique_hasard):
        position_hasard = randint(1,len(liste_des_fabriques)-1)
        fabrique_hasard = liste_des_fabriques[position_hasard]
        if erreur == 50:
            print(f"/!\  Jeu : Ordinateur choisir fabrique : Erreur l'ordinateur ne sait pas ou choisir après {erreur} essais")
            fabrique_hasard = centre_table
            break
        erreur += 1
    print(fabrique_hasard)
    return fabrique_hasard


def ordinateur_choisir_couleur(fabrique):
    '''
    L'ordinateur choisit une tuile au hasard parmi la fabrique donnée

    :param list fabrique: Fabrique dans laquelle l'ordinateur va choisir aléatoirement

    :return tuple selection_ordinateur: ('couleur',nombre,[fabrique])
    '''
    i = randint(0,len(fabrique)-1)
    j = randint(0,len(fabrique[i])-1)
    print(fabrique)
    while fabrique[i][j] not in COULEURS_JEU:
        # print(fabrique[i][j])
        i = randint(0,len(fabrique)-1)
        j = randint(0,len(fabrique[i])-1)
    selection_ordinateur = select_tuiles(i, j, fabrique,ordinateur=True)
    print("selec ordi",selection_ordinateur)
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
                print(f"/!\  Jeu : L'ordinateur n'a pas pu trouver de ligne après {fail} essais.")
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

def remplir_palais(lst_palais,lst_grilles,liste_planchers):
    '''Remplit le palais à la fin de la manche si les lignes sont complétées.'''
    m = 0
    for grille_j in lst_grilles:
        palais_j = lst_palais[m]
        for i in range(len(grille_j)):
            if 'vide' not in grille_j[i]: #La ligne est remplie donc on remplit le palais
                # print("LIGNE :",grille_j[i])
                remplir_couvercle(grille_j[i],len(grille_j[i])-1,liste_planchers)
                # print('couvercle :',couvercle)
                # liste_score[m-1]+=1
                k = cherche_couleur_palais(palais_j,grille_j[i][0], i)
                palais_j[i][k][1] = True
                calculer_score(liste_planchers,i=i,j=k,palais=palais_j,joueur=m)
                afficher_mur_palais(m+1, palais_j,i,k)
        m+=1
        #print(palais)


def remplir_couvercle(ligne_j,n,liste_planchers,plancher=False):
    '''Remplit le couvercle du plateau avec les tuiles restantes pour les réutiliser'''
    if plancher:
        for couleurs in ligne_j:
            if couleurs != -1:
                couvercle.append(couleurs)
    else:
        couleur = ligne_j[0]
        print("COULEUR",couleur)
        for i in range(len(ligne_j)-1):
            print(i,ligne_j[i])
            couvercle.append(couleur)
    print("Le couvercle contient :", len(couvercle)," tuiles")

def cherche_couleur_palais(palais_j,couleur,i):
    '''Retourne la position j du palais de la couleur indiquée'''
    if i >= len(palais_j):
        return False
    for j in range(len(palais_j[i])):
        if palais_j[i][j][0] == couleur:
            return j


def test_manche_finie(liste_fabriques,centre_table):
    for fabriques in liste_fabriques[1:]:
        if not liste_invalide(fabriques):
            return False
    if not liste_invalide(centre_table):
        return False
    return True

def coup_possible(couleur,i,palais_j):
    '''Retourne True si cette couleur n'est pas déjà dans le palais et False s\'il l\'est déjà indiquant qu'on ne peut plus jouer cette couleur'''
    j = cherche_couleur_palais(palais_j, couleur, i)
    return not palais_j[i][j][1]


def fin_partie(lst_grilles,lst_palais,liste_des_fabriques):
    print("Jeu : Test si la partie est finie : ",end="")
    if any([ligne_palais_complete(palais) for palais in lst_palais]):
        print("Une ligne d'une palais a été complété.")
        return True
    if sac_est_vide() and couvercle == [] and fabriques_vides(liste_des_fabriques):
        print(f"Le sac est vide. Il possède {len(sac)} tuiles ! ")
        return True
    print("La partie n'est pas finie.")

    return False

def cree_sous_matrice(i,j,mat):
    '''Retourne une sous_matrice de la matrice mat mais sous forme de liste'''
    sous_mat = [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]
    sous_mat_valide = []
    for i,j in sous_mat:
        if not offset(mat,i,j):
            sous_mat_valide.append((i,j))
    return sous_mat_valide
def offset(m,i,j):
    '''Retourne True si position en dehors de la matrice m sinon retourne... False'''
    i_max = len(m)-1
    j_max = len(m[0])-1

    if i>i_max :
        return True
    if 0>i:
        return True
    if j>j_max:
        return True
    if 0>j:
        return True
    return False


def cases_voisines_vides(palais,i,j):
    '''Retourne True si l\'élément indiqué ne possède aucun voisins'''
    voisins = cree_sous_matrice(i,j,palais)
    for i,j in voisins:
        print(i,j)
        if palais[i][j][1] == True:
            return False
    return True


def calculer_score(liste_planchers,i=None,j=None,palais=None,fin_partie=False,fin_manche=False,joueur = 0,liste_palais=None):
    '''Calcule le score des joueurs pendant la partie et à la fin de la partie'''
    global liste_score
    if not fin_partie and fin_manche:
        #efface("score")
        joueur = 0
        #------ Retire les points en fonction des éléments dans le plancher
        liste_malus = [-1,-1,-2,-2,-2,-3,-3]
        for planchers in liste_planchers:
            for _,malus in zip(planchers,liste_malus):
                liste_score[joueur] += malus
                print(liste_score[joueur])
            joueur += 1
        #afficher_scores(liste_score,nombre_joueurs)
    elif not fin_partie and not fin_manche:
        if cases_voisines_vides(palais,i,j): #Si le case indiquée ne possède aucun voisins on ajoute juste un point
            liste_score[joueur] += 1
            return

        compteur = 0
        points = 0
        print("====== Points du joueur ",joueur+1," ======","pour la tuile",palais[i][j][0]," placée en ligne : ",i+1)
        if not offset(palais,i+1,j) and palais[i+1][j][1] or not offset(palais,i-1,j) and palais[i-1][j][1]:
            for k in range(0,len(palais)):
                if palais[k][j][1]:
                    compteur += 1
                if k == i:
                    points += compteur
                if not palais[k][j][1]:
                    compteur = 0
                if not palais[k][j][1] and k > i:
                    break
            print(" Verticalement : ",points," points")
        compteur = 0
        if not offset(palais,i,j+1) and palais[i][j+1][1] or not offset(palais,i,j-1) and palais[i][j-1][1]:
            for k in range(0,len(palais[i])):
                if palais[i][k][1]:
                    compteur += 1
                if k == j:
                    points += compteur
                if not palais[i][k][1]:
                    compteur = 0
                if not palais[i][k][1] and k > j:
                    break
            print("Total, ",points)
        liste_score[joueur] += points
        return
    elif fin_partie:
        #efface("score")
        joueur = 0
        for palais in liste_palais:
            points = 0
            for k in range(0,len(palais)):
                if all([palais[i][k][1] for i in range(len(palais[k]))]): #Verification si les colonnes sont remplies
                    points += 7
                if all([palais[k][j][1] for j in range(len(palais[k]))]): #Verification si les lignes sont remplies
                    points += 2 #Le joueur a remplie toute une ligne ou colonne il gagne 2 ou 7 points supplémentaires
            
            for couleur in COULEURS_JEU:
                compteur = 0
                for i in range(len(palais)):
                    k = cherche_couleur_palais(palais,couleur,i)
                    if compteur == 5:
                        points += 10 #Le joueur 5 fois la meme couleur dans son palais il gagne 10 points supplémentaires
                    if palais[i][k][1]:
                        compteur += 1
            liste_score[joueur] += points
            joueur += 1
        #afficher_scores(liste_score,nombre_joueurs)
def determiner_vainqueur(liste_scores):
    '''Retourne le numéro du joueur avec le plus de points'''
    score_maximul = max(liste_scores)
    return liste_scores.index(score_maximul)


if __name__ == "__main__":
    chemin_settings = "./files/settings.txt"
    chemin_save = "./files/save.txt"
    '''
    Tour : Se finit quand tous les joueurs composant la partie on joué
    Manche : Se finit quand il n'y a plus de fabriques avec lesquelles jouer
    '''
    while not menu_jeu(chemin_settings):pass #On affiche le menu
    cree_fenetre(1800,1080) #On crée la fenêtre du jeu
    sac_plein() #On crée le sac
    global fabriques_disponibles
    nombre_joueurs,joueur_ia,low_graphismes,reload = lire_config(chemin_settings) #On lit les paramètres du jeu depuis le fichier
    if reload == True: #Pour être bien sûr qu'il soit égal à True
        ''' On lit la sauvegarde si le joueur a choisi l'option reprendre la partie'''
        save = copy_file(chemin_save)
        print("Jeu : Chargement de la partie depuis la dernière sauvegarde")
        _,nombre_joueurs,joueur,joueur_ia,joueurs_passes,liste_grilles_joueurs,\
        liste_planchers,centre_table,fabriques_disponibles,liste_palais,malus_centre,\
        liste_score,partie_finie,tour_fini,sac,couvercle,tours,manche_finie = save #Initialisation des données selon le fichier de sauvegarde

    else:
        variables_debut_jeu(nombre_joueurs)


    #------Dessine les éléments à ne jamais effacer-------#
    '''Cela permet de ne pas à devoir les réafficher à chaque tour augmentant ainsi les performances.'''
    dessiner_tout_planchers(liste_planchers)
    dessiner_tout_palais(liste_palais,low_graphismes)
    dessiner_tout_grilles_joueurs(liste_grilles_joueurs)
    afficher_tout_palais(liste_palais,low_graphismes)


    #------Boucle principale-------#
    while True:
    #------Met à jour les éléments relatifs au joueur qui joue-------#
        positions_plancher = return_positions(joueur, 1)
        positions_grille = return_positions(joueur, 0)
        grille = liste_grilles_joueurs[joueur-1]
        plancher = liste_planchers[joueur-1]
        '''Affiche les éléments graphiques qui changent tous les tours'''
        afficher_tour(centre_table,low_graphismes,fabriques_disponibles,liste_grilles_joueurs,positions_tuiles_centre,joueur)
        afficher_scores(liste_score,nombre_joueurs)
        '''Cas où un humain doit jouer'''
        if not tour_ordinateur(joueur, joueur_ia) and not partie_finie and not tour_fini and not manche_finie:
            print(len(couvercle),"COUVRR")
            while not tour_fini:
                 tour_fini = jouer_tour(joueur, plancher, grille, positions_plancher, positions_grille, fabriques_disponibles,malus_centre)
        
            '''Cas où l'ordinateur doit jouer'''
        elif tour_ordinateur(joueur, joueur_ia) and not partie_finie and not tour_fini and not manche_finie:
            mise_a_jour()
            positions_grille = return_positions(joueur, 0)
            # dessine_tuiles_lignes(grille, joueur,low_graphismes)
            ordinateur_fabrique = ordinateur_choisir_fabrique(fabriques_disponibles)
            selection_ordinateur = ordinateur_choisir_couleur(ordinateur_fabrique)
            dessiner_selection(selection_ordinateur, positions_tuiles_centre,low_graphismes)
            mise_a_jour()
            sleep(0.7)
            efface("selection")
            ordinateur_coup(selection_ordinateur, grille,positions_grille,palais)
            if selection_ordinateur[2] == centre_table and malus_centre == True:
                plancher.append(-1)
                malus_centre = False
            dessiner_tuiles_plancher(plancher,return_positions(joueur,1),low_graphismes)
            mise_a_jour()
            tour_fini = True
        if fin_partie(liste_grilles_joueurs,liste_palais,fabriques_disponibles):
            calculer_score(liste_planchers,fin_partie=True,liste_palais=liste_palais)
            generer_fin_partie(liste_planchers,liste_palais,liste_score,nombre_joueurs)
            afficher_scores(liste_score,nombre_joueurs)
            attente_clic()
            attente_clic()
            break
        if tour_fini:
            efface("fin_tour")
            joueurs_passes += 1
            joueur += 1
            tour_fini = False
        if joueurs_passes >= nombre_joueurs:
            tours+=1
            joueurs_passes = 0
            joueur = 1
        if test_manche_finie(fabriques_disponibles, centre_table) or manche_finie:
            generer_fin_manche(liste_planchers,couvercle,liste_palais,liste_grilles_joueurs,nombre_joueurs,tours)
            variables_nouvelle_manche(nombre_joueurs)
            malus_centre = True
            joueurs_passes = 0
            joueur = 1

        #---------A chaque fin de tour on sauvegarde la partie---------------#
        ecrire_save(nombre_joueurs,joueur,joueur_ia,joueurs_passes,liste_grilles_joueurs,liste_planchers,centre_table,fabriques_disponibles,liste_palais,malus_centre,liste_score,partie_finie,tour_fini,sac,couvercle,tours,manche_finie)

