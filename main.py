from upemtk import *
from graphiques import *
from random import randint



cree_fenetre(1800, 900)



#---------------------------------Sac---------------------------------#
def sac_plein():
    couleurs = ["black", "yellow", "green","orange","blue"]
    sac = []
    for colors in couleurs:
        for i in range(20):
            sac.append(colors)
    return sac

def sac_est_vide():
    return len(sac) != 0

#------------------------------Fabriques-------------------------------#
def fabriques_plein(liste):
    for i in range(4):
        taille = len(sac)
        r = randint(0,taille-1)
        liste.append(sac[r])
        sac.pop(r)

    return liste

def fabrique_est_vide():
    if len(fabrique1) == len(fabrique2) == len(fabrique3) == len(fabrique4) == len(fabrique5) == 0:
        return True
    return False


def select_fabriques():
    x,y,_ = attente_clic()
    x = x // 50
    y = y // 73
    nombre = 0
    couleur = ""
    if 0<=y<=1:
        if 1<=x<=2: #Fabrique 1
            if x==1:
                if y==0:
                    nombre = fabrique1.count(fabrique1[0])
                    couleur = fabrique1[0]
                    return couleur,nombre,fabrique1                
                if y==1:
                    nombre = fabrique1.count(fabrique1[2])
                    couleur = fabrique1[2]
                    return couleur,nombre,fabrique1
            if x ==2:
                if y ==0:
                    nombre = fabrique1.count(fabrique1[1])
                    couleur = fabrique1[1]
                    return couleur,nombre,fabrique1
                if y==1:
                    nombre = fabrique1.count(fabrique1[3])
                    couleur= fabrique1[3]
                    return couleur, nombre,fabrique1

    
        if 9<=x<=10: #Fabrique 2
            if x==9:
                if y==0:
                    nombre = fabrique2.count(fabrique2[0])
                    couleur = fabrique2[0]
                    return couleur,nombre                
                if y==1:
                    nombre = fabrique2.count(fabrique2[2])
                    couleur = fabrique2[2]
                    return couleur,nombre
            if x ==10:
                if y ==0:
                    nombre = fabrique2.count(fabrique2[1])
                    couleur = fabrique2[1]
                    return couleur,nombre
                if y==1:
                    nombre = fabrique2.count(fabrique2[3])
                    couleur= fabrique2[3]
                    return couleur, nombre


        if 17<=x<=18: #Fabrique 3
            if x==17:
                if y==0:
                    nombre = fabrique3.count(fabrique3[0])
                    couleur = fabrique3[0]
                    return couleur,nombre                
                if y==1:
                    nombre = fabrique3.count(fabrique3[2])
                    couleur = fabrique3[2]
                    return couleur,nombre
            if x ==18:
                if y ==0:
                    nombre = fabrique3.count(fabrique3[1])
                    couleur = fabrique3[1]
                    return couleur,nombre
                if y==1:
                    nombre = fabrique3.count(fabrique3[3])
                    couleur= fabrique3[3]
                    return couleur, nombre
        if 25<=x<=26: #Fabrique 4
            if x==25:
                if y==0:
                    nombre = fabrique4.count(fabrique4[0])
                    couleur = fabrique4[0]
                    return couleur,nombre                
                if y==1:
                    nombre = fabrique4.count(fabrique4[2])
                    couleur = fabrique4[2]
                    return couleur,nombre
            if x ==26:
                if y ==0:
                    nombre = fabrique4.count(fabrique4[1])
                    couleur = fabrique4[1]
                    return couleur,nombre
                if y==1:
                    nombre = fabrique4.count(fabrique4[3])
                    couleur= fabrique4[3]
                    return couleur, nombre
        if 33<=x<=34: #Fabrique 5
            if x==33:
                if y==0:
                    nombre = fabrique5.count(fabrique5[0])
                    couleur = fabrique5[0]
                    return couleur,nombre                
                if y==1:
                    nombre = fabrique5.count(fabrique5[2])
                    couleur = fabrique5[2]
                    return couleur,nombre
            if x ==34:
                if y ==0:
                    nombre = fabrique5.count(fabrique5[1])
                    couleur = fabrique5[1]
                    return couleur,nombre
                if y==1:
                    nombre = fabrique5.count(fabrique5[3])
                    couleur= fabrique5[3]
                    return couleur, nombre
    else:
        return (-10,-10,-10)
    





