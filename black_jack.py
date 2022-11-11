import random 
class BlackJack:
    def __init__(self,jeu_joueur=0,jeu_croupier=0,compteur_premier=0,compteur_dernier=51):
        self.jeu = [] # liste où l'on stockera les 52 cartes du jeu 
        #self.liste_jeu_joueur = []
        #self.liste_jeu_croupier = []
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
        return len(self.jeu)
    
        
    
    # choisi une carte aléatoirement pour le joueur 
    # Supprime la carte du jeu 
    def joueur(self):
        print(self.compteur_dernier)
        choix_aleatoire_cartes = random.randint(self.jeu[self.compteur_premier],self.jeu[self.compteur_dernier-4])
        if choix_aleatoire_cartes == 11 or choix_aleatoire_cartes == 12 or choix_aleatoire_cartes == 13:
            self.jeu_joueur+=10
        elif choix_aleatoire_cartes == 14:
            choisir_valeur = int(input("Vous pouvez choisir ce que vous preferer 1 ou 11"))
            self.jeu_joueur+=choix_valeur
        else:
            self.jeu_joueur+=choix_aleatoire_cartes 
        # cherche quelle carte le joueur a eu et la supprime du jeu de cartes
        for x in range(len(self.jeu)):
            if self.jeu_joueur == self.jeu[x]:
                del self.jeu[x]
                break # casse la boucle pour éviter quelle supprime toutes les meme cartes du meme chiffr
            
        self.compteur_dernier-=1
        
        return self.jeu_joueur,len(self.jeu)
    
    # séléctionne la première cartes au croupier et la supprime du jeu de cartes 
    def croupier(self):
        
        choix_aleatoire_cartes = random.randint(self.jeu[self.compteur_premier],self.jeu[self.compteur_dernier])
        if choix_aleatoire_cartes == 11 or choix_aleatoire_cartes == 12 or choix_aleatoire_cartes == 13:
            self.jeu_croupier+=10
        elif choix_aleatoire_cartes == 14:
            choisir_valeur = int(input("Vous pouvez choisir ce que vous preferer 1 ou 11"))
            self.jeu_croupier+=choix_valeur
        else:
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
a = black.joueur()
print(a)
"""
start_game = True
if start_game:
    black.ajouter_cartes()
while start_game:
"""


