#! /usr/bin/env python3
# -*- coding:Utf-8 -*-
""" Fichier principal """
import json
import time
import pygame
from pygame.locals import *

import function as func
import classes


def main():
    """ Fonction principal du programme """

    pygame.init()

    pygame.display.set_caption("Projet 3: Aide Mc Gyver")
    background = pygame.image.load("Pictures/Background.bmp")
    cote = pygame.image.load("Pictures/font_cote.bmp")

    size = (550, 450)
    window = pygame.display.set_mode(size)
    window.blit(background, (0, 0))
    window.blit(cote, (450, 0))

    grille = json.load(open("grille.json"))

    func.draw_grille(window, grille)

    player = classes.Player()
    player.generate_player(window)
    item = classes.Item()
    item.generate_item(window, grille)

    game = True

    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
            elif event.type == pygame.KEYDOWN:
                window.blit(background, (0, 0))
                func.draw_grille(window, grille)

                if event.key == K_RIGHT:
                    player.move_player(window, 30, 0, grille, item.win)
                elif event.key == K_LEFT:
                    player.move_player(window, -30, 0, grille, item.win)
                elif event.key == K_UP:
                    player.move_player(window, 0, -30, grille, item.win)
                elif event.key == K_DOWN:
                    player.move_player(window, 0, 30, grille, item.win)

                if player.wins is False:
                    item.check_item((player.coord_player[0], player.coord_player[1]))
                    item.draw_item(window)
                if player.wins is True:
                    game = False

        pygame.display.flip()

    time.sleep(3)
    pygame.quit()

if __name__ == "__main__":
    main()
else:
    print("Se script n'est pas fait pour être importé")
