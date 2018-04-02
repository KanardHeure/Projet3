# -*- coding:Utf-8 -*-
import pygame
from pygame.locals import *
import function as func
import random
import json


pygame.init()

size = (550 , 450)

pygame.display.set_caption("Projet 3: Aide Mc Gyver")
background = pygame.image.load("Pictures/Background.bmp")
cote = pygame.image.load("Pictures/font_cote.bmp")
window = pygame.display.set_mode(size)
window.blit(background, (0, 0))
window.blit(cote, (450, 0))

grille = json.load(open("grille.json"))


game = True
func.draw_grille(window, grille)

player = func.Player()
player.generate_player(window)
item = func.Item()
item.generate_item(window, grille)


while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        elif event.type == pygame.KEYDOWN:
            window.blit(background, (0, 0))            
            func.draw_grille(window, grille)

            if event.key == K_RIGHT:
                print("droite")
                player.move_player(window, 30, 0, grille)
            elif event.key == K_LEFT:
                print("gauche")
                player.move_player(window, -30, 0, grille)
            elif event.key == K_UP:
                print("haut")
                player.move_player(window, 0, -30, grille)
            elif event.key == K_DOWN:
                print("bas")
                player.move_player(window, 0, 30, grille)
            item.check_item((player.coord_player[0],player.coord_player[1]))
            item.draw_item(window)

    pygame.display.flip()


pygame.quit()