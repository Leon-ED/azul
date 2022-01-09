# !/usr/bin/env python3
# -*- coding: utf-8 -*-
'''Module qui a pour but d'afficher tous les graphismes à l'écran en fonction des données envoyées.'''

#---Imports
from src.upemtk import *
from src.menu import *

cote= 50
ecart = 10
largeur_fenetre = 1900
hauteur_fenetre = 900

def afficher_tour(centre_table,low_graphismes,fabriques_disponibles,liste_grilles_joueurs,positions_tuiles_centre,joueur):
    dessiner_tuiles_centre(centre_table,low_graphismes)
    dessiner_toutes_tuiles_fabriques(fabriques_disponibles,low_graphismes)
    dessiner_toutes_tuiles_grilles(liste_grilles_joueurs,low_graphismes)
    texte(positions_tuiles_centre[0]+120,positions_tuiles_centre[1]-50,"Au tour du joueur: "+str(joueur),police='Arial',tag="fin_tour") #Affiche quel joueur joue pour plus de clarté


def return_positions(joueur,type_pos):
    #Type pos 0 : positions grille, type_pos 1 = positions plancher, type_pos 3 = points du joueur
    dico_positions = dict()
    ##print(joueur,type_pos)
    if joueur != 0:
        dico_positions[1] =((250,200,10,210,300,500),(10,520),0)
        dico_positions[2] = ((1400,200,1160,210,1450,500),(1160,520),0)
        dico_positions[3]=  ((250,580,10,590,300,880),(10,900),0)
        dico_positions[4]=((1400,580,1160,590,1450,880),(1160,900),0)
        return dico_positions[joueur][type_pos]
def dessiner_lignes_motif(joueur): #Affiche les lignes du motif
    '''
    Dessine les lignes de motif des deux joueurs.

    :param int nombre_joueurs: Pas implémenté
    '''
    x,y,_,_,_,_= return_positions(joueur, 0)
    ##print(x,y)
    for nb_lignes in range(0,6):
        for nb_colonnes in range(0,nb_lignes):
            rectangle(x-(cote+ecart)*nb_colonnes, (y+ ((cote+ecart)*nb_lignes))-50, (x+cote)-(cote+ecart)*nb_colonnes,((y+cote)+(cote+ecart)*nb_lignes)-50)
            #rectangle(250-60*nb_colonnes, 150+60*nb_lignes, 300-60*nb_colonnes, 200+60*nb_lignes) #Joueur 1
            #rectangle(1400-60*nb_colonnes, 300+60*nb_lignes, 1450-60*nb_colonnes, 350+60*nb_lignes) #Joueur 2
            

def dessiner_plancher(joueur):
    '''
    Dessine les lignes de plancher des deux joueurs

    :param int nombre_joueurs: Pas implémenté
    '''
    malus = [-1,-1,-2,-2,-2,-3,-3]
    x,y = return_positions(joueur,1)
    for i in range(7):
        texte(x+15+(cote+ecart)*i,y-20,str(malus[i]),taille=15,police='Arial')
        rectangle(x+(cote+ecart)*i, y , (x+cote)+(ecart+cote)*i, y+cote)
        # (index_plancher[0]+50)+60*i
        '''
        texte(1175+60*i,710,str(malus[i]),taille=15,police='Arial')
        rectangle(1160+60*i, 730, 1210+60*i, 780)
        '''
def dessiner_tuiles_plancher(liste_plancher,index_plancher,low_graphismes):
    '''
    Dessine les tuiles présentes dans le plancher du joueur

    :param list liste_plancher: Liste contenant les couleurs des tuiles dans le plancher du joueur
    :param list index_plancher : Liste des positions du plancher du joueur (permet l'affichage)

    '''


    if "vide" in liste_plancher or len(liste_plancher) == 0:
        return
    i = 0   
    for colors in liste_plancher:
        if colors == -1:
            image(index_plancher[0]+60*i, index_plancher[1],'images/first.gif',ancrage='nw',tag="fin_manche")
            i+=1
            continue
        if low_graphismes:
            rectangle(index_plancher[0]+60*i, index_plancher[1], (index_plancher[0]+50)+60*i, (index_plancher[1]+50),remplissage=colors,tag="fin_manche")
        else:
            image(index_plancher[0]+(60*i)+1, index_plancher[1]+1, "./images/"+str(colors)+str("_h.gif"),ancrage="nw",tag="fin_manche")
        i+=1

