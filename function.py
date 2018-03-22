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
start = pygame.image.load("start.bmp")



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
            elif case == 2:
                draw_start(window, x, y)
            x = x + 30
        x = 0
        y = y + 30

def draw_wall(window, x, y):
    window.blit(wall, (x, y))

def draw_start(window, x, y):
    window.blit(start, (x, y))


class Player():
    def __init__(self):
        self.image_player = pygame.image.load("macgyver.bmp")
        self.image_player.set_colorkey(WHITE)
        self.coord_player = [30, 30]

    def generate_player(self, window):
        window.blit(self.image_player, (self.coord_player[0], self.coord_player[1]))

    def move_player(self, window, x, y, grille):
        self.coord_player[0] = self.coord_player[0] + x
        self.coord_player[1] = self.coord_player[1] + y
        if self.coord_player[0] < 0:
            self.coord_player[0] = 0
        if self.coord_player[1] < 0:
            self.coord_player[1] = 0
        if self.coord_player[0] > 420:
            self.coord_player[0] = 420
        if self.coord_player[1] > 420:
            self.coord_player[1] = 420           

        wall = check_wall(grille, self.coord_player)
        if wall:
            self.coord_player[0] = self.coord_player[0] - x
            self.coord_player[1] = self.coord_player[1] - y

        self.generate_player(window)

def check_wall(grille, coord):
    index_ligne = int(coord[0] / 30)
    index_colomn = int(coord[1] / 30)
    if grille[index_colomn][index_ligne] == 0:
        return True
    else:
        return False



def draw_random_grille(window):
    [ligne_1, ligne_2, ligne_3, ligne_4, ligne_5, ligne_6, ligne_7, ligne_8, ligne_9, ligne_10, ligne_11, ligne_12, ligne_13, ligne_14, ligne_15] = [[] for i in range(15)]
    grille = [ligne_1, ligne_2, ligne_3, ligne_4, ligne_5, ligne_6, ligne_7, ligne_8, ligne_9, ligne_10, ligne_11, ligne_12, ligne_13, ligne_14, ligne_15]

    for ligne in grille:
        while len(ligne) <= 15 :
            x = random.randint(0, 1)
            ligne.append(x)
    draw_grille(window, grille)   
