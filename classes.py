import pygame
import os

#! setting up images
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'img')
spritesheet = pygame.image.load(os.path.join(img_folder, 'backgroundsheet.png'))
BLACK = (0, 0, 0) #hex value of black
GREEN = (0, 255, 0) #hex value of green

#returns 17x, helpful for setting up spritesheet images
def x17(x):
    return x*17

#! base sprite class for floors
class Floorsprite(pygame.sprite.Sprite):
    #sprite initialization
    def __init__(self,loc):
        self.name = "empty" #name, helpful to find types of floors
        self.loc = loc #location on board
        self.floorsetup() 
        self.travel = False #whether or not player can travel on it
        self.image.fill(GREEN)
    #default setup for every floor
    def floorsetup(self):
        pygame.sprite.Sprite.__init__(self)
        self.type = "floor" #type, helpful to grab all floors
        self.image = pygame.Surface((16, 16))
        self.rect = self.image.get_rect()
        self.rect.center = [400+self.loc[0]*16,50+self.loc[1]*16]
class Void(Floorsprite):
    def __init__(self,loc):
        self.name = "void" #name, helpful to find types of floors
        self.loc = loc #location on board
        self.floorsetup() 
        self.travel = False #whether or not player can travel on it
        self.image.fill(BLACK)
class Dirt(Floorsprite):
    def __init__(self, loc):
        self.name = "dirt"
        self.loc = loc
        self.floorsetup()
        self.travel = True
        self.image.blit(spritesheet, (0,0), (x17(10),x17(8),16,16))
class Wall(Floorsprite):
    def __init__(self, loc):
        self.name = "wall"
        self.loc = loc
        self.floorsetup()
        self.travel = False
        self.image.blit(spritesheet, (0,0), (x17(10),x17(2),16,16))
