# BlackJack : Mon programme

Tous d'abord avant de vous lancer dans la lecture appronfie de mon programme je vous invite à connaitre les regles du blackjack en cliquant sur l'un des deux liens :
https://www.guide-blackjack.com/regles-du-black-jack.html 
https://www.youtube.com/watch?v=ddu_fYRuv5I&feature=youtu.be 

Détails du programme pour une bonne compréhension ultérieur :

1. Pas de mise de la part du joueur 
2. Au lieu de la possibilité de plusieurs joueurs : Un seul joueur s'affrontera contre le croupier
3. Interdiction de doubler 
4. Nous utiliserons le Blackjack dit Francais c'est à dire 6 jeu de cartes

Maintenant que vous avez eu un aperçu de la phase visible, nous allons approfondir. :)

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

Les attributs :
self.jeu_de_carte -->list : Permet de stocker le jeu de cartes 
self.derniere_carte -->int : Permet de
self.start_game -->bool :  Permet de commencer le jeu mais aussi l'arrêter 
self.la_main_du_joueur -->int : Permet de savoir la valeur de la main du joueur la même chose a été fait pour le croupier
self.liste_de_la_main_du_joueur -->list : Permet de stocker les cartes du joueur dans une liste la même chose a été fait pour le croupier
self.choix_du_joueur -->int : Permet de savoir quand le joueur ne voudra plus tirer de cartes
self.tour -->int : Permet de compter le nombre de tour (utilisation : juste pour le premier au cas où le joueur  fait un blackjack)
self.derniere_carte -->int : Je pense qu'elle me sert plus à rien du au fait que j'utilise random.choice mais elle permettait d'avoir le dernier indice du jeu de carte

