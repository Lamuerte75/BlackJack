import random 
class BlackJack:
    def __init__(self,start_game=True,la_main_du_joueur=0,la_main_du_croupier=0,partie_gagner_joueur=0,partie_total_jouer=0):
        self.la_main_du_joueur = la_main_du_joueur # servira a connaitre la valeur de la main du joueur
        self.la_main_du_croupier = la_main_du_croupier # servira a connaitre la valeur de la main du croupier
        self.start_game = start_game # pour que la partie de blackjack puisse ce lancer
        self.partie_gagner_joueur = partie_gagner_joueur # comptabilise le nombre de partie gagner par le joueur
        self.partie_total_jouer = partie_total_jouer
        #self.tour = tour
    # ajoute les cartes dans le jeu de cartes et en supprime 5 (on les brules)
    def ajouter_cartes_et_bruler(self,jeu_de_carte=[],derniere_carte=312):
        self.jeu_de_carte = jeu_de_carte # servira à stocker le jeu de carte 
        self.derniere_carte = derniere_carte # permet de savoir le dernier indice de carte 
        """ Ajoute les cartes dans la liste_jeu_de_cartes pour un total d'un dek de 6 jeu (Blackjack Francais)
        et brule 5 cartes situé dans le jeu de cartes (Règle du Blackjack oblige) """
        
        valeur_de_la_carte = 2 #
        # On fait 6 jeu donc in range 6
        # on place chaque carte 4 fois, ici nous nous intérrésons seulement au valeur de la carte
        for _ in range(6):
            valeur_de_la_carte = 2  #permettra de mettre les cartes dans la liste jeu
            for _ in range(13):
                for _ in range(4):
                     self.jeu_de_carte.append(valeur_de_la_carte) #  on ajoute la carte 4 fois 

                valeur_de_la_carte+=1 # on incrémente un pour changer la carte
        
        # Permet de supprimer 5 cartes on les brules car
        # C'est une règle du BlackJack
        for x in range(5):
            supprimer_carte =  random.choice(jeu_de_carte)#random.randint(self.jeu_de_carte[0],self.jeu_de_carte[self.derniere_carte])
            for x in range(len(self.jeu_de_carte)):
                if supprimer_carte == self.jeu_de_carte[x]:
                    del self.jeu_de_carte[x]
                    break # on casse la boucle pour eviter la suppresion des cartes de meme valeur
            self.derniere_carte-=1 
        return self.jeu_de_carte #,compteur_premier,compteur_dernier
       
         
    
    def joueur(self,liste_de_la_main_du_joueur=[]):
        """ 
        On choisi une carte aléatoirement pour le joueur.
        On le met dans une liste avec les bons termes des cartes Ex : 11 sera Vallée dans la liste
        Puis on ajoute la valeur de la carte au jeu du joueur    
        Supprime la carte du jeu 
        """
        self.liste_de_la_main_du_joueur = liste_de_la_main_du_joueur # stockera le jeu du joueur dans une liste 
        
       
        print("Le joueur s'apprête à tirer une carte")
        choix_aleatoire_carte = random.choice(self.jeu_de_carte)
        
        # Ajoute les cartes du joueur a son dek qui est une liste
        if choix_aleatoire_carte == 11:
            print("Vous avez tirée un Vallée")
            self.liste_de_la_main_du_joueur.append("Vallée") # ajoute la valeur du choix aleatoire dans la liste du jeu du joueur
            self.la_main_du_joueur+=10 # ajoute la valeur du choix aleatoire dans le jeu du joueur
            
        elif choix_aleatoire_carte == 12:
            print("Vous avez tirée une Dame ")
            self.liste_de_la_main_du_joueur.append("Dame")
            self.la_main_du_joueur+=10 
            
        elif choix_aleatoire_carte == 13:
            print("Vous avez tirée un Roi")
            self.liste_de_la_main_du_joueur.append("Roi")
            self.la_main_du_joueur+=10 
        elif choix_aleatoire_carte == 14:
            print("Vous avez tirée un AS")
            self.liste_de_la_main_du_joueur.append("AS")
            choisir_valeur = int(input("Vous pouvez choisir ce que vous preferer comme valeur 1 ou 11  "))
            self.la_main_du_joueur+=choisir_valeur
        else:
            print("Vous avez tirée un ",choix_aleatoire_carte)
            self.liste_de_la_main_du_joueur.append(choix_aleatoire_carte)
            self.la_main_du_joueur+=choix_aleatoire_carte

        # cherche quelle carte le joueur a eu et la supprime du jeu de cartes
        for carte in range(len(self.jeu_de_carte)):
            if choix_aleatoire_carte == self.jeu_de_carte[carte]:
                del self.jeu_de_carte[carte]
                break # pour eviter de supprimer les autres cartes de même valeur 

            self.derniere_carte-=1 # vu qu'on a supprimé une carte on enleve 1 à la longueur du jeu
        
        
        return self.la_main_du_joueur
    
    
    def croupier(self,liste_de_la_main_du_croupier=[]):
        """ 
        On choisi une carte aléatoirement pour le joueur.
        On le met dans une liste avec les bons termes des cartes Ex : 11 sera Vallée dans la liste
        Puis on ajoute la valeur de la carte au jeu du joueur    
        Supprime la carte du jeu 
        """
        self.liste_de_la_main_du_croupier = liste_de_la_main_du_croupier # stockera le jeu du croupier dans une liste 
        print("Le croupier s'apprête à tirer une carte")
        choix_aleatoire_carte = random.choice(self.jeu_de_carte)
        # Ajoute les cartes du joueur a son dek qui est une liste
        if choix_aleatoire_carte == 11:
            print("Le croupier a tirée un Vallée") 
            self.liste_de_la_main_du_croupier.append("Vallée") # ajoute la valeur du choix aleatoire dans la liste du jeu du joueur
            self.la_main_du_croupier+=10 # ajoute la valeur du choix aleatoire dans le  jeu du joueur
            
        elif choix_aleatoire_carte == 12:
            print("Le croupier a tirée une Dame ")
            self.liste_de_la_main_du_croupier.append("Dame")
            self.la_main_du_croupier+=10
            
        elif choix_aleatoire_carte == 13:
            print("Le croupier a tirée  Roi")
            self.liste_de_la_main_du_croupier.append("Roi")
            self.la_main_du_croupier+=10
            
        elif choix_aleatoire_carte == 14:
            print("Le croupier a tirée un AS")
            self.liste_de_la_main_du_croupier.append("AS")
            choisir_valeur = int(input("Le croupier choisi sa préférence  comme valeur 1 ou 11 "))
            self.la_main_du_croupier+=choisir_valeur
            
        else: 
            print("Le croupier a tirée un ",choix_aleatoire_carte)
            self.liste_de_la_main_du_croupier.append(choix_aleatoire_carte)
            self.la_main_du_croupier+=choix_aleatoire_carte
            
    # cherche quelle carte le joueur a eu et la supprime du jeu de cartes
        for carte in range(len(self.jeu_de_carte)):
            if choix_aleatoire_carte == self.jeu_de_carte[carte]:
                del self.jeu_de_carte[carte]
                break # pour eviter de supprimer les autres cartes de même valeur 
    
            self.derniere_carte-=1 # vu qu'on a supprimé une carte on enleve 1 à la longueur du jeu
 
        return self.la_main_du_croupier
    
    def voir_le_jeu_joueur(self):
        """ Parcours la liste de la main du joueur et lui affiche ses cartes """ 
        
        for x in range(len(self.liste_de_la_main_du_joueur)):
            print(self.liste_de_la_main_du_joueur[x],end=" ")
                
    def voir_le_jeu_croupier(self):
       """ Parcours la liste de la main du croupier et lui affiche ses cartes """ 
       for x in range(len(self.liste_de_la_main_du_croupier)):
            print(self.liste_de_la_main_du_croupier[x],end=" ")
        
    def jeu_du_joueur(self,choix_du_joueur=0,tour=0):
        self.tour = tour # permet de savoir à quelle tour on est 
        self.choix_du_joueur = choix_du_joueur # permettra de savoir si le joueur veut continuer a tirer des cartes ou non 
        
        """
        Tant que le joueur decide de tirer une carte on vérifie : 
        Si la main du joueur est supérieur a 21 et si oui, et si cela a été fait le cas dès le premier tour
        Si le joueur décide de piocher une autre carte on vérifie que sa main n'est pas supérieur a 21 
        Si elle est supérieur à 21 le joueur à perdu 
        Si le joueur décide de ne plus piocher de carte on sort de la boucle 
        """
        black.joueur()
        while self.choix_du_joueur == 0:
            print("La valeur de votre jeu est :",self.la_main_du_joueur)
            print("Votre jeu est : "),black.voir_le_jeu_joueur()
            if self.la_main_du_joueur == 21 and self.tour == 1:
                    print("BLACKJACK !!!!!!!")
                    break
                    self.start_game = False
                    
            if  self.la_main_du_joueur > 21:
                print()
                print("Vous avez perdu")
                self.start_game = False
                break 
            choisir_de_tirer_une_autre_carte_joueur = input("Si vous voulez recevoir encore une carte taper 1 sinon appuyer sur n'importe quelle touche ")
            if choisir_de_tirer_une_autre_carte_joueur == "1":
                black.joueur()
            else:
                print("Le joueur a choisi de ne plus/pas tirer de carte")
                self.choix_du_joueur = 1
            self.tour+=1
        
    def jeu_du_croupier(self):
        """  
        Si le joueur n'a pas dépassé 21 c'est au tour du croupier de jouer 
        Tant que la main du croupier est inférieur à 17 il continuera à tirer une carte
        Si la main du croupier dépasse 21 le joueur gagne
        Si la main du croupier est supérieur au jeu du joueur il arrête de tirer des cartes
        """
        if self.start_game:
            print()
            print("Au tour du croupier ")
            print()
        if self.start_game: # Si le joueur n'a pas dépasser 21 
            
            print("La valeur du jeu du croupier est :",self.la_main_du_croupier)
            while self.la_main_du_croupier < 17:
                black.croupier()
                print("La valeur du jeu du croupier est :",self.la_main_du_croupier)
                print("Le croupier a : "),black.voir_le_jeu_croupier()
                print()
                
                if self.la_main_du_croupier > 21:
                   print()
                   print("Le croupier à dépasser 21")
                   print("Vous avez gagnés")
                   self.start_game = False # Stipule que le jeu est bien terminé
                   break # On sort de la boucle 
                if self.la_main_du_croupier > self.la_main_du_joueur: # Si le croupier a une meilleur il arrête de piocher
                    break
                
                
    def who_win(self):
        """
        Si le jeu continue et que le joueur et le croupier on fini de piocher
        On compare les cartes du joueur et du croupier :
        Si le jeu du joueur et du croupier ont la même valeur : On affiche Egalité
        Si le jeu du joueur et mieux que celui du croupier : On affiche Vous avez gagné
        Si le jeu du joueur est inférieur à celui du croupier : On affiche Vous avez perdu 
        """
        if self.start_game:
            # Si le jeu continue et que le joueur et le croupier on fini de piocher 
            # On compare avec trois conditions
            # SI il y a une égalité, si le joueur à une meilleure main ou si c'est le cas du croupier 
            print("le croupier à ",self.la_main_du_croupier)
            print("Vous avez",self.la_main_du_joueur)           
            if self.la_main_du_croupier == self.la_main_du_joueur:
                print("Egalité")
            if self.la_main_du_joueur > self.la_main_du_croupier:
                print("Vous avez gagné")
                self.partie_gagner_joueur+=1
            if self.la_main_du_croupier > self.la_main_du_joueur:
                print("Vous avez perdu")
        self.start_game = False # On déclare que la partie est terminé 
        return self.partie_gagner_joueur
    def nombre_de_partie_jouer(self):
        """ Incrémente 1 au nombre de partie jouer et renvoie le nombre de partie jouer"""
        self.partie_total_jouer+=1    
        return self.partie_total_jouer
        
    def restart_game(self):
        
        """ 
        Si la partie est terminé 
        On supprime les cartes dans le jeu du joueur et celui du croupier 
        On reinitialise la valeur de la main du joueur et du croupier à 0
        """
        if not(self.start_game):
            
            """
            for carte in range(len(self.liste_de_la_main_du_joueur)):
                del self.liste_de_la_main_du_joueur[carte]
            for carte in range(len(self.liste_de_la_main_du_croupier)):
                del self.liste_de_la_main_du_croupier[carte]
            """
            self.liste_de_la_main_du_joueur = [] # Le joueur n'a plus de carte dans son jeu 
            self.liste_de_la_main_du_croupier = [] # Le croupier n'a plus de carte dans son jeu
            self.la_main_du_joueur = 0 # On reinitialise la main du joueur à 0 
            self.la_main_du_croupier = 0 # On reinitialise la main du croupier a 0 
            if len(self.jeu_de_carte) <= 50:
                self.jeu_de_carte = []
        print()    
        nouvelle_partie = int(input("Voulez vous faire une partie  1 = Oui, Autre touche = Non "))
        print()
        if nouvelle_partie == 1:
            self.start_game = True # On peut refaire une partie 
            
        return nouvelle_partie  

    def probability_to_win(self):
        """ Permet de calculer la probabilité que le joueur a de gagner grace à la méthode ... """
        pass
        
black = BlackJack()
ajout_du_jeu_de_carte = black.ajouter_cartes_et_bruler() # Fonctionne correctement 
partie = black.restart_game()
while partie ==1:
    black.joueur()
    black.croupier()
    black.jeu_du_joueur()
    black.jeu_du_croupier()
    gagnant = black.who_win()
    nombre_partie_jouer = black.nombre_de_partie_jouer()
    if black.restart_game() != 1:
        partie = 0
    if len(ajout_du_jeu_de_carte) <= 50:
        black.ajouter_cartes_et_bruler
        
print("Le joueur à gagner :",gagnant,"sur",nombre_partie_jouer,"partie")

#a = black.jeu_du_joueur()

       
        
        
