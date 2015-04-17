__author__ = 'jcochran'

import pygame
from pygame import *
import sys
import constants
import random
from images import Images
from alien import Alien
from ship import Ship
from missile import Missile
from base import Base
from sounds import Sounds

class SpaceInvaders:
    screen = None
    spSurface = None
    aliens = None
    ship = None
    missile = None
    bombs = None
    bases = None
    display = None
    gameLoop = True
    numLives = 3

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((constants.SCREEN_WIDTH,
                                  constants.SCREEN_HEIGHT), 0, 0)
        self.spSurface = pygame.Surface((constants.SCREEN_WIDTH,
                                         constants.SCREEN_HEIGHT))
        self.aliens = pygame.sprite.Group()
        self.ship = pygame.sprite.Group()
        self.missile = pygame.sprite.Group()
        self.bombs = pygame.sprite.Group()
        self.bases = pygame.sprite.Group()

        # create and initialize the aliens
        xPos = 80
        for i in range(0, 13):
            self.aliens.add(Alien(Images.alien01a, Images.alien01b,
                                  "Bob", 4, xPos, 100))
            self.aliens.add(Alien(Images.alien02a, Images.alien02b,
                                  "Tom", 4, xPos, 150))
            self.aliens.add(Alien(Images.alien03a, Images.alien03b,
                                  "Sam", 4, xPos, 200))
            xPos += 50
        # create and initialize the user's ship
        self.ship.add(Ship(Images.ship, "hero", 1,
                           constants.SCREEN_WIDTH/2,
                           constants.SCREEN_HEIGHT-100))

        # create and initialize the bases
        xPos = 164
        for i in range(0,4):
            self.bases.add(Base(1, xPos, constants.SCREEN_HEIGHT-200))
            xPos += 165

    def updateAliens(self):
        self.aliens.update(2, 15)

    def dropBombs(self):
        # randomly drop a bomb here
        if random.randrange(0, 101) > 99:
            if(len(self.aliens.sprites()) > 0):
                list = self.aliens.sprites()
                #print(len(list))
                index = random.randrange(0, len(list))
                #print(index)
                ranAlien = list[index]
                self.bombs.add(Missile(Images.bomb2, "bomb", 4,
                                       ranAlien.rect.centerx,
                                       ranAlien.rect.centery+10))
            # else no aliens left on the screen - game over
        # else don't make a new bomb
        self.bombs.update()
        bombList = self.bombs.sprites()
        # look for collisions between bombs and bases or
        # bombs and ships
        if len(bombList) > 0:
            for bomb in bombList:
                # base collision?
                base_hit = pygame.sprite.spritecollide(bomb,
                                            self.bases, False)
                # ship collision?
                ship_hit = pygame.sprite.spritecollide(bomb,
                                            self.ship, False)
                if len(base_hit) > 0:
                    for base in base_hit:
                        base.numLives -= 1
                        bomb.kill()
                if len(ship_hit) > 0:
                    ship_hit[0].show_hit()
                    bomb.kill()
                    Sounds.shipdies.play()
                    self.gameLoop = False

    def moveMissile(self):
        self.missile.update()
        # check for enemy collision
        if len(self.missile.sprites()) > 0:
            temp = self.missile.sprites()[0]
            alien_hit = pygame.sprite.spritecollide(temp, self.aliens,
                                                    False)
            if len(alien_hit) > 0:
                alien_hit[0].show_hit()
                temp.kill()
                Sounds.aliendies.play()

    def processKeys(self):
        # process keydown events
        keys = pygame.key.get_pressed()
        if keys[K_LEFT]:
            self.ship.update(-4)
        if keys[K_RIGHT]:
            self.ship.update(4)
        if keys[K_SPACE]:
            if len(self.missile.sprites()) == 0:
                Sounds.shot.play()
                x = self.ship.sprites()[0].rect.centerx
                y = self.ship.sprites()[0].rect.centery
                self.missile.add(Missile(Images.missile, "missile",
                                      1, x, y-15))

    def launch_screen(self):
        f = pygame.font.Font("font/8bitOperatorPlus8-Bold.ttf", 50)
        msg = "PLAY SPACE INVADERS"
        text = f.render(msg, True, constants.WHITE)
        textRect = text.get_rect()
        textRect.center = (constants.SCREEN_WIDTH/2,
            constants.SCREEN_HEIGHT-200)
        picRect = Images.intro.get_rect()
        picRect.center = (constants.SCREEN_WIDTH/2,200)
        intro = True
        while intro:
            for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN:
                        if textRect.collidepoint(pygame.mouse.get_pos()):
                            intro = False
                    #if event.type == QUIT
            if textRect.collidepoint(pygame.mouse.get_pos()):
                text = f.render("PLAY SPACE INVADERS", True,
                                constants.GREEN)
            else:
                text = f.render(msg, True, constants.WHITE)
            self.screen.fill(constants.BLACK)
            self.screen.blit(Images.intro, picRect)
            self.screen.blit(text, textRect)
            pygame.display.flip()


    def play(self):
        frames = 0
        while self.numLives > 0:
            while self.gameLoop:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit(0)

                frames += 1
                if frames % 20 == 0:
                    self.updateAliens()
                    frames = 0
                self.processKeys()
                self.moveMissile()
                self.dropBombs()
                self.ship.update(0)
                self.bases.update()
                self.screen.fill(constants.BLACK)
                self.spSurface.fill(constants.BLACK)
                self.aliens.draw(self.screen)
                self.missile.draw(self.screen)
                self.bombs.draw(self.screen)
                self.ship.draw(self.screen)
                self.bases.draw(self.screen)
                pygame.display.flip()
            pygame.time.delay(1000)
            # create and initialize the user's ship
            self.ship.add(Ship(Images.ship, "hero", 1,
                           constants.SCREEN_WIDTH/2,
                           constants.SCREEN_HEIGHT-100))
            self.numLives -= 1
            self.gameLoop = True
        print("game over")


if __name__ == '__main__':
    app = SpaceInvaders()
    app.launch_screen()
    app.play()