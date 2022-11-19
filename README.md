# BlackJack : Mon programme

Tous d'abord avant de vous lancer dans la lecture appronfie de mon programme je vous invite à connaitre les regles du blackjack en cliquant sur l'un des deux liens :
https://www.guide-blackjack.com/regles-du-black-jack.html 
https://www.youtube.com/watch?v=ddu_fYRuv5I&feature=youtu.be 

Si vous n'avez pas la foi je vais vous expliquer brièvement comment jouer au Blackjack :
Il faut gagner le croupier sans dépasser 21 si ni le joueur ni le croupier à dépasser 21 on va comparer leurs cartes
Le plus haut gagne. 
Les bûches donc les Vallets Dame Roi AS ont une valeur de 10 
L'AS vaut 1 ou 11 dépendant du Jeu 


Détails du programme pour une bonne compréhension ultérieur :

1. Pas de mise de la part du joueur 
2. Au lieu de la possibilité de plusieurs joueurs : Un seul joueur s'affrontera contre le croupier
3. Interdiction de doubler 
4. Le sabot sera constitué de 6 jeu de cartes ( comme le BlackJack est joué en France

Maintenant que vous avez eu un aperçu de la phase visible, nous allons approfondir le sujet en séparant la compréhension du programme et son élaboration en 3 axes :
Premièrement nous définirons les méthodes utilisés ainsi que les/leurs attributs. Puis par la suite nous expliquerons en bref dans un ordre chronologique les Etapes qu'effectue mon programme, et pour finir nous verrons le journal de bord ( les problèmes que j'ai pu rencontrer durant la conception de ce projet).

Ce programme est totalement fait en POO et comporte de nombreuses méthodes et d'attribut : 

Les méthodes : 
ajouter_cartes_et_bruler --> Iniatilisation du sabot (6 jeu de cartes) et supprimer les 5 premières cartes
joueur --> Permet au joueur de tirer une carte, l'ajouter dans son jeu, comptabiliser la valeur de son jeu et supprimer la carte du jeu courant
croupier --> Permet de tirer une carte, l'ajouter dans son jeu, comptabiliser la valeur de son jeu et supprimer la carte du jeu courant
voir_le_jeu_joueur --> Permet au joueur de voir son jeu 
voir_le_jeu_croupier --> Permet au croupier de voir son jeu 
jeu_du_joueur --> Permet au joueur de voir si il veut piocher une autre carte ou non et vérifie qu'il ne dépasse pas 21
jeu_du_croupier --> Le croupier pioche une carte tant que la valeur de son jeu est inférieur a 18 et vérifie qu'il ne dépasse pas 21
who_win --> Permet de savoir qui a gagner grâce à des conditions
nombre_de_partie_jouer --> Comptabilise le nombre de partie jouer
restart_game --> Reinitialise la main du croupier et du joueur, ainsi que leur valeur et si il y 50 cartes ou moins dans le jeu, On vide le jeu de cartes.
probability_to_win --> Qui va nous permettre de connaitre la probabilité du joueur de gagner # Méthodes pas encore faites


Les attributs :
self.jeu_de_carte -->list : Permet de stocker le jeu de cartes 
self.derniere_carte -->int : Permet de
self.start_game -->bool :  Permet de commencer le jeu mais aussi l'arrêter 
self.la_main_du_joueur -->int : Permet de savoir la valeur de la main du joueur la même chose a été fait pour le croupier
self.liste_de_la_main_du_joueur -->list : Permet de stocker les cartes du joueur dans une liste la même chose a été fait pour le croupier
self.choix_du_joueur -->int : Permet de savoir quand le joueur ne voudra plus tirer de cartes
self.tour -->int : Permet de compter le nombre de tour (utilisation : juste pour le premier au cas où le joueur  fait un blackjack)
self.derniere_carte -->int : Je pense qu'elle me sert plus à rien du au fait que j'utilise random.choice mais elle permettait d'avoir le dernier indice du jeu de carte


Comment fonctionne le Programme : 

Les Etapes :

1. Tous d'abord on va initialiser le jeu de cartes et retirer 5 cartes (on les brules)
2. On fait tirer une carte aléatoirement au croupier et au joueur (2 fois au joueur si c'est le premier tour, après que le croupier est reçus sa premiere cartes
3. On oublie pas de bien supprimer les cartes tirées du jeu de cartes
4. On permet au joueur de tirer une autre carte si il le souhaite, du côté du croupier le tirage sera automatique et va respecter le "croupier de base".
5. On compare qui a gagner 
6. Puis on relance une partie si le joueur souhaite rejouer

Si j'y arrive une Etape s'ajoutera avant l'étape 4 qui permettra de compter 

Lisais ça avant de lire le Journal de Bord : 

Dans le Journal de Bord je ne parlerais que des problèmes moyens ou majeurs que j'ai pu avoir lors de la création de ce Projet. 

Journal de Bord : 

11/11/2022 : 
Lorsque je voulais bruler les cartes (donc les supprimer) du jeu de cartes un problème d'index avait lieu : list index out of range créer lorsque le joueur voulait tirer une carte.
Le problème étant dû a self.compteur_dernier qui était était trop elever par rapport a la taille du jeu de cartes. 
J'ai pu le résoudre en enlevant 1 au compteur dernier.

12/11/2022 : 

Début d'un nouveau fichier gameplay où la partie était censer se dérouler
Cependant nombreux problèmes tels que variable undefined ou autres 
Abbendons du fichiers Gameplay etant donné que cela rajouter trop de difficultés et aussi que un seul fichier suffisait en fin de compte


15/11/2022 : 

Ajout de 5 nouveau jeu de carte en plus de celui précèdent (comme le Blackjack français fait), encore une fois problème d'index dû à l'ajout des nouveau dek.
Problème résolu et qui était dû à seulement un décalage de self.derniere_carte

16/11/2022 : 
Problème : empty for randrange lié au module random et la méthode random.randint() 
Résolu en utilisant simplement random.choice() à la place de random.randint()

17/11/2022 : 

Lorsque je lance une nouvelle partie la valeur du jeu du croupier et du joueur et de 0.
Cependant on voit les cartes précèdentes dans leurs jeu + celle de la partie qui se déroule actuellement.
Résolution du Problèmes en définissant la liste du jeu du joueur et celui du croupier dans le __init__ au lieu que dans les méthodes voir_le_jeu_joueur() et voir_le_jeu_croupier()


