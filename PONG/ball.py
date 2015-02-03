#!/bin/usr/env python2.7
# ball.py
# Object representation of a ball
# 01/26/2015
__author__ = 'jcochran'

import pygame
from pygame import *

class Ball:
    rect = None
    color = (255,255,255)
    xs = 0
    ys = 0

    def __init__(self, r):
        self.rect = r

    def move(self):
        self.rect.move_ip(self.xs, self.ys)

    def colliding_with(self, other):
        return self.rect.colliderect(other)









