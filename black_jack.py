import random 
class BlackJack:
    def __init__(self,la_main_du_joueur=0,la_main_du_croupier=0,derniere_carte=311):
        self.liste_de_la_main_du_joueur = []
        self.liste_de_la_main_du_croupier = []
        self.la_main_du_joueur = la_main_du_joueur
        self.la_main_du_croupier = la_main_du_croupier
        self.derniere_carte = derniere_carte
        self.jeu_de_carte = []
    # ajoute les cartes dans le jeu de cartes et en supprime 5 (on les brules)
    def ajouter_cartes_et_bruler(self):
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
            supprimer_carte =  random.randint(self.jeu_de_carte[0],self.jeu_de_carte[self.derniere_carte])
            for x in range(len(self.jeu_de_carte)):
                if supprimer_carte == self.jeu_de_carte[x]:
                    del self.jeu_de_carte[x]
                    break # on casse la boucle pour eviter la suppresion des cartes de meme valeur
            self.derniere_carte-=1 
        return self.jeu_de_carte #,compteur_premier,compteur_dernier
    
         
    
    def joueur(self):
        """ 
        On choisi une carte aléatoirement pour le joueur.
        On le met dans une liste avec les bons termes des cartes Ex : 11 sera Vallée dans la liste
        Puis on ajoute la valeur de la carte au jeu du joueur    
        Supprime la carte du jeu 
        """
       
        choix_aleatoire_carte = random.randint(self.jeu_de_carte[0],self.jeu_de_carte[self.derniere_carte])
        
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
            choisir_valeur = int(input("Vous pouvez choisir ce que vous preferer comme valeur 1 ou 11"))
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
        print("La valeur de votre jeu est :",self.la_main_du_joueur)
        return self.la_main_du_joueur
    
    
    def croupier(self):
        """ 
        On choisi une carte aléatoirement pour le joueur.
        On le met dans une liste avec les bons termes des cartes Ex : 11 sera Vallée dans la liste
        Puis on ajoute la valeur de la carte au jeu du joueur    
        Supprime la carte du jeu 
        """
        
        choix_aleatoire_carte = random.randint(self.jeu_de_carte[0],self.jeu_de_carte[self.derniere_carte])
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
            choisir_valeur = int(input("Le croupier choisi sa préférence  comme valeur 1 ou 11"))
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
        print("La valeur du jeu du croupier est :",self.la_main_du_croupier)
            
 
        return self.la_main_du_croupier
    
    def voir_le_jeu_joueur(self):
        """ Parcours la liste de la main du joueur et lui affiche ses cartes """ 
        
        for x in range(len(self.liste_de_la_main_du_joueur)):
            print(self.liste_de_la_main_du_joueur[x],end=" ")
                
    def voir_le_jeu_croupier(self):
       """ Parcours la liste de la main du croupier et lui affiche ses cartes """ 
       for x in range(len(self.liste_de_la_main_du_croupier)):
            print("Le croupier a ",self.liste_de_la_main_du_croupier[x],end=" ")
        
    def probability_to_win(self):
        """ Permet de calculer la probabilité que le joueur a de gagner grace à la méthode ... """
        pass
        
black = BlackJack()
start_game = True
tour = 1
print("Le croupier distribue les cartes")
if  tour == 1:
    #Si la partie commence on ajoute les cartes
    black.ajouter_cartes_et_bruler() # ajoute les jeux de carte
    black.joueur() # distribue une carte au joueur
    black.croupier() # distribue une carte au croupier
    
print()
print() 
while start_game:
    print("C'est votre tour ")
    print("Votre jeu est : "),black.voir_le_jeu_joueur()
    print()
    choix_du_joueur = 0  # Permet que le joueur tire x nombre de fois une carte
    while choix_du_joueur == 0:
        # Tant que le joueur veux choisir une carte la boucle continue 
        # Sauf si il dépasse 21
        print("Le joueur tire une carte")
        main_du_joueur = black.joueur() # Montre la carte qui vient d'être tirée par le joueur
        print("Votre jeu est : "),black.voir_le_jeu_joueur()
        # Si le joueur a un blackjack  ( donc a 21) dès le premier tour 
        # Il gagne automatiquement 
        # Sinon il choisi ou non de tirer une autre carte
        if main_du_joueur == 21 and tour == 1:
            print("BLACKJACK !!!!!!!")
            break
            start_game = False
        choisir_de_tirer_une_autre_carte_joueur = input("Si vous voulez recevoir encore une carte taper 1 sinon appuyer sur n'importe quelle touche ")
        
        if choisir_de_tirer_une_autre_carte_joueur == "1":
            if main_du_joueur > 21:
                print("Vous avez perdu")
                start_game = False
                break 
        else:
            print("Le joueur a choisi de ne plus/pas tirer de carte")
            choix_du_joueur = 1
        tour+=1
    print()
    # On verifie bien que le joueur est toujours en dessous de 21 
    if start_game: # Si le joueur n'a pas encore perdu 
        print("Au tour du croupier ")
        print("Le jeu du croupier est")
        black.voir_le_jeu_croupier()
        main_du_croupier = black.croupier()
        while main_du_croupier < 17:
            main_du_croupier = black.croupier()
            if main_du_croupier > 21:
                print("Le croupier à dépasser 21")
                print("Vous avez gagnés")
                start_game = False # Le jeu est terminer
                break
            if main_du_croupier > main_du_joueur:
                break 
                
                
    # Si ni le croupier ni le joueur à dépasser 21
    # Et que le joueur ainsi que le croupier ne pioche plus
    # On compare qui à  le meilleur jeu de carte
    if start_game  == True and choix_du_joueur == 1:
        print("le croupier à ",main_du_croupier)
        print("Vous avez",main_du_joueur)
        if main_du_joueur == main_du_croupier:
            print("Egalité")
        if main_du_joueur > main_du_croupier:
            print("Vous avez gagné")
        if main_du_croupier > main_du_joueur:
            print("Vous avez perdu")
        start_game = False
            
             
        
        
