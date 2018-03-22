# -*- coding:Utf-8 -*-
import pygame
from pygame.locals import *
import function as func
import random
import json


pygame.init()

size = (450 , 450)

pygame.display.set_caption("Projet 3: Aide Mc Gyver")
background = pygame.image.load("Background.bmp")
wall = pygame.image.load("wall.bmp")
clock = pygame.time.Clock()
window = pygame.display.set_mode(size)
window.blit(background, (0, 0))

grille2 = json.load(open("grille.json"))


game = True
func.draw_grille(window, grille2)

player = func.Player()
player.generate_player(window)

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        elif event.type == pygame.KEYDOWN:
            window.blit(background, (0, 0))
            func.draw_grille(window, grille2)
            if event.key == K_RIGHT:
                print("droite")
                player.move_player(window, 30, 0, grille2)
            elif event.key == K_LEFT:
                print("gauche")
                player.move_player(window, -30, 0, grille2)
            elif event.key == K_UP:
                print("haut")
                player.move_player(window, 0, -30, grille2)
            elif event.key == K_DOWN:
                print("bas")
                player.move_player(window, 0, 30, grille2)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            window.blit(background, (0, 0))
            func.draw_random_grille(window)


    pygame.display.flip()


pygame.quit()