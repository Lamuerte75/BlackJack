import random 
class BlackJack:
    def __init__(self,jeu_joueur=0,jeu_croupier=0):
        self.jeu = [] # liste où l'on stockera les 52 cartes du jeu 
        self.jeu_joueur = jeu_joueur 
        self.jeu_croupier = jeu_croupier
        
    # ajoute les cartes dans le jeu de cartes 
    def ajouter_cartes(self):
        compteur_cartes = 2 # permettra de mettre les cartes dans la liste jeu
        # on place chaque carte 4 fois, ici nous nous intérrésons seulement au valeur de la carte
        for _ in range(13):
            for x in range(4):
                self.jeu.append(compteur_cartes) # on ajoute la carte 4 fois 
                
            compteur_cartes+=1 # on incrémente un pour changer la carte
            
        return self.jeu
    
    
    # séléctionne la première cartes au joueur aléatoirement et la supprime du jeu actuelle
    def joueur(self):
        choix_aleatoire_cartes = random.randint(1,14)
        self.jeu_joueur+=choix_aleatoire_cartes 

        return self.jeu_joueur
    
    # séléctionne la première cartes au croupier
    def croupier(self):
        choix_aleatoire_cartes = random.randint(1,14)
        self.jeu_croupier+=choix_aleatoire_cartes

        return self.jeu_croupier
    
    # supprime les cartes données au joueur et au croupier du jeu
    
    def supprime_du_jeu(self):
        
        for x in range(len(self.jeu)):
            if J == self.jeu[x]:
                del self.jeu[x] 
                break # on sort de la boucle pour éviter qu'elle supprime toutes les cartes
                
        for x in range(len(self.jeu)):
            if croupier(self) == self.jeu[x]:
                del self.jeu[x] # on supprime la carte que l'on vient de tirer du jeu 
                break # on sort de la boucle pour éviter qu'elle supprime toutes les cartes
        return self.jeu
    
        def probability_to_win(self):
            pass
        
        

black = BlackJack()
a = black.ajouter_cartes()
print(a)
b = black.joueur()
print(b)
c = black.croupier()
print(c)
d = black.supprime_du_jeu()
