__author__ = 'jcochran'

import pygame
from pygame import *
import constants

class Missile(pygame.sprite.Sprite):
    name = None

    def __init__(self, img, name, group, xPos, yPos):
        pygame.sprite.Sprite.__init__(self)
        self.group = group
        self.name = name
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.center = (xPos, yPos)

    # override the update method of the Sprite class
    def update(self):
        # move the missile up or down based on name
        if self.name == "missile":
            self.rect.move_ip(0, -5)
            if self.rect.centery < 4:
                self.kill()
        else:
            self.rect.move_ip(0, 5)
            if self.rect.centery > constants.SCREEN_HEIGHT - 4:
                self.kill()








