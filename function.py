# -*- coding:Utf-8 -*-
import pygame
from pygame.locals import *
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
wall = pygame.image.load("wall.bmp")

def draw_rect(window, color, x, y):
    pygame.draw.rect(window, color, [x, y, 30, 30])


def random_rect(window):
    color = random.randint(0,4)
    if color == 0:
        color = BLACK
    elif color == 1:
        color = RED
    elif color == 2:
        color = GREEN
    elif color == 3:
        color = WHITE
    elif color == 4:
        color = BLUE

    x = random.randrange(0, 450, 30)
    y = random.randrange(0, 450, 30)
    draw_rect(window, color, x, y)

def draw_ligne(window, ligne):
    x = 0
    for case in ligne:
        if case == 0:
            color = BLACK
        elif case == 1:
            color = RED
        elif case == 2:
            color = GREEN
        elif case == 3:
            color = WHITE
        elif case == 4:
            color = BLUE
        if x == 0:
            x = 0
        y = 0
        draw_rect(window, color, x, y)
        x = x + 30

def draw_grille(window, grille):
    x = 0
    y = 0
    i = 0
    j = 0
    for ligne in grille:
        for case in ligne:
            if case == 0:
                draw_wall(window, x, y)
            x = x + 30
        x = 0
        y = y + 30

def draw_wall(window, x, y):
    window.blit(wall, (x, y))


def draw_random_grille(window, grille):
    grille = clear_grille(grille)
    for ligne in grille:
        while len(ligne) <= 15 :
            x = random.randint(0, 1)
            ligne.append(x)
    draw_grille(window, grille)   

def clear_grille(grille):
    for ligne in grille:
        ligne.clear()
    return grille

class Case:
    def __init__(window):
        self.image = None
        self.wall = True # or false for way
        self.coord = (0, 0)
        self.height = 30 # hauteur
        self.width = 30 # Largeur
        self.window = window

