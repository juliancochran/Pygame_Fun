__author__ = 'jcochran'

import pygame
from pygame import *
from images import Images

class Base(pygame.sprite.Sprite):
    images = None
    numLives = 6

    def __init__(self, group, xPos, yPos):
        pygame.sprite.Sprite.__init__(self)
        self.group = group
        self.images = []
        self.images.append(Images.base01)
        self.images.append(Images.base02)
        self.images.append(Images.base03)
        self.images.append(Images.base04)
        self.images.append(Images.base05)
        self.images.append(Images.base06)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.center = (xPos, yPos)

    def update(self):
        #self.numLives -= 1
        if self.numLives == 0:
            self.kill()
        else:
            self.image = self.images[6-self.numLives]