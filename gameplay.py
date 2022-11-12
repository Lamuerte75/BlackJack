from black_jack import BlackJack as bj

class gameplay:
    def __init__(self,tour=1):
        self.startgame = True 
        self.tour = tour
        
    def game(self):
        if self.startgame ==  True and self.tour == 1:
            bj.ajouter_cartes_et_bruler(self,[],0,51) # Fonctionne
            
            bj.joueur(self,bj.ajouter_cartes_et_bruler(self,[],0,51)) # n'arrive pas à définir la variable jeu 
            #bj.croupier(self)
            #bj.joueur(self)
            

        
        


game = gameplay()
a = game.game()
