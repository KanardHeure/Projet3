#! /usr/bin/env python3
# -*- coding:Utf-8 -*-
import pygame

WHITE = (255, 255, 255)
wall = pygame.image.load("Pictures/wall.bmp")
start = pygame.image.load("Pictures/start.bmp")
garde = pygame.image.load("Pictures/garde.bmp")
garde.set_colorkey(WHITE)

def draw_grille(window, grille):
    x = 0
    y = 0
    for ligne in grille:
        for case in ligne:
            if case == 0:
                window.blit(wall, (x, y))
                #draw_wall(window, x, y)
            elif case == 2:
                window.blit(start, (x, y))
                #draw_start(window, x, y)
            elif case == 3:
                window.blit(garde, (x, y))
            x = x + 30
        x = 0
        y = y + 30
