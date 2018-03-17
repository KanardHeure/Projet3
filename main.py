# -*- coding:Utf-8 -*-
import pygame
from pygame.locals import *
import function as func
import random
import json

pygame.init()

size = (450 , 450)

background = pygame.image.load("Background.bmp")
wall = pygame.image.load("wall.bmp")
clock = pygame.time.Clock()
window = pygame.display.set_mode(size)
window.blit(background, (0, 0))

[ligne_1, ligne_2, ligne_3, ligne_4, ligne_5, ligne_6, ligne_7, ligne_8, ligne_9, ligne_10, ligne_11, ligne_12, ligne_13, ligne_14, ligne_15] = [[] for i in range(15)]
grille = [ligne_1, ligne_2, ligne_3, ligne_4, ligne_5, ligne_6, ligne_7, ligne_8, ligne_9, ligne_10, ligne_11, ligne_12, ligne_13, ligne_14, ligne_15]
grille2 = json.load(open("grille.json"))

game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        elif event.type == pygame.KEYDOWN:
            print("Keydown")
            window.blit(background, (0, 0))
            func.draw_grille(window, grille2)
        elif event.type == pygame.KEYUP:
            print("Keyup")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            window.blit(background, (0, 0))
            func.draw_random_grille(window, grille)


    pygame.display.flip()


pygame.quit()