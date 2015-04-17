__author__ = 'jcochran'

import pygame
from pygame import *
from images import Images

class Ship(pygame.sprite.Sprite):
    name = None
    baseImg = None
    death1Img = None
    death2Img = None

    def __init__(self, img1, name, group, xPos, yPos):
        pygame.sprite.Sprite.__init__(self)
        self.group = group
        self.name = name
        self.baseImg = img1
        self.death1Img = Images.deadship1
        self.death2Img = Images.deadship2
        self.image = self.baseImg
        self.rect = self.image.get_rect()
        self.rect.center = (xPos, yPos)

    def show_hit(self):
        self.image = Images.deadship1
        self.moveCount = 0

    # override the update method of the Sprite class
    def update(self, x):
        # move the ship left or right based on keyboard
        # input being sent by the main game loop
        if self.image == self.baseImg:
            self.rect.move_ip(x, 0)
        else:
            self.moveCount += 1
            if self.moveCount > 15:
                self.image = self.death2Img
            if self.moveCount > 30:
                self.image = self.death1Img
            if self.moveCount == 45:
                self.kill()


