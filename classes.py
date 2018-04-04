#! /usr/bin/env python3
# -*- coding:Utf-8 -*-
import json
import random
import pygame
from pygame.locals import *

WHITE = (255, 255, 255)
image_win = pygame.image.load("Pictures/win.bmp")
image_lose = pygame.image.load("Pictures/lose.bmp")

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
        self.win = False

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
        self.win_lose()

    def win_lose(self):
        if self.aiguille[1] == False and self.tube[1] == False and self.ether[1] == False :
            self.win = True
        else :
            self.win = False

class Player():
    def __init__(self):
        self.image_player = pygame.image.load("Pictures/Mcgyver.bmp")
        self.image_player.set_colorkey(WHITE)
        self.coord_player = [30, 30]
        self.wins = False

    def generate_player(self, window):
        window.blit(self.image_player, (self.coord_player[0], self.coord_player[1]))

    def move_player(self, window, x, y, grille, win):
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

        index_ligne = int(self.coord_player[0]/30)
        index_colomn = int(self.coord_player[1]/30)
        if grille[index_colomn][index_ligne] == 0 :
            self.coord_player[0] = self.coord_player[0] - x
            self.coord_player[1] = self.coord_player[1] - y
        elif grille[index_colomn][index_ligne] == 3 :
            self.coord_player[0] = self.coord_player[0] - x
            self.coord_player[1] = self.coord_player[1] - y

            if win == True:
                self.wins = True
                window.blit(image_win, (0, 150))
            else:
                self.wins = True
                window.blit(image_lose, (0, 150))

        self.generate_player(window)
