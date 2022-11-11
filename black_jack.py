import random 
class BlackJack:
    def __init__(self,jeu_joueur=0,jeu_croupier=0,compteur_premier=0,compteur_dernier=51):
        self.jeu = [] # liste où l'on stockera les 52 cartes du jeu 
        self.jeu_joueur = jeu_joueur 
        self.jeu_croupier = jeu_croupier
        self.compteur_premier = compteur_premier
        self.compteur_dernier = compteur_dernier
        
    # ajoute les cartes dans le jeu de cartes 
    def ajouter_cartes(self):
        compteur_cartes = 2 # permettra de mettre les cartes dans la liste jeu
        # on place chaque carte 4 fois, ici nous nous intérrésons seulement au valeur de la carte
        for _ in range(13):
            for x in range(4):
                self.jeu.append(compteur_cartes) # on ajoute la carte 4 fois 
                
            compteur_cartes+=1 # on incrémente un pour changer la carte
            
        return len(self.jeu)
    
    
    # choisi une carte aléatoirement pour le joueur 
    # Supprime la carte du jeu 
    def joueur(self):

        choix_aleatoire_cartes = random.randint(self.jeu[self.compteur_premier],self.jeu[self.compteur_dernier])
        self.jeu_joueur+=choix_aleatoire_cartes 
        # cherche quelle carte le joueur a eu et la supprime du jeu de cartes
        for x in range(len(self.jeu)):
            if self.jeu_joueur == self.jeu[x]:
                del self.jeu[x]
                break # casse la boucle pour éviter quelle supprime toutes les meme cartes du meme chiffr
            
        self.compteur_dernier-=1
        
        return len(self.jeu)
    
    # séléctionne la première cartes au croupier et la supprime du jeu de cartes 
    def croupier(self):
        
        choix_aleatoire_cartes = random.randint(self.jeu[self.compteur_premier],self.jeu[self.compteur_dernier])
        self.jeu_croupier+=choix_aleatoire_cartes 
        # cherche quelle carte le croupier a eu et la supprime du jeu de cartes
        for x in range(len(self.jeu)):
            if self.jeu_croupier == self.jeu[x]:
                del self.jeu[x]
                break # casse la boucle pour éviter quelle supprime toutes les meme cartes du meme chiffre
        self.compteur_dernier-=1
       
        return self.jeu_croupier
    

    def probability_to_win(self):
        pass
        


black = BlackJack()
a = black.ajouter_cartes()
b = black.joueur()
c = black.croupier()
