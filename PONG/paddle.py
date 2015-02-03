#!/bin/usr/env python2.7
# paddle.py
# Object representation of a paddle for Pong game
# 01/30/2015
__author__ = 'jcochran'

import pygame
from pygame import *

class Paddle:
    rect = None
    color = (255,255,255)

    def __init__(self, r):
        self.rect = r

    def moveUp(self):
        self.rect.move_ip(0,-3)

    def moveDown(self):
        self.rect.move_ip(0,3)

    def colliding_with(self, other):
        return self.rect.colliderect(other)









