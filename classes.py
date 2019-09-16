# This is primarily for classes and helper functions

import pygame
import os
from floors import *
#group that contains all sprites
all_sprites = pygame.sprite.Group() 

#! setting up images
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'img')
spritesheet = pygame.image.load(os.path.join(img_folder, 'backgroundsheet.png'))
BLACK = (0, 0, 0) #hex value of black
GREEN = (0, 255, 0) #hex value of green

#returns 17x, helpful for setting up spritesheet images
def x17(x):
    return x*17

#checks if you can move into a location
def canmove(travelloc):
    for sprite in all_sprites:
        if sprite.loc == travelloc and sprite.travel == False:
            return False
    return True

def lineofsight(self):
    #list of all blocks in player line of sight
    inlos = []
    for x in range(1,self.vision+1):
        inlos.append([self.loc[0]-x,self.loc[1]])
        for y in range(1,self.vision+1):
            if self.loc[1]+y-x >= self.loc[1]:
                if [self.loc[0]+x,self.loc[1]+y-x] not in inlos:
                    inlos.append([self.loc[0]+x,self.loc[1]+y-x])
            if self.loc[1]-y+x <= self.loc[1]:
                if [self.loc[0]+x,self.loc[1]-y+x] not in inlos:
                    inlos.append([self.loc[0]+x,self.loc[1]-y+x])
            if self.loc[0]-x+y <= self.loc[0]:
                if [self.loc[0]-x+y,self.loc[1]+y] not in inlos:
                    inlos.append([self.loc[0]-x+y,self.loc[1]+y])
            if self.loc[1]-x+y <= self.loc[1]:
                if [self.loc[0]-x+y,self.loc[1]-y] not in inlos:
                    inlos.append([self.loc[0]-x+y,self.loc[1]-y])
    # outlos = []
    # for location in inlos:
    #     for sprite in all_sprites:
    #         if sprite.loc == location and sprite.transparent == False:
    #             outlos.append(location)
    # for location in outlos:
    #     if location[0] > self.loc[0]:
    #         if location[1] == self.loc[1]:
    #             for i in range(1,self.vision+1):
    #                 if [location[0]+1+i,location[1]] in inlos:
    #                     inlos.remove([location[0]+1+i,location[1]])
    #                 if [location[0]+1+i,location[1]-i] in inlos:
    #                     inlos.remove([location[0]+1+i,location[1]-i])
    #                 if [location[0]+1+i,location[1]+i]in inlos:
    #                     inlos.remove([location[0]+1+i,location[1]+i])
        # elif location[0] < player.loc[0]
        # elif location[1] > player.loc[1]
        # elif location[1] < player.loc[1]
    return inlos

#! Main player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = "Player"
        self.type = "Player"
        self.transparent = True
        self.loc = [2,2] #Starting location on board
        self.vision = 5 #how far player can see
        self.los = lineofsight(self)
        self.travel = False #whether or not you can move through
        self.image = pygame.Surface((16, 16))
        self.rect = self.image.get_rect()
        self.rect.center = [400+self.loc[0]*16,50+self.loc[1]*16]
    def moveright(self):
        if canmove([self.loc[0]+1,self.loc[1]]):
            self.loc = [self.loc[0]+1,self.loc[1]]
            self.rect.center = [self.rect.center[0]+16,self.rect.center[1]]
            self.los = lineofsight(self)
    def moveleft(self):
        if canmove([self.loc[0]-1,self.loc[1]]):
            self.loc = [self.loc[0]-1,self.loc[1]]
            self.rect.center = [self.rect.center[0]-16,self.rect.center[1]]
            self.los = lineofsight(self)
    def moveup(self):
        if canmove([self.loc[0],self.loc[1]-1]):
            self.loc = [self.loc[0],self.loc[1]-1]
            self.rect.center = [self.rect.center[0],self.rect.center[1]-16]
            self.los = lineofsight(self)
    def movedown(self):
        if canmove([self.loc[0],self.loc[1]+1]):
            self.loc = [self.loc[0],self.loc[1]+1]
            self.rect.center = [self.rect.center[0],self.rect.center[1]+16]
            self.los = lineofsight(self)

#! base sprite class for floors
class Floorsprite(pygame.sprite.Sprite):
    #sprite initialization
    def __init__(self,loc):
        self.name = "empty" #name, helpful to find types of floors
        self.loc = loc #location on board
        self.floorsetup() 
        self.transparent = True #whether or not you can see through
        self.travel = False #whether or not it can be travelled on
    #default setup for every floor
    def floorsetup(self):
        pygame.sprite.Sprite.__init__(self)
        self.type = "floor" #type, helpful to grab all floors
        self.image = pygame.Surface((16, 16))
        self.rect = self.image.get_rect()
        self.rect.center = [400+self.loc[0]*16,50+self.loc[1]*16]
    def sighted(self):
        self.image.fill(GREEN)
    def hide(self):
        self.image.fill(BLACK)
    def update(self):
        if self.loc in player.los:
            self.sighted()
        else:
            self.hide()
class Void(Floorsprite):
    def __init__(self,loc):
        self.name = "void" #name, helpful to find types of floors
        self.loc = loc #location on board
        self.floorsetup() 
        self.transparent = True
        self.travel = False #whether or not player can travel on it
    def sighted(self):
        self.image.fill(BLACK)
class Dirt(Floorsprite):
    def __init__(self, loc):
        self.name = "dirt"
        self.loc = loc
        self.floorsetup()
        self.transparent = True
        self.travel = True
    def sighted(self):
        self.image.blit(spritesheet, (0,0), (x17(10),x17(8),16,16))
class Wall(Floorsprite):
    def __init__(self, loc):
        self.name = "wall"
        self.loc = loc
        self.floorsetup()
        self.transparent = False
        self.travel = False
    def sighted(self):
        self.image.blit(spritesheet, (0,0), (x17(10),x17(2),16,16))

#! Enemy classes
class Enemy(pygame.sprite.Sprite):
    def __init__(self,loc):
        self.name = "enemy" #name, helpful to find types of enemies
        self.loc = loc #location on board
        self.enemysetup()
    def enemysetup(self):
        pygame.sprite.Sprite.__init__(self)
        self.transparent = True #whether or not you can see through
        self.travel = False #whether or not you can move through
        self.type = "enemy" #type, helpful to grab all enemies
        self.image = pygame.Surface((16, 16))
        self.rect = self.image.get_rect()
        self.rect.center = [400+self.loc[0]*16,50+self.loc[1]*16]
    def sighted(self):
        self.image.fill(GREEN)
    def hide(self):
        self.image.fill(BLACK)
    def update(self):
        if self.loc in player.los:
            self.sighted()
        else:
            self.hide()

class Goblin(Enemy):
    def __init__(self,loc):
        self.name = "goblin"
        self.loc = loc
        self.enemysetup()

def floorcreation():
    #deletes old floor
    for sprite in all_sprites:
        if sprite.type == "floor":
            sprite.kill()
        if sprite.type == "enemy":
            sprite.kill()
    #creates new floor tiles
    for i in range(len(cfloor)):
        for x in range(len(cfloor[i])):
            if cfloor[x][i] == 9:
                floorsprite = Void([i,x])
            elif cfloor[x][i] == 0:
                floorsprite = Dirt([i,x])
            elif cfloor[x][i] == 1:
                floorsprite = Wall([i,x])
            else:
                floorsprite = Floorsprite([i,x])
            all_sprites.add(floorsprite)
    #creates new monsters
    for mon in cmons:
        goblin = Goblin(mon)
        all_sprites.add(goblin)

player = Player()
floorcreation()
all_sprites.add(player)