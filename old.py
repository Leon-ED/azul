def affiche_fabrique(fabrique):
    '''
    Prend en paramètre une liste de couleur et dessine les rectangles
    de chaque couleur de cette liste.
    '''
    position = 0
    i = 0
    ligne = 0
    for couleurs in fabrique:
        if i == 2:
            i = 0
            ligne = 1
        rectangle(50+50*i, 25+50*ligne, 100+50*i, 75+50*ligne,remplissage=couleurs,couleur= "black",epaisseur=2)
        i+=1   

    
    #Fabrique 2
    position = 0
    for ligne in range(len(fabrique2)//2):
        for i in range(len(fabrique2)//2):
            rectangle(450+50*i, 25+50*ligne, 500+50*i, 75+50*ligne,remplissage=fabrique2[position],couleur= "black",epaisseur=2)
            position += 1
    
    position = 0
    for ligne in range(len(fabrique3)//2):
        for i in range(len(fabrique3)//2):
            rectangle(850+50*i, 25+50*ligne, 900+50*i, 75+50*ligne,remplissage=fabrique3[position],couleur= "black",epaisseur=2)
            position += 1
    
    position = 0
    for ligne in range(len(fabrique4)//2):
        for i in range(len(fabrique4)//2):
            rectangle(1250+50*i, 25+50*ligne, 1300+50*i, 75+50*ligne,remplissage=fabrique4[position],couleur= "black",epaisseur=2)
            position += 1
    
    position = 0
    for ligne in range(len(fabrique5)//2):
        for i in range(len(fabrique5)//2):
            rectangle(1650+50*i, 25+50*ligne, 1700+50*i, 75+50*ligne,remplissage=fabrique5[position],couleur= "black",epaisseur=2)
            position += 1






def select_fabriques():
    '''
    Si le clic se trouve dans la zone de fabrique: retourne la couleur, le nombre et dans quelle fabrique le clic a été effectué sinon retourne -10,-10,-10
    '''
    x,y,_ = attente_clic()
    x = x // 50  # Divise le clic pour que chaque tuile ait sa position pour 
    y = y // 73  # être précis
    nombre = 0
    couleur = ""
    if 0<=y<=1: #Si le clic se trouve bien entre le haut et le bas des fabriques
        if 1<=x<=2: #Fabrique 1, si le clic est bien entre les position de la première fabrique
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
                    return couleur,nombre,fabrique2             
                if y==1:
                    nombre = fabrique2.count(fabrique2[2])
                    couleur = fabrique2[2]
                    return couleur,nombre,fabrique2
            if x ==10:
                if y ==0:
                    nombre = fabrique2.count(fabrique2[1])
                    couleur = fabrique2[1]
                    return couleur,nombre,fabrique2
                if y==1:
                    nombre = fabrique2.count(fabrique2[3])
                    couleur= fabrique2[3]
                    return couleur, nombre,fabrique2


        if 17<=x<=18: #Fabrique 3
            if x==17:
                if y==0:
                    nombre = fabrique3.count(fabrique3[0])
                    couleur = fabrique3[0]
                    return couleur,nombre,fabrique3                
                if y==1:
                    nombre = fabrique3.count(fabrique3[2])
                    couleur = fabrique3[2]
                    return couleur,nombre,fabrique3
            if x ==18:
                if y ==0:
                    nombre = fabrique3.count(fabrique3[1])
                    couleur = fabrique3[1]
                    return couleur,nombre,fabrique3
                if y==1:
                    nombre = fabrique3.count(fabrique3[3])
                    couleur= fabrique3[3]
                    return couleur, nombre,fabrique3
        if 25<=x<=26: #Fabrique 4
            if x==25:
                if y==0:
                    nombre = fabrique4.count(fabrique4[0])
                    couleur = fabrique4[0]
                    return couleur,nombre,fabrique4            
                if y==1:
                    nombre = fabrique4.count(fabrique4[2])
                    couleur = fabrique4[2]
                    return couleur,nombre,fabrique4
            if x ==26:
                if y ==0:
                    nombre = fabrique4.count(fabrique4[1])
                    couleur = fabrique4[1]
                    return couleur,nombre,fabrique4
                if y==1:
                    nombre = fabrique4.count(fabrique4[3])
                    couleur= fabrique4[3]
                    return couleur, nombre,fabrique4
        if 33<=x<=34: #Fabrique 5
            if x==33:
                if y==0:
                    nombre = fabrique5.count(fabrique5[0])
                    couleur = fabrique5[0]
                    return couleur,nombre,fabrique5                
                if y==1:
                    nombre = fabrique5.count(fabrique5[2])
                    couleur = fabrique5[2]
                    return couleur,nombre,fabrique5
            if x ==34:
                if y ==0:
                    nombre = fabrique5.count(fabrique5[1])
                    couleur = fabrique5[1]
                    return couleur,nombre,fabrique5
                if y==1:
                    nombre = fabrique5.count(fabrique5[3])
                    couleur= fabrique5[3]
                    return couleur, nombre,fabrique5
    else:
        return (-10,-10,-10)
    