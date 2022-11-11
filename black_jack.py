import random 
class BlackJack:
    def __init__(self,jeu_joueur=0,jeu_croupier=0,compteur_premier=0,compteur_dernier=51):
        self.jeu = [] # liste où l'on stockera les 52 cartes du jeu 
        self.liste_jeu_joueur = []
        self.liste_jeu_croupier = []
        self.jeu_joueur = jeu_joueur 
        self.jeu_croupier = jeu_croupier
        self.compteur_premier = compteur_premier
        self.compteur_dernier = compteur_dernier
        
    # ajoute les cartes dans le jeu de cartes et en supprime 5 (on les brules)
    def ajouter_cartes_et_bruler(self):
        compteur_cartes = 2 # permettra de mettre les cartes dans la liste jeu
        
        # on place chaque carte 4 fois, ici nous nous intérrésons seulement au valeur de la carte
        for _ in range(13):
            for x in range(4):
                self.jeu.append(compteur_cartes) # on ajoute la carte 4 fois 
                
            compteur_cartes+=1 # on incrémente un pour changer la carte
            
        # Permet de supprimer 5 cartes on les brules car
        # C'est une règle du BlackJack
        for x in range(5):
            supprimer_carte =  random.randint(self.jeu[self.compteur_premier],self.jeu[self.compteur_dernier])
            for x in range(len(self.jeu)):
                if supprimer_carte == self.jeu[x]:
                    del self.jeu[x]
                    break # on casse la boucle pour eviter la suppresion des cartes de meme valeur
            self.compteur_dernier-=1 
            
    
        
    

    def joueur(self):
        # Steps
        # choisi une carte aléatoirement pour le joueur 
        # On le met dans une liste avec les bons termes des cartes Ex : 11 sera Vallée dans la liste
        # Puis on ajoute la valeur de la carte au jeu du joueur 
        # Supprime la carte du jeu 
        
        choix_aleatoire_cartes = random.randint(self.jeu[self.compteur_premier],self.jeu[self.compteur_dernier])
        
        # Ajoute les cartes du joueur a son dek qui est une liste
        if choix_aleatoire_cartes == 11:
            print("Vous avez tirée un Vallée")
            self.liste_jeu_joueur.append("Vallée") # ajoute la valeur du choix aleatoire dans la liste du jeu du joueur
            self.jeu_joueur+=10 # ajoute la valeur du choix aleatoire dans le jeu du joueur
            
        elif choix_aleatoire_cartes == 12:
            print("Vous avez tirée une Dame ")
            self.liste_jeu_joueur.append("Dame")
            self.jeu_joueur+=10 
            
        elif choix_aleatoire_cartes == 13:
            print("Vous avez tirée un Roi")
            self.liste_jeu_joueur.append("Roi")
            self.jeu_joueur+=10 
        elif choix_aleatoire_cartes == 14:
            print("Vous avez tirée un AS")
            self.liste_jeu_joueur.append("AS")
            choisir_valeur = int(input("Vous pouvez choisir ce que vous preferer comme valeur 1 ou 11"))
            self.jeu_joueur+=choisir_valeur
        else:
            print("Vous avez tirée un ",choix_aleatoire_cartes)
            self.liste_jeu_joueur.append(choix_aleatoire_cartes)
            self.jeu_joueur+=choix_aleatoire_cartes 

        # cherche quelle carte le joueur a eu et la supprime du jeu de cartes
        for x in range(len(self.liste_jeu_joueur)):
            for i in range(len(self.jeu)):
                if self.liste_jeu_joueur[x] == self.jeu[i]:
                    del self.jeu[x]
                    break # evite de supprimer les autres cartes de même valeur que celle tirée

            self.compteur_dernier-=1
        print("La valeur de votre jeu est :",self.jeu_joueur)
        
        
        
    
    # séléctionne la première cartes au croupier et la supprime du jeu de cartes 
    def croupier(self):
        # Steps
        # choisi une carte aléatoirement pour le croupier 
        # On le met dans une liste avec les bons termes des cartes Ex : 11 sera Vallée dans la liste
        # Puis on ajoute la valeur de la carte au jeu du croupier 
        # Supprime la carte du jeu 
        
        choix_aleatoire_cartes = random.randint(self.jeu[self.compteur_premier],self.jeu[self.compteur_dernier])
        # Ajoute les cartes du joueur a son dek qui est une liste
        if choix_aleatoire_cartes == 11:
            print("Le croupier a tirée un Vallée") 
            self.liste_jeu_croupier.append("Vallée") # ajoute la valeur du choix aleatoire dans la liste du jeu du joueur
            self.jeu_croupier+=10 # ajoute la valeur du choix aleatoire dans le  jeu du joueur
            
        elif choix_aleatoire_cartes == 12:
            print("Le croupier a tirée une Dame ")
            self.liste_jeu_croupier.append("Dame")
            self.jeu_croupier+=10
            
        elif choix_aleatoire_cartes == 13:
            print("Le croupier a tirée  Roi")
            self.liste_jeu_croupier.append("Roi")
            self.jeu_croupier+=10
            
        elif choix_aleatoire_cartes == 14:
            print("Le croupier a tirée un AS")
            self.liste_jeu_croupier.append("AS")
            choisir_valeur = int(input("Le croupier choisi sa préférence  comme valeur 1 ou 11"))
            self.jeu_croupier+=choisir_valeur
            
        else: 
            print("Vous avez tirée un ",choix_aleatoire_cartes)
            self.liste_jeu_croupier.append(choix_aleatoire_cartes)
            self.jeu_croupier+=choix_aleatoire_cartes
            
    # cherche quelle carte le joueur a eu et la supprime du jeu de cartes
        for x in range(len(self.liste_jeu_croupier)):
            for i in range(len(self.jeu)):
                if self.liste_jeu_croupier[x] == self.jeu[i]:
                    del self.jeu[x]
                    break # evite de supprimer les autres cartes de même valeur que celle tirée
    
                self.compteur_dernier-=1
            print("La valeur du jeu du croupier est :",self.jeu_croupier)
            
 
       
        return self.liste_jeu_croupier
    

    def probability_to_win(self):
        pass
        
black = BlackJack()
start_game = True
tour = 1 
if start_game:
    #Si la partie commence on ajoute les cartes
    black.ajouter_cartes_et_bruler() # 
print("Le croupier distribue les cartes")

# Quand le tour est de 1 le joueur recoit deux cartes 
if tour == 1:
    black.joueur()
    black.croupier()
    black.joueur()

while startgame:
    choisir_de_tirer_une_autre_carte = input("Si vous voulez recevoir encore une carte taper 1 sinon appuyer sur n'importe quelle touche")
    if choisir_de_tirer_une_autre_carte == 1:
        black.joueur()
    else:
        pass
        



    



