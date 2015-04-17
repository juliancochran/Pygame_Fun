__author__ = 'jcochran'

import pygame
from pygame import *

class Sounds:
    pygame.mixer.init(44100, -16, 2, 2048)
    shot = pygame.mixer.Sound("snd/shoot.wav")
    aliendies = pygame.mixer.Sound("snd/invaderkilled.wav")
    shipdies = pygame.mixer.Sound("snd/explosion.wav")