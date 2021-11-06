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

def plus_de_tuiles():
    '''
    Retourne True s'il n'y a plus de tuiles en jeu (fabriques et centre du plateau) sinon False
    '''
    if fabrique1 == fabrique2 == fabrique3 == fabrique4 == fabrique5 == [-10] and len(centre_table) == 0:
        return True
    return False

def liste_invalide(fabrique):
    '''
    Prend en paramètre une liste(fabrique) et renvoie True si elle est invalide
    c'est à dire si sa taille est nulle ou que son type n'est pas une liste sinon renvoie False.
    '''
    for i in range(len(fabrique)):
        if type(fabrique[i]) != list:
            print("pas liste")
            return True

        if -10 in fabrique:
            return True
    for lines in fabrique:
        for colors in lines:
            if colors != 'vide':
                return False

    return False

def select_fabrique(x,y):
    '''
    Prends en paramètres les coordonnées d'un clic puis renvoie la fabrique correspondante au clic
    selon le nombre de fabriques (lié au nombre de joueur) et renvoie l'indice i et j ainsi que la liste (fabrique)
    sélectionnée. 
    '''
    i = (x//50)-1
    j = (y//50)-1
    #print("Select fabrique i et j",i,j)
    fabrique = []
    selection = []
    emplacements = []
    if i < 0 or j<0:
        return -10,-10,-10
    if nombre_joueurs >=2:
        if i == 0 or i==1:
            #print("Fabrique 1")
            fabrique = fabrique1

        if i == 4 or i==5:
            i-=4
            #print("Fabrique 2")
            fabrique = fabrique2

        if i == 8 or i==9:
            i-=8
            #print("Fabrique 3")
            fabrique = fabrique3

        if i == 12 or i==13:
            i-=12
            #print("Fabrique 4")
            fabrique = fabrique4

        if i == 16 or i==17:
            i-=16
            #print("Fabrique 5")
            fabrique = fabrique5

    if nombre_joueurs >=3:
        if i == 20 or i==21:
            i-=20
            #print("Fabrique 6")
            fabrique = fabrique6

        if i == 24 or i==25:
            i-=24
            #print("Fabrique 7")
            fabrique = fabrique7

    if nombre_joueurs >= 4:

        if i == 28 or i==29:
            i-=28
            #print("Fabrique 8")
            fabrique = fabrique8
        
        if i == 32 or i==33:
            i-=32
            #print("Fabrique 9")
            fabrique = fabrique9
    return i,j,fabrique


def select_tuiles(i,j,fabrique):
    '''
    Prend en paramètres les indices i et j et une liste (fabrique) renvoie la couleur ainsi que le nombre
    d'occurence de la couleur dans la fabrique ainsi que la fabrique. Si cela ne correspond à rien la fonction renvoie
    -10
    '''
    #print("i et j",i,j)
    #print(fabrique)
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

def clic():
    '''
    Retourne la position x,y du clic de l'utilisateur.
    '''
    x, y, _ = attente_clic()
    return x, y

def remplir_cases(selection,grille,y,ordinateur=False):
    '''
    Prends en paramètre la sélection composée de la couleur de la tuile, du nombre d'occurence de cette couleur et la liste (fabrique)
    d'où viennent ces tuiles. Ainsi que la grille du joueur en train de jouer et la position y du clic de l'utilisateur.
    La fonction renvoie -10 si les coordonnées du clic de sont pas bonnes. Sinon elle place dans la liste de la grille les éléments sélectionnés
    et s'il le faut appelle la fonction remplir_plancher afin de traiter les cas où plus de tuiles sont sélectionnées qu'il n'y a de place sur la ligne choisie.
    '''
    couleur,nombre,_ = selection
    #positions_grille_j1 = (250,360,10,300,360,650)
    if ordinateur == False:
        if (y < positions_grille[4] or y > positions_grille[5]): #Detecte sur la position y n'est pas bonne
            #print("remplir_cases: y non valide",y)
            return -10 
        if  (x<positions_grille[2] or x>positions_grille[3]): #Detecte si la position x n'est pas bonne
            #print("remplir_cases: x non valide",x)
            return -10
        y = (y//60)-6
        #print(y,'remplir cases y')
        if 'vide' not in grille[y]: #Detecte s'il n'y a plus de place dans la ligne et retourne -10 si c'est le cas
            #print("remplir_cases: Plus de place dans ligne")
            return -10

    longueur = 0
    for colors in grille[y]: #Detecte si une couleur autre est déja présente et si c'est le cas retourne -10
        if colors == 'vide':
            longueur += 1   
            continue
        if colors != couleur:
            #print("remplir_cases: Pas la bonne couleur")
            return -10
    reste = 0
    #print("Place libre: ",longueur)
    #print("remplir_cases, y = ",y)

    for i in range(0,nombre):
        if nombre> longueur:
            reste = nombre-longueur
            if i == longueur-1:
                remplir_plancher(couleur,reste,plancher)
                j=0
                while j< len(grille[y])-1 and grille[y][j] != 'vide':
                    j+=1
                grille[y][j] = couleur
                #print("remplir_cases: Il y a un reste:",reste)   ############################A enlever à la fin
                #print("remplir_cases: Grille:",grille)
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
            #print("remplir_cases: Pas de reste",grille)            
            



def remplir_plancher(couleur,reste,grille_plancher):
    '''
    Prends en paramètre, la couleur de la tuile, le nombre restant et la grille du plancher du joueur en train de jouer.
    La fonction si la grille de plancher n'est pas pleine ajoute les éléments à celle-ci
    '''
    if len(grille_plancher) != 7:
        for i in range(reste):
            grille_plancher.append(couleur)
    #print("remplir plancher",grille_plancher) ############################A enlever à la fin


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
    #print(fabriques_disponibles,"1 --------------")
    fabrique[:] = [-10]
    #print(fabriques_disponibles,"2 --------------")


#---------------------------------Ordinateur---------------------------------#
def tour_ordinateur(num_joueur,liste_joueurs_ia):
    if num_joueur == 2:
        return True
    return False


def ordinateur_choisir_fabrique(liste_des_fabriques):

    position_hasard = randint(1,len(liste_des_fabriques)-1)
    print(position_hasard,"pos hasard")
    fabrique_hasard = liste_des_fabriques[position_hasard]
    print(fabrique_hasard)



    return fabrique_hasard



def ordinateur_choisir_couleur(fabrique):
    if fabrique == [-10]:
        return -10
    ia_i = randint(0,len(fabrique)-1)
    ia_j = randint(0,len(fabrique[ia_i])-1)


    while fabrique[ia_i][ia_j] == 'vide':
        print("case vide couleur")
        ia_i = randint(1,len(fabrique)-1)
        ia_j = randint(0,len(fabrique[ia_i])-1)
        print(fabrique)

    print(ia_i,ia_j)
    selection_ordinateur = select_tuiles(ia_i, ia_j, fabrique)

    remove_couleur(selection_ordinateur)
    deplacer_vers_centre(selection_ordinateur)
    return selection_ordinateur

def ordinateur_coup(selection_ordinateur,grille_joueur):
    colors = ["black", "yellow", "green","orange","blue"] 
    couleur, nombre, fabrique = selection_ordinateur
    colors.remove(couleur)


    while True:
        print("mauvaise coup")
        ia_i = randint(0,len(grille_joueur)-1)
        ia_j = randint(0,len(grille_joueur[ia_i])-1)

        if 'vide' not in grille_joueur[ia_i]:
            continue
        if grille_joueur[ia_i][ia_j] in colors:
            continue
        break
    print(grille_joueur,"grille")
    remplir_cases(selection_ordinateur, grille, ia_i,ordinateur=True)





    '''

    colors = ["black", "yellow", "green","orange","blue"]   
def coup(fabrique,grille_joueur):
    colors = ["black", "yellow", "green","orange","blue"]
    if fabrique == [-10]:
        return
    i = randint(0,1)
    j = randint(0,1)
    selection= select_tuiles(i, j, fabrique)
    colors.remove(selection[0])
    #print(grille_joueur)
    #print(selection)
    while True:
        i = randint(0, len(grille_joueur)-1)
        j = randint(0,len(grille_joueur[i])-1)
        #print("i= ",i,"j= ",j)
        if 'vide' not in grille_joueur[i]:
            #print("vide")
            continue
        if grille_joueur[i][j] in colors:
            #print("couleur deja la")
            continue


        break
    efface_tout()
    #print(remplir_cases(selection, grille, i,True),'remplir cases bot')
    dessine_tuiles_lignes(grille, positions_grille)
    remove_couleur(selection)
    deplacer_vers_centre(selection)
    dessiner_tuiles_centre(centre_table)
    '''




 


if __name__ == "__main__":

    joueur_ia = menu_azul()
    ferme_fenetre()
    cree_fenetre(1800,900)
     
    #------Initialisation-------#

    nombre_joueurs = 2

    sac = sac_plein()
    centre_table = [["vide","vide","vide","vide","vide","vide","vide","vide","vide","vide"],
                    ["vide","vide","vide","vide","vide","vide","vide","vide","vide","vide"],
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
        #(x et y 1er carré coin gauche supérieur, largeur totale de la + grande ligne, et hauteur totale )
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
    
    
    
    
    positions_tuiles_centre = [650,350]

    joueurs_passes = 0 
    tours = 0
    joueur = 1
    grille = grille_j1
    plancher = ligne_plancher_j1
    Tour_fini = False

    #-------Boucle principale------#
    while True:
        dessiner_plateau(nombre_joueurs=nombre_joueurs,nombre_fabriques=nombre_fabriques)
        dessiner_tuiles_centre(centre_table)
        #Detecte si un tour est finit dans ce cas là remet à zéro les variables pour le tour suivant
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

            print(centre_table)

            if fabrique1 == fabrique2 == fabrique3 == fabrique4 == fabrique5 == [-10] and liste_invalide(centre_table):
                print("Fini")
                break


            #Met à jour les variables en fonction du joueur qui doit jouer
            if joueur == 1:
                texte(positions_tuiles_centre[0],positions_tuiles_centre[1]-70,"1")
                positions_grille = positions_grille_j1
                positions_plancher = positions_plancher_j1

                grille = grille_j1
                plancher = ligne_plancher_j1

            if joueur == 2:
                texte(positions_tuiles_centre[0],positions_tuiles_centre[1]-70,"2")
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







        if tour_ordinateur(joueur, joueur_ia):
            selection = 99999999
            ordinateur_fabrique = ordinateur_choisir_fabrique(fabriques_disponibles)

            selection_ordinateur = ordinateur_choisir_couleur(ordinateur_fabrique)

            ordinateur_coup(selection_ordinateur, grille)

            dessine_tuiles_lignes(grille, positions_grille)
            Tour_fini = True
  

        else:
            #print("Le joueur qui joue est le joueur ",joueur)
            #print(centre_table)
            x,y,_ = attente_clic()
            #print(x,y)

            if 1>=(y//50)-1 >=0:   #Si le clic se trouve dans la zone des fabriques on appelle la fonction select_fabrique
                #print("Zone fabriques")
                x,y,fabrique_selectionnee = select_fabrique(x,y)
                ##print(centre_table)
                if x == -10:
                    continue
                selection = select_tuiles(y, x, fabrique_selectionnee)
                ##print(selection,"Selection")
            
            elif 1 >= ((y-350)//50) >= 0 and 10>=(x-650)//50>=0 and (tours != 0 or joueurs_passes !=0):
                i = (y-350)//50
                j = (x-650)//50
                ##print("Clic tuile centre")
                #positions_tuiles_centre = [650,350]
                #positions_tuiles_centre = [700,400]
                ##print((((y-350)//50)),((x-650)//50))
                ##print(i,j)
                selection = select_tuiles(i,j,centre_table)
                

            else:
                ##print(((y-350)//50) -1)
                ##print("Else continue")
                continue




            if selection != -10: #Si la selection est valide
                dessiner_selection(selection, positions_plancher)
                ##print("pos plancher",positions_plancher)
                x,y,type_clic = attente_clic()
                if un_select_fabrique(type_clic): #Pour déselectionner ce qu'on a sélectionné (pas implémenté)
                    efface_tout()
                    ##print("if : Clic droit")
                    selection = -10
                    continue
                    
                else:
                    tour_valide = None                
                    if remplir_cases(selection,grille,y) == -10: #Détecte si le clic est invalide
                        ##print("Boucle True: Clic pas valide pour remplir cases")
                        while selection !=-10:
                            if selection[0] == 'vide':
                                break
                            ##print("true selection",selection[0])
                            x,y,type_clic = attente_clic()
                            if un_select_fabrique(type_clic):
                                efface_tout()
                                tour_valide = False
                                ##print("Boucle True: Clic droit > supp selection")
                                break
                            if remplir_cases(selection, grille, y) != -10:
                                ##print("Boucle True : Clic valide")
                                break
                        if tour_valide == False:
                            continue
                        ##print("Clic remplir_case invalide")
                        ##print("selection;",selection)


                    efface_tout() #Efface tout pour mettre à jour les graphiques
                    remove_couleur(selection) #Enleve les tuiles de la couleurs posée de la liste de la fabrique
                    deplacer_vers_centre(selection) # Vide la fabrique et déplace les tuiles restantes vers le centre
                    dessiner_tuiles_centre(centre_table) #Affiche les tuiles au centre
                    #dessine_tuiles_lignes(grille, positions_grille)
                    
                    Tour_fini = True
                    
                    
                    #Debug
                    '''
                    #print("TUILES AU CENTRE",centre_table)
                    #print("TUILES PLANCHER", plancher)
                    #print("Fabriques",fabrique1,fabrique2,fabrique3,fabrique4)
                    '''
            else:
                pass

               ##print("Selection = -10")
            
        if Tour_fini:
            efface_tout()
            joueurs_passes += 1
            joueur += 1
            Tour_fini = False



    









attente_clic()
ferme_fenetre()
