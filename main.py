import sys, random
import pygame as pg



class Jeu:
    #cette classe va contenir toutes les variables ainsi que toutes les fonctions utiles pour le bon déroulement du jeu
    
    def __init__(self):
        self.ecran = pg.display.set_mode((800, 600))
        pg.display.set_caption("Jeu Snake")
        self.jeu_en_cours = True
        
        
        #creer la position du serpent
        self.serpent_position_x = 300
        self.serpent_position_y = 300
        self.serpent_direction_x = 0
        self.serpent_direction_y = 0
        self.serpent_corps = 10

        #créer la position de la pomme
        self.pomme_position_x = random.randrange(110, 590, 10)
        self.pomme_position_y = random.randrange(110, 390, 10)
        self.pomme = 10
        
        #fixer les fps du jeu
        self.clock = pg.time.Clock()
        
        
    def fonction_principale(self):
        #permet de gérer les événements, ainsi qu'afficher certains composants du jeu grâce aux while loop
        while self.jeu_en_cours:
            for evenement in pg.event.get():
                #print(evenement)
                
                #creation d'un événement qui permet de quitter en cliquant sur la croix 
                if evenement.type == pg.QUIT:
                    sys.exit()
                
                #creer les événements qui permetttent de faire bouger le serpent
                
                if evenement.type == pg.KEYDOWN:
                    if evenement.key == pg.K_RIGHT:
                        self.serpent_direction_x = 10
                        self.serpent_direction_y = 0
                        #print("A DROITE")
                        
                    if evenement.key == pg.K_LEFT:
                        self.serpent_direction_x = -10
                        self.serpent_direction_y = 0
                        #print("A GAUCHE")
                        
                    if evenement.key == pg.K_DOWN:
                        self.serpent_direction_y = 10
                        self.serpent_direction_x = 0
                        #print("EN BAS")
                        
                    if evenement.key == pg.K_UP:
                        self.serpent_direction_y = -10
                        self.serpent_direction_x = 0
                        #print("EN HAUT")
                    
        
            #faire bouger le serpent        
            self.serpent_position_x += self.serpent_direction_x
            self.serpent_position_y += self.serpent_direction_y
            #print(self.serpent_position_x, self.serpent_position_y)
            
            #faire bouger la pomme si le serpent la mange
            if self.pomme_position_y == self.serpent_position_y and self.serpent_position_x == self.pomme_position_x:
                print("OK")
                self.pomme_position_x = random.randrange(110, 590, 10)
                self.pomme_position_y = random.randrange(110, 390, 10)
                
                
            #faire bouger le serpent si il se trouve dans les limites du jeu
            if self.serpent_position_x < 102 or self.serpent_position_x > 688 \
                or self.serpent_position_y < 102 or self.serpent_position_y > 487:
                    sys.exit()
            
                
            self.ecran.fill((0, 0, 0))
            
            #afficher les limites 
            self.limites()
            
            #afficher la pomme
            pg.draw.rect(self.ecran,(255,0,0),(self.pomme_position_x, self.pomme_position_y, self.pomme, self.pomme))
            
            #afficher le serpent
            pg.draw.rect(self.ecran, (0, 125, 0), (self.serpent_position_x, self.serpent_position_y, self.serpent_corps, self.serpent_corps))
            
            self.clock.tick(22)
            pg.display.flip()
            
    
    def limites(self):
        pg.draw.rect(self.ecran, (255,255,255), (100, 100, 600, 400), 3)
            
if __name__ == '__main__':
    pg.init()
    Jeu().fonction_principale()
    pg.quit()