def dessiner_tuiles_centre(liste_centre,low_graphismes):
    '''
    Dessine les tuiles au centre du plateau

    :param list liste_centre: Liste contenant la couleur des tuiles au centre du plateau

    '''
    nb_elem = 0
    nb_ligne = 0
    ##print(liste_centre)
    for i in range(len(liste_centre)):
        for j in range(len(liste_centre[i])):
            if nb_elem == 10:
                nb_elem = 0
                nb_ligne +=1
            if liste_centre[i][j] != 'vide':
                if low_graphismes:
                    rectangle(650+50*nb_elem, 400+50*nb_ligne, 700+50*nb_elem, 350+50*nb_ligne,remplissage=liste_centre[i][j],couleur='black',tag="fin_tour")
                else:
                    image(650+50*nb_elem, 350+50*nb_ligne, "./images/"+str(liste_centre[i][j])+str("_h.gif"),ancrage="nw",tag="fin_tour")
            nb_elem +=1

            

def dessiner_selection(selection,index_plancher,low_graphismes):
    '''
    Dessine les tuiles actuellement sélectionnées par le joueur.

    :param tuple selection: ('couleur',compteur,fabrique) > (str,int,list)
    :param list index_plancher: Liste des positions du plancher du joueur (permet l'affichage)


    '''
    couleur,nombre,_ = selection
    if couleur == 'vide':
        return
        positions_tuiles_centre[0]+120,positions_tuiles_centre[1]-50
    texte(index_plancher[0]+120, index_plancher[1]-110, "Selection:",taille=23,police='Arial',tag="selection")
    texte(index_plancher[0]+120, index_plancher[1]-80, "Clic droit pour effacer",taille=13,police='Arial',tag="selection")
    for i in range(nombre):
        if low_graphismes:
            rectangle((index_plancher[0]+290)+60*i, index_plancher[1]-110, (index_plancher[0]+340)+60*i, (index_plancher[1]-60),remplissage=couleur,tag="selection")
            continue
        image((index_plancher[0]+290)+60*i, index_plancher[1]-110, "./images/"+str(couleur)+str("_h.gif"),ancrage="nw",tag="selection")


def dessiner_toutes_tuiles_fabriques(lst_fabriques,low_graphismes):
    i = 0
    for nom_fabrique in lst_fabriques[:-1]:
        if nom_fabrique != "vide":
            dessiner_tuiles_fabriques(nom_fabrique, i,low_graphismes)
            i+=1

def dessiner_toutes_tuiles_grilles(lst_grilles,low_graphismes):
    i = 0
    ##print(lst_grilles)
    for grilles in lst_grilles:
        dessine_tuiles_lignes(grilles,i+1,low_graphismes)
        i+=1

def dessiner_tout_planchers(lst_planchers):
    i = 0
    for planchers in lst_planchers:
        dessiner_plancher(i+1)
        i+=1

def dessiner_tout_palais(lst_palais,low_graphismes):
    i = 0
    for palais in lst_palais:
        dessiner_murs_palais(i+1,low_graphismes)
        i +=1
def dessiner_tout_grilles_joueurs(liste_grilles_joueurs):
    i = 0
    for grilles in liste_grilles_joueurs:
        dessiner_lignes_motif(i+1)
        i+=1

def dessiner_tuiles_fabriques(fabrique,i,low_graphismes):
    '''
    Prend en paramètre une liste de couleur et dessine les rectangles
    de chaque couleur de cette liste.

    :param list fabrique: Liste de la fabrique a dessiner
    :param int i: Numéro de la fabrique
    :param list liste_positions: Position des fabriques dans la fenêtre
    '''
    ligne(-100,200,2200,200,epaisseur=3)
    x = 50+200*i
    cercle(x+50,100,60,epaisseur=2,tag="fin_tour")
    ##print(fabrique)
    if -10 in fabrique:
        return
    ecart = 200
    j = 0
    lignes = 0
    for line in fabrique:
        for colors in line:
            if j == 2:
                j = 0
                lignes = 1
            if colors != "vide":
                if low_graphismes:
                    rectangle(x+50*j, 50+50*lignes, (x+50)+50*j, 100+50*lignes,couleur='black',remplissage=colors,epaisseur=3,tag="fin_tour")

                else:
                        
                    image(x+50*j,50+50*lignes, "./images/"+str(colors)+str("_h.gif"),ancrage="nw",tag="fin_tour")
                    rectangle(x+50*j, 50+50*lignes, (x+50)+50*j, 100+50*lignes,couleur='black',epaisseur=3,tag="fin_tour")
            
            j+=1   

