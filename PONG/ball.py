#!/bin/usr/env python2.7
# class for a ball object in pygame
# 01/23/2015
__author__ = 'Julian Cochran, NC, USA'

import pygame
from pygame import *

class Ball:
    rect = None
    color = (255,0,0) #default: red stored as a tuple
    sx = 0
    sy = 0

    def __init__(self, r, c, x, y):
        self.rect = r
        self.color = c
        self.sx = x
        self.sy = y

    def collidingWith(self, other):
        return isinstance(other, pygame.Rect) and rect.colliderect(other)

