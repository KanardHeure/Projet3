#! /usr/bin/env python3
# -*- coding:Utf-8 -*-
""" Fonction """
import pygame

WHITE = (255, 255, 255)
WALL = pygame.image.load("Pictures/wall.bmp")
START = pygame.image.load("Pictures/start.bmp")
GARDE = pygame.image.load("Pictures/garde.bmp")
GARDE.set_colorkey(WHITE)

def draw_grille(window, grille):
    """ Permet de créer la grille de jeu """
    x_pixel = 0
    y_pixel = 0
    for ligne in grille:
        for case in ligne:
            if case == 0:
                window.blit(WALL, (x_pixel, y_pixel))
            elif case == 2:
                window.blit(START, (x_pixel, y_pixel))
            elif case == 3:
                window.blit(GARDE, (x_pixel, y_pixel))
            x_pixel = x_pixel + 30
        x_pixel = 0
        y_pixel = y_pixel + 30
