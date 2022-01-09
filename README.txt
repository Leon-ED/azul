Projet Développement Python 1 : Jeu Azul
Réalisé par DOUMI Sofiane & EDMEE Léon.


Dernière modification : 09/01/2022

Jeu:

Pour lancer le jeu exécuter le fichier main.py à l'aide de Python3
 > Appuyer sur jouer
 > Selectionner le nombre de joueurs
 > Sélectionner le mode joueur contre joueur / joueur contre ordinateur

Un mode de test où les deux joueurs sont contrôlés par l'ordinateur est disponible en cliquant sur le carré
en bas à gauche sur le menu 'accueil' dès le lancement du fichier. Il oppose 4 joueurs contrôlés par l'ordinateur et jouent sans délai.

> Le jeu s'arrête dès qu'un joueur a rempli une ligne de son palais ou alors quand il n'y a plus de tuiles en jeu que ça soit dans le sac,
le couvercle et les fabriques

-----Phase 1 -----

Implémentations :
    - Intéraction avec le joueur via un menu (pas besoin de modifier le code ou d'ouvrir un éditeur)
    - Mode Joueur contre Joueur & Joueur contre ordinateur
    - Phase sélection des tuiles dans les fabriques ou la ligne du milieu
    - Un seul clic suffit pour sélectionner toutes les tuiles d'une même couleur dans une fabrique
    - Affichage des tuiles sélectionnées et possibilité de les déselectionner (clic droit)
    - Docstrings des modules et des fonctions.
    
Non implémenté / Bugs:
    - Le placement des tuiles dans la grille se fait par rapport à la plus grande ligne c'est à dire qu'il est possible de placer une tuile 
dans la plus petite ligne sans cliquer directement dessus.

Problèmes rencontrés:
    - La position des tuiles au milieu ne bouge pas même si celles avant ont étés prises : cela pose aucun problème au
plan technique ou au niveau de la jouabilité mais un peu pour l'esthétisme.
   
    - La création du joueur contrôlé par l'ordinateur a posé des soucis car il faisait souvent planter le jeu
en se bloquant dans un boucle infini car il ne trouvait pas de bonnes coordonnées pour choisir ses tuiles ou les poser.
 ----> Ca a été corrigé


-----Phase 2 -----
Implémentations:
    - Le jeu complet avec la phase décoration du mur et les manches (re-remplissage des fabriques etc...)
    - Jouer de 2 à 4 joueurs (Pour l'instant sans bot au dela du 2 joueurs car le menu n'est pas fini mais les bots marchent à 4)
    - Possibilité de forcer le jeu à 2,3,4 dans le fichier settings.txt dans le dossier files
    --Settings.txt : 2 lignes pour le moment la première indique le nombre de joueurs : de 2 à 4
        - La seconde les joueurs controlés par l'ordinateur a noté sous la forme : 1,2 ou 1,3,4 ou 1,2,3,4 etc..



Non implémenté / Bugs / Problèmes rencontrés:
    - Sauvegarde / chargement d'une sauvegarde ---> Sera prêt pour la phase 3
    - Récupérer les tuiles "tombées" pour les remettre en jeu ---> Sera prêt pour la phase 3
    - Menu options où on peut choisir entre un mode bas graphiques (dessins avec upemtk) ou haut graphiques (utilisation d'images) ---> Sera prêt pour la phase 3
    (Toujours possible de choisir l'option soit même dans le main.py)
    - Le comptage des points ---> Sera prêt pour la phase 3

-----Phase 3 -----

Implémentations:
    -Celles de la phase 1 et 2
    -Les fabriques sont supprimées dynamiquement au fur et à mesure qu'elles sont jouées
    -Comptage des points à la fin de la manche et à la fin de la partie
    -Sauvegarde de la partie (automatique) et chargement d'une partie au choix si une sauvegarde existe
    -Possibilité de choisir entre un mode décoré et un mode non décoré
    -Enregistrement des tuiles non utilisées pour les réutiliser si le sac est vide : couvercle du jeu
    

    ---Extension du jeu :
    -Amélioration du jeu de l'ordinateur auparavant il prenait une fabrique au hasard , une couleur au hasard et les placait dans une ligne au hasard.
    Désormais :
    -A chaque coup il calcul selon sa grille et selon son palais la place disponible et les couleurs qu'il peut placer
    -Les matrices représentant les fabriques sont simplifiées en une liste.
    -Pour chaque ligne et les possibilités de placement des tuiles , l'ordinateur analyse les fabriques et s'il peut remplir la ligne directement il le fait.
    Sinon il continue  avec la ligne suivante et s'il ne trouve toujours rien, il joue analyse la "moins pire" des possibilités et la jouer.
    Et s'il ne trouve toujours rien alors il place les tuiles dans le plancher
    L'ancienne version de l'ordinateur les faisait finir la partie avec énormément des points négatifs et très rarement en positif avec quand c'est le cas un  très faible score.
    La nouvelle version rend l'ordinateur très compétitif , il ne termine jamais une partie avec des points négatifs mais avec beaucoup de points et est très difficile à battre !