def dessiner_murs_palais(joueur,low_graphismes=True):
    '''
    Dessine les murs du palais des deux joueurs.

    :param int nombre_joueurs: Pas implémenté
    '''   
    x,y,_,_,_,_ = return_positions(joueur, 0)
    x +=70
    for nb_lignes in range(0,5):
        for nb_colonnes in range(0,5):
            couple =palais[nb_lignes][nb_colonnes]
            rectangle((x)+60*nb_colonnes, (y+10)+60*nb_lignes, (x+cote)+(cote+ecart)*nb_colonnes, (y+cote+10)+(ecart+cote)*nb_lignes,epaisseur=2)
            if low_graphismes:
                rectangle((x+15)+60*nb_colonnes, (y+10+15)+60*nb_lignes, (x+cote-15)+(cote+ecart)*nb_colonnes, (y+30+10)+(ecart+cote)*nb_lignes,epaisseur=2,couleur=couple[0],remplissage=couple[0])
            else:
                image((x)+60*nb_colonnes, (y+10)+60*nb_lignes, "./images/"+str(couple[0])+str("_l.gif"),ancrage="nw",tag=(str(joueur)+str(nb_lignes)+str(nb_colonnes)))
            #rectangle(1500+60*nb_colonnes, 360+60*nb_lignes, 1550+60*nb_colonnes, 410+60*nb_lignes)

palais = [[["blue",False],["yellow",False],["red",False],["black",False],["green",False]],
            [["green",False],["blue",False],["yellow",False],["red",False],["black",False]],
            [["black",False],["green",False],["blue",False],["yellow",False],["red",False]],
            [["red",False],["black",False],["green",False],["blue",False],["yellow",False]],
            [["yellow",False],["red",False],["black",False],["green",False],["blue",False]]]

def afficher_mur_palais(joueur,palais_j,i,j,low_graphismes):
    ##print("la")
    x,y,_,_,_,_ = return_positions(joueur, 0)
    x+=70
    ##print("la2")
    ##print("=========================",i,j)
    if low_graphismes:
        rectangle((x)+60*j, (y+10)+60*i, (x+cote)+(cote+ecart)*j, (y+cote+10)+(ecart+cote)*i,epaisseur=2,remplissage=palais[i][j][0])
    else:
        image((x)+60*j, (y+10)+60*i, "./images/"+str(palais_j[i][j][0])+str("_h.gif"),ancrage="nw")


def afficher_tout_palais(liste_palais,low_graphismes=False):
    joueur = 1
    for palais in liste_palais:
        x,y,_,_,_,_ = return_positions(joueur, 0)
        x+=70
        for i in range(len(palais)):
            for j in range(len(palais[i])):
                if palais[i][j][1]:
                    if low_graphismes:
                        rectangle((x)+60*j, (y+10)+60*i, (x+cote)+(cote+ecart)*j, (y+cote+10)+(ecart+cote)*i,epaisseur=2,remplissage=palais[i][j][0])
                    else:
                        image((x)+60*j, (y+10)+60*i, "./images/"+str(palais[i][j][0])+str("_h.gif"),ancrage="nw")

        joueur+=1
            
def afficher_scores(liste_scores,nombre_joueurs):

    for i in range(nombre_joueurs):
        x,y,_,_,_,_= return_positions(i+1, 0)
        #print(liste_scores[i])
        texte(x-200,y+20,"Score : "+str(liste_scores[i]),tag='score',police="Arial")

def dessine_tuiles_lignes(grille,joueur,low_graphismes):
    '''
    Dessine les tuiles dans la grille du joueur

    :param list grille: Grille du joueur qui joue
    :param list index: Position de la grille du joueur dans la fenêtre

    '''
    x,y,_,_,_,_= return_positions(joueur, 0)
    for nb_lignes in range(len(grille)):
        for nb_colonnes in range(nb_lignes+1):
            if grille[nb_lignes][nb_colonnes] == "vide":
                continue
            if low_graphismes:
            #rectangle(index[0]-(cote+ecart)*j, index[1]+(cote+ecart)*i, (index[0]+cote)-(cote+ecart)*j, (index[1]+cote)+(cote+ecart)*i,remplissage=grille[i][j])
                rectangle(x-(cote+ecart)*nb_colonnes, (y+(cote+ecart)*nb_lignes)+10, (x+cote)-(cote+ecart)*nb_colonnes,((y+cote)+(cote+ecart)*nb_lignes)+10,remplissage=grille[nb_lignes][nb_colonnes],tag="fin_manche")
            #rectangle(x-(cote+ecart)*nb_colonnes, (y+ ((cote+ecart)*nb_lignes))-50, (x+cote)-(cote+ecart)*nb_colonnes,((y+cote)+(cote+ecart)*nb_lignes)-50)
            else:
                image(x-(cote+ecart)*nb_colonnes,  (y+(cote+ecart)*nb_lignes)+10, "./images/"+str(grille[nb_lignes][nb_colonnes])+str("_h.gif"),ancrage="nw",tag='fin_manche')

if __name__ == "__main__":
    cree_fenetre(100,100)
    attente_clic()
    ferme_fenetre()
