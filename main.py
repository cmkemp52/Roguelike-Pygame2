import pygame
import os
from classes import *
from floors import *

#! Parameters
WIDTH = 800 #width of window
HEIGHT = 600 #height of window
FPS = 30 #game FPS
gturn = 0 #global turn count
cfloor = floor1 #current floor variable
cmons = floor1mons #current monster locations

def floorcreation():
    #deletes old floor
    for sprite in all_sprites:
        if sprite.type == "floor":
            sprite.kill()
        if sprite.type == "enemy":
            sprite.kill()
    for i in range(len(cfloor)):
        for x in range(len(cfloor[i])):
            if cfloor[i][x] == 9:
                floorsprite = Void([i,x])
            elif cfloor[i][x] == 0:
                floorsprite = Dirt([i,x])
            elif cfloor[i][x] == 1:
                floorsprite = Wall([i,x])
            else:
                floorsprite = Floorsprite([i,x])
            all_sprites.add(floorsprite)

#! initialize game and create window
pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Abraham Lincoln") #caption for top of window
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group() #group that contains all sprites
floorcreation()

#! main game loop
running = True
while running:
    clock.tick(FPS)#runs loop at FPS
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
    all_sprites.update() #update all sprites
    screen.fill(BLACK) #set background to black
    all_sprites.draw(screen) #draws all sprites to screen
    pygame.display.flip() #syncs screen


pygame.quit()