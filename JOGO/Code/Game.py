#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame as pygame
from pygame import Surface
from pygame.font import Font

from Code.Const import WIN_HEIGHT, WIN_WIDTH
from Code.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu.run()


