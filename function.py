# -*- coding:Utf-8 -*-
import pygame
from pygame.locals import *
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
wall = pygame.image.load("Pictures/wall.bmp")
start = pygame.image.load("Pictures/start.bmp")
aiguille = pygame.image.load("Pictures/aiguille.bmp")
tube = pygame.image.load("Pictures/tube.bmp")
ether = pygame.image.load("Pictures/ether.bmp")
ether.set_colorkey(WHITE)
aiguille.set_colorkey(WHITE)
tube.set_colorkey(WHITE)


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

def draw_item(window, item_aiguille, item_tube, item_ether):
    if item_aiguille[1] == True :
        window.blit(aiguille, item_aiguille[0])
    if item_tube[1] == True :
        window.blit(tube, item_tube[0])
    if item_ether[1] == True :
        window.blit(ether, item_ether[0])

def pop_items(grille):
    liste_chemin = []
    x = 0
    y = 0
    for liste in grille:
        for case in liste:
            if case == 1:
                liste_chemin.append((x, y))
            x = x + 30
        x = 0
        y = y + 30
    index = random.randint(0, (len(liste_chemin) - 1))
    coord_aiguille = liste_chemin[index]
    del liste_chemin[index]
    index = random.randint(0, (len(liste_chemin) - 1))
    coord_tube = liste_chemin[index]
    del liste_chemin[index]
    index = random.randint(0, (len(liste_chemin) - 1))
    coord_ether = liste_chemin[index]
    return coord_aiguille, coord_tube, coord_ether



class Player():
    def __init__(self):
        self.image_player = pygame.image.load("Pictures/macgyver.bmp")
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

class Item():
    def __init__(self):
        self.image_aiguille = pygame.image.load("Pictures/aiguille.bmp")
        self.image_tube = pygame.image.load("Pictures/tube.bmp")
        self.image_ether = pygame.image.load("Pictures/ether.bmp")
        self.image_ether.set_colorkey(WHITE)  
        self.image_aiguille.set_colorkey(WHITE)
        self.image_tube.set_colorkey(WHITE)
        self.aiguille = [self.image_aiguille, True]
        self.tube = [self.image_tube, True]
        self.ether = [self.image_ether, True]

    def generate_item(self, window, grille):
        liste_chemin = []
        x = 0
        y = 0
        for liste in grille:
            for case in liste:
                if case == 1:
                    liste_chemin.append((x, y))
                x = x + 30
            x = 0
            y = y + 30
        index = random.randint(0, (len(liste_chemin) - 1))
        self.coord_aiguille = liste_chemin[index]
        del liste_chemin[index]
        index = random.randint(0, (len(liste_chemin) - 1))
        self.coord_tube = liste_chemin[index]
        del liste_chemin[index]
        index = random.randint(0, (len(liste_chemin) - 1))
        self.coord_ether = liste_chemin[index]
        self.aiguille.append(self.coord_aiguille)
        self.tube.append(self.coord_tube)
        self.ether.append(self.coord_ether)
        self.draw_item(window)

    def draw_item(self, window):
        if self.aiguille[1] == True :
            window.blit(self.aiguille[0], self.aiguille[2])
        if self.tube[1] == True :
            window.blit(self.tube[0], self.tube[2])
        if self.ether[1] == True :
            window.blit(self.ether[0], self.ether[2])

    def check_item(self, coord_player):
        if coord_player == self.aiguille[2]:
            self.aiguille[1] = False
        if coord_player == self.tube[2]:
            self.tube[1] = False
        if coord_player == self.ether[2]:
            self.ether[1] = False



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
