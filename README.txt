Projet Développement Python 1 : Jeu Azul
Réalisé par DOUMI Sofiane & EDMEE Léon.


Dernière modification : 07/11/2021

Jeu:

Pour lancer le jeu exécuter le fichier main.py à l'aide de Python3
 > Appuyer sur jouer puis sélectionner le mode de jeu

Un mode de test où les deux joueurs sont contrôlés par l'ordinateur est disponible en cliquant sur le carré
en bas à gauche sur le menu 'accueil' dès le lancement du fichier.

> Le jeu s'arrête dès qu'il n'y a plus de tuiles en jeu : dans les fabriques ou dans la zone du centre.

-----Phase 1 -----

Implémentations :
    - Intéraction avec le joueur via un menu (pas besoin de modifier le code ou d'ouvrir un éditeur)
    - Mode Joueur contre Joueur & Joueur contre ordinateur
    - Phase sélection des tuiles dans les fabriques ou la ligne du milieu
    - Un seul clic suffit pour sélectionner toutes les tuiles d'une même couleur dans une fabrique
    - Affichage des tuiles sélectionnées et possibilité de les déselectionner (clic droit)
    - Docstrings des modules et des fonctions

Problèmes rencontrés:

    - La position des tuiles au milieu ne bouge pas même si celles avant ont étés prises : cela pose aucun problème au
plan technique ou au niveau de la jouabilité mais un peu pour l'esthétisme.
   
    - La création du joueur contrôlé par l'ordinateur a posé des soucis car il faisait souvent planter le jeu
en se bloquant dans un boucle infini car il ne trouvait pas de bonnes coordonnées pour choisir ses tuiles ou les poser
 ----> Ca a été corrigé



