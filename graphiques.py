from upemtk import *



'''
cercle(0,0,50)

cercle(100,75,60)  #
cercle(500, 75, 60)
cercle(900, 75, 60)
cercle(1300, 75, 60)
cercle(1700, 75, 60)

rectangle(100, 75, 150, 125)
rectangle(50, 75, 100, 125)                   # Cote = 50
rectangle(100, 25, 150, 75)
rectangle(50, 25, 100, 75)
#rectangle(ax, ay, bx, by)
'''

#----------------------Module s'occupant de générer les graphismes du jeu----------------------#

def dessiner_fabriques():
    for i in range(5):
        cercle(100+400*i,75,60,epaisseur=1)

def dessiner_grille_joueur1(): #Affiche la grille du joueur 1
    for nb_lignes in range(0,6):
        for nb_colonnes in range(0,nb_lignes):
            rectangle(250-60*nb_colonnes, 300+60*nb_lignes, 300-60*nb_colonnes, 350+60*nb_lignes)

def dessiner_grille_joueur2(): #Affiche la grille du joueur 2
    for nb_lignes in range(0,6):
        for nb_colonnes in range(0,nb_lignes):
            rectangle(1400-60*nb_colonnes, 300+60*nb_lignes, 1450-60*nb_colonnes, 350+60*nb_lignes)

def dessiner_murs_palais():
     for nb_lignes in range(0,5):
        for nb_colonnes in range(0,5):
            rectangle(350+60*nb_colonnes, 360+60*nb_lignes, 400+60*nb_colonnes, 410+60*nb_lignes)
            rectangle(1500+60*nb_colonnes, 360+60*nb_lignes, 1550+60*nb_colonnes, 410+60*nb_lignes)



def afficher_couleurs():
    pass



def dessiner_plateau():
    dessiner_fabriques()
    dessiner_grille_joueur1()
    dessiner_grille_joueur2()
    dessiner_murs_palais()
