#!/bin/usr/env python2.7
# pong.py
# Simple Python version of Pong game
# latest version: 2/3/2015
__author__ = 'jcochran'

import pygame
from pygame import *
import sys, random
from ball import Ball
from paddle import Paddle

#constants for the game
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
DIMENSIONS = (WIDTH, HEIGHT) = (1000, 800)
pygame.init()

# prints the introductory directions to the screen
def showDirections(screen):
    font = pygame.font.Font(None, 50)
    dir1 = "Welcome to LoLPoNg!"
    dir1Text = font.render(dir1, 1, WHITE)
    dir1Rect = dir1Text.get_rect()
    dir1Rect.centerx = WIDTH/2
    dir1Rect.centery = HEIGHT/2-120
    dir2 = "Player 1 moves the paddle using W and X"
    dir2Text = font.render(dir2, 1, WHITE)
    dir2Rect = dir2Text.get_rect()
    dir2Rect.centerx = WIDTH/2
    dir2Rect.centery = HEIGHT/2-70
    dir3 = "Player 2 moves the paddle using up and down arrow"
    dir3Text = font.render(dir3, 1, WHITE)
    dir3Rect = dir3Text.get_rect()
    dir3Rect.centerx = WIDTH/2
    dir3Rect.centery = HEIGHT/2-20
    dir4 = "First player to 10 wins the game"
    dir4Text = font.render(dir4, 1, WHITE)
    dir4Rect = dir4Text.get_rect()
    dir4Rect.centerx = WIDTH/2
    dir4Rect.centery = HEIGHT/2+30
    dir5 = "Click the mouse anywhere to begin the game"
    dir5Text = font.render(dir5, 1, WHITE)
    dir5Rect = dir5Text.get_rect()
    dir5Rect.centerx = WIDTH/2
    dir5Rect.centery = HEIGHT/2+80

    screen.fill(BLACK)
    screen.blit(dir1Text, dir1Rect)
    screen.blit(dir2Text, dir2Rect)
    screen.blit(dir3Text, dir3Rect)
    screen.blit(dir4Text, dir4Rect)
    screen.blit(dir5Text, dir5Rect)
    pygame.display.flip()

# moves the paddles based on key press events
def movePaddles(p1Paddle, p2Paddle):
    keys = pygame.key.get_pressed()
    # p1Paddle move detection
    if keys[K_w] and p1Paddle.rect.top > 0:
        p1Paddle.moveUp()
    if keys[K_x]:
        p1Paddle.moveDown()
    # p2Paddle move detection
    if keys[K_UP]:
        p2Paddle.moveUp()
    if keys[K_DOWN]:
        p2Paddle.moveDown()

# updates the screen -- draws data elements to the screen
def updateScreen(screen, ball, p1Paddle, p2Paddle, p1Score, p2Score):
    screen.fill(BLACK)
    pygame.draw.line(screen, WHITE, (WIDTH/2, 0), (WIDTH/2, HEIGHT))
    pygame.draw.rect(screen, ball.color, ball)
    pygame.draw.rect(screen, p1Paddle.color, p1Paddle)
    pygame.draw.rect(screen, p2Paddle.color, p2Paddle)
    drawScore(screen, p1Score, p2Score)
    pygame.display.flip()

# fun stuff -- not used in this application
def changeBallColor(ball):
    red = random.randrange(0,256)
    blue = random.randrange(0,256)
    green = random.randrange(0,255)
    ball.color = (red, blue, green)

# draws player scores to the screen
def drawScore(screen, p1Score, p2Score):
    font = pygame.font.Font(None, 50)
    p1Text = font.render(str(p1Score), 1, WHITE)
    p2Text = font.render(str(p2Score), 1, WHITE)
    p1Rect = p1Text.get_rect()
    p2Rect = p2Text.get_rect()
    p1Rect.center = (WIDTH/2-50, 50)
    p2Rect.center = (WIDTH/2+50, 50)
    screen.blit(p1Text, p1Rect)
    screen.blit(p2Text, p2Rect)

