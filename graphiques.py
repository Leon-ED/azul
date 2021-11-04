from upemtk import *

#----------------------Module s'occupant de générer les graphismes de début de jeu----------------------#

cote_carre = 50
largeur_fenetre = 1800
hauteur_fenetre = 900

def dessiner_fabriques(nombre_fabriques):
    '''
    Dessine les  cercles des fabriques en haut de l'écran
    '''
    ecart = largeur_fenetre/nombre_fabriques
    for i in range(nombre_fabriques):
        cercle(100+ecart*i,75,60,epaisseur=1)




def dessiner_lignes_motif(nombre_joueurs): #Affiche les lignes du motif
    '''
    Dessine les lignes de motif des deux joueurs.
    '''
    for nb_lignes in range(0,6):
        for nb_colonnes in range(0,nb_lignes):
            rectangle(250-60*nb_colonnes, 300+60*nb_lignes, 300-60*nb_colonnes, 350+60*nb_lignes) #Joueur 1
            rectangle(1400-60*nb_colonnes, 300+60*nb_lignes, 1450-60*nb_colonnes, 350+60*nb_lignes) #Joueur 2

def dessiner_murs_palais(nombre_joueurs):
    '''
    Dessine les murs du palais des deux joueurs.
    '''   
    for nb_lignes in range(0,5):
        for nb_colonnes in range(0,5):
            rectangle(350+60*nb_colonnes, 360+60*nb_lignes, 400+60*nb_colonnes, 410+60*nb_lignes)
            rectangle(1500+60*nb_colonnes, 360+60*nb_lignes, 1550+60*nb_colonnes, 410+60*nb_lignes)



def dessiner_plancher(nombre_joueurs):
    '''
    Dessine les lignes de plancher des deux joueurs
    '''
    for i in range(7):
        rectangle(150+50*i, 700, 200+50*i, 750)
        rectangle(1300+50*i, 700, 1350+50*i, 750)

def dessiner_tuiles_plancher(liste_plancher,index_plancher):
    if "vide" in liste_plancher or len(liste_plancher) == 0:
        return
    print("FONCTION DESSINER TUILES PLANCEHR")
    i = 0   
    for colors in liste_plancher:
        rectangle(index_plancher[0]+50*i, index_plancher[1], (index_plancher[0]+50)+50*i, (index_plancher[1]+50),remplissage=colors)
        i+=1
        #rectangle(50+50*i,800,100+50*i,850,remplissage='black',couleur='black')


def dessiner_tuiles_centre(liste_centre):
    i = 0
    j = 0
    for lines in liste_centre:
        for colors in lines:
            if colors == -1 or 'vide':
                continue
            if i == 10:   #Détermine le nombre d'éléments au maximum sur une ligne
                i = 0
                j +=1
            rectangle(650+50*i, 400+50*j, 700+50*i, 350+50*j,remplissage=colors,couleur='black')
            i += 1


def dessiner_selection(selection,index_plancher):
    couleur,nombre,_ = selection
    for i in range(nombre):
        rectangle(index_plancher[0]+50*i, index_plancher[1]+60, (index_plancher[0]+50)+50*i, (index_plancher[1]+110),remplissage=couleur)


def dessiner_tuiles_fabriques(fabrique,i,liste_positions):
    '''
    Prend en paramètre une liste de couleur et dessine les rectangles
    de chaque couleur de cette liste.
    '''
    if -10 in fabrique:
        return
    ecart = 200
    #print(liste_positions)
    j = 0
    ligne = 0
    x = liste_positions[i-1]
    for line in fabrique:
        for colors in line:
            if j == 2:
                j = 0
                ligne = 1
            rectangle(x+50*j, 50+50*ligne, (x+50)+50*j, 100+50*ligne,remplissage=colors,couleur='black',epaisseur=2)
            
            j+=1   

def dessine_tuiles_lignes(grille,index):
    #j = (y//60)-5
    for i in range(len(grille)):
        for j in range(i+1):
            if grille[i][j] == "vide":
                continue
            print("graphique, dessine_tuiles_grilles",grille)
            rectangle(index[0]-60*j, index[1]+60*i, (index[0]+50)-60*j, (index[1]+50)+60*i,remplissage=grille[i][j])
            
    '''
    i,j = -1,0
    for lines in grille:
        i+=1
        j = 0
        for colors in lines:
            if colors == 'vide':
                j+=1
                continue
            rectangle(250-60*j, 360+60*i+1, 300-60*j, 410+60*i+1,remplissage=grille[i][j])
        
    '''


def dessiner_plateau(nombre_joueurs,nombre_fabriques):
    '''
    Permet de dessiner tous les éléments du jeu en une seule fois en regroupant
    toutes les autres fonctions.
    '''
    #dessiner_fabriques(nombre_fabriques)
    dessiner_lignes_motif(nombre_joueurs)
    dessiner_murs_palais(nombre_joueurs)
    dessiner_plancher(nombre_joueurs)


def position(nombre_fabriques):
    ecart = 200
    liste_positions = [50]
    for i in range(1,nombre_fabriques):
        liste_positions.append(liste_positions[i-1]+ecart)
    return liste_positions


