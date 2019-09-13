import pygame
import os
from classes import *
from floors import *

#! Parameters
WIDTH = 800 #width of window
HEIGHT = 600 #height of window
FPS = 30 #game FPS
gturn = 0 #global turn count

#! initialize game and create window
pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Abraham Lincoln") #caption for top of window
clock = pygame.time.Clock()


#! main game loop
running = True
while running:
    clock.tick(FPS)#runs loop at FPS
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.moveleft()
            if event.key == pygame.K_RIGHT:
                player.moveright()
            if event.key == pygame.K_UP:
                player.moveup()
            if event.key == pygame.K_DOWN:
                player.movedown()
    all_sprites.update() #update all sprites
    screen.fill(BLACK) #set background to black
    all_sprites.draw(screen) #draws all sprites to screen
    pygame.display.flip() #syncs screen


pygame.quit()