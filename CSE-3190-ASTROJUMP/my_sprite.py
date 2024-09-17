import random

import pygame
from window import Window

class mySprite:
    """
    Many of the common attributes and methods for sprites in pygame
    """
    def __init__(self, HEIGHT=0, WIDTH=0, X=0, Y=0, SPD=0, COLOR=(255, 255, 255)):
        self.__HEIGHT = HEIGHT
        self.__WIDTH = WIDTH
        self._DIM = (self.__WIDTH, self.__HEIGHT)
        self._SURFACE = pygame.Surface
        self.__X = X
        self.__Y = Y
        self.__POS = (self.__X, self.__Y)
        self.__SPD = SPD
        self._COLOR = COLOR
        self.__DIR_X = 1
        self.__DIR_Y = -1
        self.HEIGHT = 0



        #Player Jumping
        self.JUMPING = False
        self.FALLING = True
        self.ONPLATFORM = True
        self.__GRAVITY = 2
        self.__MAX_HEIGHT = 10
        self.DOUBLEJUMP = False



    # MODIFIER

    def Jump(self):


        if self.JUMPING == True:
            self.__Y -= self.__SPD
            self.__Y += self.__GRAVITY
            if self.__Y <= self.HEIGHT - self.__MAX_HEIGHT:
                print("A")
                self.JUMPING = False
                self.FALLING = True




        self.__POS = (self.__X, self.__Y)
    def Falling(self):
        if self.FALLING == True:
            self.__Y += self.__SPD
            self.__Y += self.__GRAVITY

    def getJump(self):
        return self.JUMPING

    def setJumpHeight(self, HEIGHT):

        self.__MAX_HEIGHT = HEIGHT
    def getJUMPHEIGHT(self):
        return self.__MAX_HEIGHT


    def setGravity(self, GRAVITY):
        self.__GRAVITY = GRAVITY


    def shake(self, MAX_WIDTH, MIN_WIDTH):
        self.__X += self.__SPD * self.__DIR_X
        if self.__X == MAX_WIDTH:
            self.__DIR_X = -1
        if self.__X == MIN_WIDTH:
            self.__DIR_X = 1
        self.__POS = (self.__X, self.__Y)

    def highJump(self):
        MAX_HEIGHT = 20
        self.__Y -= self.__SPD
        self.__Y += self.__GRAVITY
        if self.__Y < MAX_HEIGHT:
            self.JUMPING = False

    def marqueeX(self, MAX_WIDTH, MIN_WIDTH=0):
        self.__X += self.__SPD
        if self.__X > MAX_WIDTH:
            self.__X = MIN_WIDTH - self.getWidth()

        self.__POS = (self.__X, self.__Y)

    def moveWASD(self, KEYS_PRESSED):
        """
        Move sprite with WASD
        :param KEYS_PRESSED: list
        :return: None
        """
        if KEYS_PRESSED[pygame.K_d]:
            self.__X += self.__SPD
        if KEYS_PRESSED[pygame.K_a]:
            self.__X -= self.__SPD
        if KEYS_PRESSED[pygame.K_w]:
            self.__Y -= self.__SPD
        if KEYS_PRESSED[pygame.K_s]:
            self.__Y += self.__SPD

        self.__POS = (self.__X, self.__Y)

    def wrapBox(self, MAX_WIDTH, MAX_HEIGHT, MIN_WIDTH=0,MIN_HEIGHT=0):
        if self.__X > MAX_WIDTH:
            self.__X = MIN_WIDTH - self.getWidth()
        if self.__X < MIN_WIDTH - self.getWidth():
            self.__X = MAX_WIDTH
        if self.__Y > MAX_HEIGHT:
            self.__Y = MIN_HEIGHT - self.getHeight()
        if self.__Y < MIN_HEIGHT - self.getHeight():
            self.__Y = MAX_HEIGHT
        self.__POS = (self.__X, self.__Y)


    def scrollX(self, MAX_WIDTH, MIN_WIDTH = 0, DIR = 1):

        self.__X += self.__SPD * DIR
        if self.__X < MIN_WIDTH - self.getWidth():
            self.__X = MAX_WIDTH

        self.__POS = (self.__X, self.__Y)

    def scrollY(self, MAX_HEIGHT, MIN_HEIGHT = 0, DIR = 1):
        self.__Y += self.__SPD * DIR
        if self.__Y < MIN_HEIGHT - self.getHeight():
            self.__Y = MAX_HEIGHT

        self.__POS = (self.__X, self.__Y)

    def moveAD(self, KEYS_PRESSED):
        """
        Move sprite with WASD
        :param KEYS_PRESSED: list
        :return: None
        """
        if KEYS_PRESSED[pygame.K_d]:
            self.__X += self.__SPD
        if KEYS_PRESSED[pygame.K_a]:
            self.__X -= self.__SPD

        self.__POS = (self.__X, self.__Y)


    def move(self):
        self.__X += self.__SPD * self.__DIR_X
        self.__Y += self.__SPD * self.__DIR_Y

        self.__POS = (self.__X, self.__Y)

    def checkBoundaries(self, MAX_X, MAX_Y, MIN_X = 0, MIN_Y = 0):

        if self.__X > MAX_X - self.getWidth():
            self.__X = MAX_X - self.getWidth()
            self.__DIR_X = -1
        if self.__X < MIN_X:
            self.__X = MIN_X
            self.__DIR_X = 1
        if self.__Y < MIN_Y:
            self.__Y = MIN_Y
            self.__DIR_Y = 1
            self.FALLING = True


        self.__POS = (self.__X, self.__Y)


    def setWidth(self, WIDHT):
        self.__WIDTH = WIDHT
        self._DIM = (self.__WIDTH, self.__HEIGHT)

    def setHeight(self, HEIGHT):
        self.__HEIGHT = HEIGHT
        self._DIM = (self.__WIDTH, self.__HEIGHT)

    def setPos(self, TUPLE):
        self.__X = TUPLE[0]
        self.__Y = TUPLE[1]
        self.__POS = (self.__X, self.__Y)

    def setColor(self, TUPLE):
        self._COLOR = TUPLE

    def setSpeed(self, SPD):
        self.__SPD = SPD

    # ACCESSOR
    def getWidth(self):
        return self._SURFACE.get_width()

    def getHeight(self):
        return self._SURFACE.get_height()

    def getDim(self):
        return (self._SURFACE.get_width(), self._SURFACE.get_height())

    def getX(self):
        return self.__X
    def getY(self):
        return self.__Y

    def getPos(self):
        return self.__POS

    def getSurface(self):
        return self._SURFACE

    def setDirY(self):
        self.__DIR_Y = self.__DIR_Y * -1

    def setDirX(self):
        self.__DIR_X = self.__DIR_X * -1

    def isSpriteColliding(self, POS, DIM):
        """
        Check if a sprite is colliding with the current sprite
        :param POS: tuple
        :param DIM: tuple
        :return: bool
        """
        SPRITE_X = POS[0]
        SPRITE_Y = POS[1]
        SPRITE_W = DIM[0]
        SPRITE_H = DIM[1]
        if SPRITE_X >= self.__X - SPRITE_W and SPRITE_X <= self.__X + self.getWidth():
            if SPRITE_Y >= self.__Y - SPRITE_H and SPRITE_Y <= self.__Y + self.getHeight():
                return True

        return False

    def determineSpriteDirection(self, POS, DIM):
        SPRITE_X = POS[0] + 7
        SPRITE_Y = POS[1]
        SPRITE_W = DIM[0]
        SPRITE_H = DIM[1]

        if self.__Y + self.__HEIGHT <= SPRITE_Y  and self.FALLING == True and self.__X > SPRITE_X and self.__X  < SPRITE_X + SPRITE_W - 35:
            print("Hi")
            self.ONPLATFORM = True
            self.__Y  = SPRITE_Y - 15
            return True

    def determineSpriteDirection1(self, POS, DIM):
        SPRITE_X = POS[0] + 10
        SPRITE_Y = POS[1]
        SPRITE_W = DIM[0]
        SPRITE_H = DIM[1]

        if self.__Y + self.__HEIGHT <= SPRITE_Y  and self.FALLING == True and self.__X > SPRITE_X and self.__X  < SPRITE_X + SPRITE_W - 35:
            return True

    def checkPlatFormBound(self, MAX_X, MAX_Y, MIN_X = 0, MIN_Y=-50):
        if self.__X > MAX_X - self.getWidth():
            self.__X = MAX_X - self.getWidth()
        if self.__Y > MAX_Y:
            self.__Y = MIN_Y
            self.__X = random.randrange(MIN_X, MAX_X- self.__WIDTH )

        self.__POS = (self.__X, self.__Y)


