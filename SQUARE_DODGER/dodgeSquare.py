#!/bin/usr/env python2.7
import sys, pygame
from pygame import *
import random
from sounds import Sounds

DIMENSIONS = (WIDTH,HEIGHT) = (900,700)
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
PURPLE = (127,0,127)
GOLD = (255,215,0)
colors = [RED, GREEN, BLUE, PURPLE, GOLD]

pygame.init()
screen = pygame.display.set_mode(DIMENSIONS)
square = Rect(WIDTH/2 - 50, HEIGHT/2 - 50, 100, 100)
circle = Rect(100, 100, 60, 60)
xs = random.randrange(4, 9)
ys = random.randrange(4, 9)
bumpCount = 0
car = pygame.image.load("carrot.png")
carBox = car.get_rect()
broc = pygame.image.load("broccoli.png")
brocBox = broc.get_rect()
cup = pygame.image.load("cupcake.png")
cupBox = cup.get_rect()
foodOnScreen = False
score = 0
sounds = Sounds()

if __name__ == "__main__":
	rancolor = random.choice(colors)
	running = True
	changeSpeed = True
	# this displays font to the screen
	font = pygame.font.Font(None, 40)
	dir = "Dodge the square using the arrow keys."
	dir2 = "Eat cupcakes. Click to start."
	dirText = font.render(dir, 1, WHITE)
	dir2Text = font.render(dir2, 1, WHITE)
	dirRect = dirText.get_rect()
	dir2Rect = dir2Text.get_rect()
	dirRect.center = (WIDTH/2, HEIGHT/2-20)
	dir2Rect.center = (WIDTH/2, HEIGHT/2+10)
	while running:
		for event in pygame.event.get():
			if event.type == MOUSEBUTTONDOWN:
				running = False
		screen.fill(BLACK)
		screen.blit(dirText, dirRect)
		screen.blit(dir2Text, dir2Rect)
		pygame.display.flip()
		
	#reset running to True now
	running = True
	while running:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
		screen.fill(BLACK)
		# the next five lines draw my score to the screen
		dir = str(score)
		dirText = font.render(dir, 1, WHITE)
		dirRect = dirText.get_rect()
		dirRect.center = (WIDTH-60, 60)
		screen.blit(dirText, dirRect)
		# these two lines draw my circle and the evil square!
		pygame.draw.rect(screen, rancolor, square)
		pygame.draw.ellipse(screen, GOLD, circle)
		# this draws food to the screen
		if not foodOnScreen:
			cupBox.center = (random.randrange(100, WIDTH-100),\
				random.randrange(100, HEIGHT-100))
			foodOnScreen = True
		else:
			screen.blit(cup, cupBox)
		# these lines of code move my hero circle
		keys = pygame.key.get_pressed()
		if keys[K_LEFT] and circle.left > 0:
			circle.move_ip(-8,0)
		if keys[K_RIGHT] and circle.right < WIDTH:
			circle.move_ip(8,0)
		if keys[K_UP] and circle.top > 0:
			circle.move_ip(0,-8)
		if keys[K_DOWN] and circle.bottom < HEIGHT:
			circle.move_ip(0,8)
		# this line moves the evil square
		square.move_ip(xs,ys)
		# these lines of code bounce the evil square
		if square.left < 2:
			xs *= -1
			bumpCount += 1
			rancolor = random.choice(colors)
		if square.right > WIDTH-2:
			xs *= -1
			bumpCount += 1
			rancolor = random.choice(colors)
		if square.top < 2:
			ys *= -1
			bumpCount += 1
			rancolor = random.choice(colors)
		if square.bottom > HEIGHT-2:
			ys *= -1
			bumpCount += 1
			rancolor = random.choice(colors)
		if (bumpCount+1) % 10 == 0 and changeSpeed:
			if xs < 0:
				xs -= 1
			else:
				xs += 1
			if ys < 0:
				ys -= 1
			else:
				ys += 1
			changeSpeed = False
		if (bumpCount+1) % 11 == 0:
			changeSpeed = True
		pygame.display.flip()
		# detect if the evil square has killed me!
		if square.colliderect(circle):
			running = False
		# eat food?
		if circle.colliderect(cupBox):
			sounds.randomEat()
			foodOnScreen = False
			score += 1
	# this is when I am dead
	dead = True
	dir2 = "Like waaah. You're dead. Play again soon."
	dir2Text = font.render(dir2, 1, WHITE)
	dir2Rect = dir2Text.get_rect()
	dir2Rect.center = (WIDTH/2, HEIGHT/2)
	sounds.randomDie()
	while dead:
		for event in pygame.event.get():
			if event.type == MOUSEBUTTONDOWN:
				pygame.quit()
				sys.exit()
		screen.fill(BLACK)
		screen.blit(dirText, dirRect)
		screen.blit(dir2Text, dir2Rect)
		pygame.display.flip()
	
	#print("Estoy muerto, amigo. Yo quiero Taco Bell. Adios.")
	
		