# displays winner in the final loop block
def showWinner(screen, winner, p1Score, p2Score):
    font = pygame.font.Font(None, 50)
    whoWon = (winner + " wins by a score of:")
    showScore = ""
    if p1Score > p2Score:
        showScore += str(p1Score) + " - " + str(p2Score)
    else:
        showScore += str(p2Score) + " - " + str(p1Score)

    whoWonText = font.render(whoWon, 1, RED)
    whoWonRect = whoWonText.get_rect()
    whoWonRect.center = (WIDTH/2, HEIGHT/2-60)

    showScoreText = font.render(showScore, 1, RED)
    showScoreRect = showScoreText.get_rect()
    showScoreRect.center = (WIDTH/2, HEIGHT/2)

    exitText = font.render("Click the mouse to quit.", 1, RED)
    exitRect = exitText.get_rect()
    exitRect.center = (WIDTH/2, HEIGHT/2+60)

    screen.blit(whoWonText, whoWonRect)
    screen.blit(showScoreText, showScoreRect)
    screen.blit(exitText, exitRect)
    pygame.display.flip()

# main method for this game
def main():
    # variable declaration for this game
    screen = pygame.display.set_mode(DIMENSIONS)
    pygame.display.set_caption('LoLPoNg')
    ball = Ball(Rect(WIDTH/2-15, HEIGHT/2-15, 30, 30))
    p1Paddle = Paddle(Rect(20, HEIGHT/2-50, 20, 100))
    p2Paddle = Paddle(Rect(WIDTH-40, HEIGHT/2-50, 20, 100))
    p1Score = 0
    p2Score = 0

    # this is the A block - display directions
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == MOUSEBUTTONDOWN:
                intro = False
        showDirections(screen)

    # this declares the random first serve
    ranx = random.randrange(0,2)
    if ranx == 0:
        ranx = random.randrange(-4,-2)
    else:
        ranx = random.randrange(4,6)
    rany = random.randrange(-3,-1)
    ball.xs = ranx
    ball.ys = rany
    waitCount = 0
    # this is the B block - main game loop
    while p1Score < 3 and p2Score < 3:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)
        if waitCount < 100:
            waitCount += 1
            movePaddles(p1Paddle, p2Paddle)
            updateScreen(screen, ball, p1Paddle, p2Paddle, p1Score, p2Score)
        else:
            ball.move()
            movePaddles(p1Paddle, p2Paddle)
            updateScreen(screen, ball, p1Paddle, p2Paddle, p1Score, p2Score)
            # this code bounces the ball off a paddle
            if ball.colliding_with(p1Paddle.rect):
                ball.rect.left = p1Paddle.rect.right+1
                ball.xs *= -1
            if ball.colliding_with(p2Paddle.rect):
                ball.rect.right = p2Paddle.rect.left-1
                ball.xs *= -1
            # if the ball bounces on top/bottom of screen
            if ball.rect.top < 3:
                ball.rect.top = 3
                ball.ys *= -1
            if ball.rect.bottom > HEIGHT-3:
                ball.rect.bottom = HEIGHT-3
                ball.ys *= -1
            #if the ball leaves the screen: who gets the point?
            if ball.rect.right < 0:
                p2Score += 1
                ball.rect.center = (WIDTH/2, HEIGHT/2)
                waitCount = 0
            if ball.rect.left > WIDTH:
                p1Score += 1
                ball.rect.center = (WIDTH/2, HEIGHT/2)
                waitCount = 0
    # refresh the screen to draw final score
    updateScreen(screen, ball, p1Paddle, p2Paddle, p1Score, p2Score)
    # this is the final C block
    while True:
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                pygame.quit()
                sys.exit(0)
        if p1Score > p2Score:
            showWinner(screen,"Player 1",p1Score,p2Score)
        else:
            showWinner(screen,"Player 2",p1Score,p2Score)

main()

























