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
        self.image_player = pygame.image.load("Pictures/Mcgyver.bmp")
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
        self.font_aiguille = pygame.image.load("Pictures/font_aiguille.bmp")
        self.font_tube = pygame.image.load("Pictures/font_tube.bmp")
        self.font_ether = pygame.image.load("Pictures/font_ether.bmp")
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
        else:
            window.blit(self.font_aiguille, (455, 90))
        if self.tube[1] == True :
            window.blit(self.tube[0], self.tube[2])
        else:
            window.blit(self.font_tube, (455, 210))
        if self.ether[1] == True :
            window.blit(self.ether[0], self.ether[2])
        else:
            window.blit(self.font_ether, (455, 330))


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


