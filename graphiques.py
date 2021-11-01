from upemtk import *

#----------------------Module s'occupant de générer les graphismes de début de jeu----------------------#

#Cote d'un carré: 50

def dessiner_fabriques():
    '''
    Dessine les 5 cercles des fabriques en haut de l'écran
    '''
    for i in range(5):
        cercle(100+400*i,75,60,epaisseur=1)

def dessiner_lignes_motif(): #Affiche les lignes du motif
    '''
    Dessine les lignes de motif des deux joueurs.
    '''
    for nb_lignes in range(0,6):
        for nb_colonnes in range(0,nb_lignes):
            rectangle(250-60*nb_colonnes, 300+60*nb_lignes, 300-60*nb_colonnes, 350+60*nb_lignes) #Joueur 1
            rectangle(1400-60*nb_colonnes, 300+60*nb_lignes, 1450-60*nb_colonnes, 350+60*nb_lignes) #Joueur 2

def dessiner_murs_palais():
    '''
    Dessine les murs du palais des deux joueurs.
    '''   
    for nb_lignes in range(0,5):
        for nb_colonnes in range(0,5):
            rectangle(350+60*nb_colonnes, 360+60*nb_lignes, 400+60*nb_colonnes, 410+60*nb_lignes)
            rectangle(1500+60*nb_colonnes, 360+60*nb_lignes, 1550+60*nb_colonnes, 410+60*nb_lignes)



def dessiner_plancher():
    '''
    Dessine les lignes de plancher des deux joueurs
    '''
    for i in range(8):
        rectangle(250-50*i, 900, 300-50*i, 1050)



def dessiner_plateau():
    '''
    Permet de dessiner tous les éléments du jeu en une seule fois en regroupant
    toutes les autres fonctions.
    '''
    dessiner_fabriques()
    dessiner_lignes_motif()
    dessiner_murs_palais()
    dessiner_plancher()
