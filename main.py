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


    def fonction_principale(self):
        #permet de gérer les événements, ainsi qu'afficher certains composants du jeu grâce aux while loop
        while self.jeu_en_cours:
            for evenement in pg.event.get():
                print(evenement)
                if evenement.type == pg.QUIT:
                    sys.exit()
                
                #creer les événements qui permetttent de faire bouger le serpent
                
                if evenement.type == pg.KEYDOWN:
                    if evenement.key == pg.K_RIGHT:
                        self.serpent_direction_x = 0.07
                        self.serpent_direction_y = 0
                        print("A DROITE")
                        
                    if evenement.key == pg.K_LEFT:
                        self.serpent_direction_x = -0.07
                        self.serpent_direction_y = 0
                        print("A GAUCHE")
                        
                    if evenement.key == pg.K_DOWN:
                        self.serpent_direction_y = 0.07
                        self.serpent_direction_x = 0
                        print("EN BAS")
                        
                    if evenement.key == pg.K_UP:
                        self.serpent_direction_y = -0.07
                        self.serpent_direction_x = 0
                        print("EN HAUT")
                    
            self.serpent_position_x += self.serpent_direction_x
            self.serpent_position_y += self.serpent_direction_y
            print(self.serpent_position_x, self.serpent_position_y)
            
            
            #faire bouger le serpent
            
            
            #faire bouger le serpent si il se trouve dans les limites du jeu
            if self.serpent_position_x < 102 or self.serpent_position_x > 688 \
                or self.serpent_position_y < 102 or self.serpent_position_y > 487:
                    sys.exit()
            
            
            self.ecran.fill((0, 0, 0))
            
            #afficher les limites 
            self.limites()
            
            #afficher le serpent
            pg.draw.rect(self.ecran, (0, 125, 0), (self.serpent_position_x, self.serpent_position_y, self.serpent_corps, self.serpent_corps))
            
            pg.display.flip()
            
    
    def limites(self):
        pg.draw.rect(self.ecran, (255,255,255), (100, 100, 600, 400), 3)
            
if __name__ == '__main__':
    pg.init()
    Jeu().fonction_principale()
    pg.quit()
