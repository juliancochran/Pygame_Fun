#!/bin/usr/env python2.7
import sys, pygame
from pygame import *
import random

class Sounds:
	pygame.mixer.init(44100, -16, 2, 2048)
	eatSounds = []
	dieSounds = []
	
	eatSounds.append(pygame.mixer.Sound("eatsound/ah.wav"))
	eatSounds.append(pygame.mixer.Sound("eatsound/bottle_pop_2.wav"))
	eatSounds.append(pygame.mixer.Sound("eatsound/bottle_pop_3.wav"))
	eatSounds.append(pygame.mixer.Sound("eatsound/friday-rocks.wav"))
	eatSounds.append(pygame.mixer.Sound("eatsound/hey.wav"))
	eatSounds.append(pygame.mixer.Sound("eatsound/mmm-2.wav"))
	eatSounds.append(pygame.mixer.Sound("eatsound/nice-work.wav"))
	eatSounds.append(pygame.mixer.Sound("eatsound/squeeze-toy-1.wav"))
	eatSounds.append(pygame.mixer.Sound("eatsound/wine-glass-clink-2.wav"))
	eatSounds.append(pygame.mixer.Sound("eatsound/woohoo.wav"))
	eatSounds.append(pygame.mixer.Sound("eatsound/yeah.wav"))
	eatSounds.append(pygame.mixer.Sound("eatsound/yes_1.wav"))
	eatSounds.append(pygame.mixer.Sound("eatsound/yes_2.wav"))
	eatSounds.append(pygame.mixer.Sound("eatsound/you_got_it_1.wav"))
	eatSounds.append(pygame.mixer.Sound("eatsound/you_got_it_2.wav"))
	eatSounds.append(pygame.mixer.Sound("eatsound/yummy.wav"))

	dieSounds.append(pygame.mixer.Sound("diesound/bye-bye-1.wav"))
	dieSounds.append(pygame.mixer.Sound("diesound/bye-bye-2.wav"))
	dieSounds.append(pygame.mixer.Sound("diesound/bye.wav"))
	dieSounds.append(pygame.mixer.Sound("diesound/i-dont-think-so-1.wav"))
	dieSounds.append(pygame.mixer.Sound("diesound/i-dont-think-so-2.wav"))
	dieSounds.append(pygame.mixer.Sound("diesound/im-in-trouble.wav"))
	dieSounds.append(pygame.mixer.Sound("diesound/maybe-next-time-huh.wav"))
	dieSounds.append(pygame.mixer.Sound("diesound/maybe-next-time.wav"))
	dieSounds.append(pygame.mixer.Sound("diesound/no-6.wav"))
	dieSounds.append(pygame.mixer.Sound("diesound/okay-bye.wav"))
	dieSounds.append(pygame.mixer.Sound("diesound/poor-baby.wav"))
	dieSounds.append(pygame.mixer.Sound("diesound/thats-pretty-much-it.wav"))
	
	def randomEat(self):
		random.choice(self.eatSounds).play()
		
	def randomDie(self):
		random.choice(self.dieSounds).play()
