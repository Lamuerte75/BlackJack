import random 
class BlackJack:
    def __init__(self,la_main_du_joueur=0,la_main_du_croupier=0,derniere_carte=51):
        self.liste_de_la_main_du_joueur = []
        self.liste_de_la_main_du_croupier = []
        self.la_main_du_joueur = la_main_du_joueur
        self.la_main_du_croupier = la_main_du_croupier
        self.derniere_carte = derniere_carte
        self.jeu_de_carte = []
    # ajoute les cartes dans le jeu de cartes et en supprime 5 (on les brules)
    def ajouter_cartes_et_bruler(self):
        valeur_de_la_carte = 2 # permettra de mettre les cartes dans la liste jeu
        # on place chaque carte 4 fois, ici nous nous intérrésons seulement au valeur de la carte
        for _ in range(13):
            for x in range(4):
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
        # Steps
        # choisi une carte aléatoirement pour le joueur 
        # On le met dans une liste avec les bons termes des cartes Ex : 11 sera Vallée dans la liste
        # Puis on ajoute la valeur de la carte au jeu du joueur 
        # Supprime la carte du jeu 

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
            self.liste_jeu_joueur.append("AS")
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

        self.derniere_carte-=1
        print("La valeur de votre jeu est :",self.la_main_du_joueur)
        
    # séléctionne la première cartes au croupier et la supprime du jeu de cartes 
    def croupier(self):
        # Steps
        # choisi une carte aléatoirement pour le croupier 
        # On le met dans une liste avec les bons termes des cartes Ex : 11 sera Vallée dans la liste
        # Puis on ajoute la valeur de la carte au jeu du croupier 
        # Supprime la carte du jeu 
        
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
            print("Vous avez tirée un ",choix_aleatoire_carte)
            self.liste_de_la_main_du_croupier.append(choix_aleatoire_carte)
            self.la_main_du_croupier+=choix_aleatoire_carte
            
    # cherche quelle carte le joueur a eu et la supprime du jeu de cartes
        for carte in range(len(self.jeu_de_carte)):
            if choix_aleatoire_carte == self.jeu_de_carte[carte]:
                del self.jeu_de_carte[carte]
                break # pour eviter de supprimer les autres cartes de même valeur 
    
                self.derniere_carte-=1
        print("La valeur du jeu du croupier est :",self.la_main_du_croupier)
            
 
        return self.liste_de_la_main_du_croupier
    
    def voir_le_jeu_joueur(self):
        #Permet de voir le  jeu du joueur 
        for x in range(len(self.liste_de_la_main_du_joueur)):
            self.liste_de_la_main_du_joueur[x],end="")

    def voir_le_jeu_croupier(self):
        # Permet de voir le jeu du croupier
        for x in range(len(self.liste_de_la_main_du_croupier)):
            print("Le croupier a ",self.liste_de_la_main_du_croupier[x],end=" ")
        
    def gameplay(self):
        pass
    def probability_to_win(self):
        pass
        
black = BlackJack()
start_game = True
tour = 1
if  tour == 1:
    #Si la partie commence on ajoute les cartes
    black.ajouter_cartes_et_bruler() # ajoute les jeu de carte
    black.joueur()
    black.croupier()
    black.joueur()
print("Le croupier distribue les cartes")
# Quand le tour est de 1 le joueur recoit deux cartes et le croupier une 


while start_game:
    black.voir_le_jeu_joueur()
    choisir_de_tirer_une_autre_carte_joueur = input("Si vous voulez recevoir encore une carte taper 1 sinon appuyer sur n'importe quelle touche")
    if choisir_de_tirer_une_autre_carte_joueur == 1:
        black.joueur()
    black.voir_le_jeu_croupier()
    choisir_de_tirer_une_autre_carte_croupier = input("Si vous voulez recevoir encore une carte taper 1 sinon appuyer sur n'importe quelle touche")
    if choisir_de_tirer_une_aure_carte_croupier == 1:
        black.croupier()
        
        



    



