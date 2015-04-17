__author__ = 'jcochran'

import pygame
from pygame import *
from images import Images

class Alien(pygame.sprite.Sprite):
    name = None
    baseImg = None
    swapImg = None
    moveCount = 0
    goRight = True

    def __init__(self, img1, img2, name, group, xPos, yPos):
        pygame.sprite.Sprite.__init__(self)
        self.group = group
        self.name = name
        self.baseImg = img1
        self.swapImg = img2
        self.image = self.baseImg
        self.rect = self.image.get_rect()
        self.rect.center = (xPos, yPos)

    def show_hit(self):
        self.image = Images.deadalien
        self.moveCount = 0

    # override the update method of the Sprite class
    def update(self, x, y):
        #if I am dead, I can't move, right?
        if self.image != Images.deadalien:
            # do I move left or right?
            if self.goRight:
                self.rect.move_ip(x, 0)
            else:
                self.rect.move_ip(-x, 0)
            # add to my moveCount total
            self.moveCount += 1
            # swap my image
            if self.image == self.baseImg:
                self.image = self.swapImg
            elif self.image == self.swapImg:
                self.image = self.baseImg

            # should I start moving left now?
            if self.moveCount == 25:
                self.rect.move_ip(0, y)
                self.moveCount = 0
                self.goRight = not(self.goRight)

        else:
            self.moveCount += 1
            if self.moveCount == 3:
                self.kill()