def affiche_fabrique():
    position = 0
    for ligne in range(len(fabrique1)//2):
        for i in range(len(fabrique1)//2):
            rectangle(50+50*i, 25+50*ligne, 100+50*i, 75+50*ligne,remplissage=fabrique1[position],couleur= "black",epaisseur=2)
            position += 1
    
    position = 0
    for ligne in range(2):
        for i in range(2):
            rectangle(450+50*i, 25+50*ligne, 500+50*i, 75+50*ligne,remplissage=fabrique2[position],couleur= "black",epaisseur=2)
            position += 1
    position = 0
    for ligne in range(2):
        for i in range(2):
            rectangle(850+50*i, 25+50*ligne, 900+50*i, 75+50*ligne,remplissage=fabrique3[position],couleur= "black",epaisseur=2)
            position += 1
    position = 0
    for ligne in range(2):
        for i in range(2):
            rectangle(1250+50*i, 25+50*ligne, 1300+50*i, 75+50*ligne,remplissage=fabrique4[position],couleur= "black",epaisseur=2)
            position += 1
    position = 0
    for ligne in range(2):
        for i in range(2):
            rectangle(1650+50*i, 25+50*ligne, 1700+50*i, 75+50*ligne,remplissage=fabrique5[position],couleur= "black",epaisseur=2)
            position += 1
    
    
def remove_fabrique(data):
    couleur,nombre,liste = data
    for i in range(nombre):
        liste.remove(couleur)
    

def clic():
    x, y, _ = attente_clic()
    return x, y

def remplir_cases(joueur,y,couleur,nombre):
    y = (y//60)-6
    if y < 0 or y > 4:
        return
    if joueur == 1:    #Remplit la grille du 1er joueur
        longueur = len(grille_j1[y])
        reste = 0
        compteur = 0
        for i in range(longueur):
            if nombre> longueur:
                if compteur == nombre:
                    return couleur, reste
                grille_j1[y][i]= couleur
                reste = nombre-longueur
                print(grille_j1,reste)
                compteur +=1
            else:
                grille_j1[y][i] = couleur


    if joueur ==2:  #Remplit la grille du 2eme joueur (bot ou pas)
        longueur = len(grille_j1[y])
        reste = 0
        for i in range(nombre):
            if nombre> longueur:
                grille_j2[y][i]= couleur
                reste = nombre-longueur
            else:
                grille_j2[y][i] = couleur





if __name__ == "__main__":
    dessiner_plateau()
    grille_j1 = [["vide"], ["vide", "vide"], ["vide", "vide", "vide"], ["vide", "vide", "vide", "vide"], ["vide", "vide", "vide", "vide", "vide"]]
    grille_j2 = [["vide"], ["vide", "vide"], ["vide", "vide", "vide"], ["vide", "vide", "vide", "vide"], ["vide", "vide", "vide", "vide", "vide"]]
    sac = sac_plein()
    fabrique1 = fabriques_plein(list())
    fabrique2 = fabriques_plein(list())
    fabrique3 = fabriques_plein(list())
    fabrique4 = fabriques_plein(list())
    fabrique5 = fabriques_plein(list())


    while True:
        efface_tout()
        dessiner_plateau()
        affiche_fabrique()

        data =couleur,nombre,fabrique_num = select_fabriques()
        print(couleur,nombre)
        if couleur != nombre != fabrique_num != -10:
            x,y,_ = attente_clic()
            remplir_cases(1, y, couleur, nombre)
            print(data)
            remove_fabrique(data)
            print(grille_j1)
            print(fabrique1)




attente_clic()
ferme_fenetre()
