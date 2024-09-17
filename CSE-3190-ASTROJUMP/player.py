# Player.py in CSE-3190-atstrojump

"""
Title: PLayer class for astrojump
date-created: 2023-05-11
author: Austin Meng
"""
import pygame
import pygame.time
pygame.init()
from window import Window
from image_sprite import ImageSprite
from brick import Brick
import random
class Player(ImageSprite):

    def __init__(self):
        self.__WINDOW = Window("HELLO")
        ImageSprite.__init__(self, "Images/Front Astronaut.png")
        self.__SURFACE = pygame.Surface(self._DIM, pygame.SRCALPHA,32)
        self.setPos((self.__WINDOW.getWidth()//2, self.__WINDOW.getHeight()//2))

    def getTime(self):
        return pygame.time.get_ticks()






if __name__ == "__main__":
    WINDOW = Window("IDK")

    PLATFORM_ONE = ImageSprite("Images/pngwing.com.png")

    PLATFORM_TWO = ImageSprite("Images/pngwing.com.png")
    PLATFORM_TWO.setFlipX()

    PLATFORM_THREE = ImageSprite("Images/pngwing.com.png")

    PLATFORM_FOUR = ImageSprite("Images/pngwing.com.png")

    PLATFORM_FIVE = ImageSprite("Images/pngwing.com.png")

    PLATFORM_SIX = ImageSprite("Images/pngwing.com.png")
    PLATFORM_SIX.setFlipX()

    PLATFORM_SEVEN = ImageSprite("Images/pngwing.com.png")
    PLATFORM_SEVEN.setFlipX()

    PLATFORM_EIGHT = ImageSprite("Images/pngwing.com.png")

    PLATFORM_NINE = ImageSprite("Images/pngwing.com.png")

    PLATFORM_TEN = ImageSprite("Images/pngwing.com.png")

    PLATFORM_ELEVEN = ImageSprite("Images/pngwing.com.png")
    PLATFORM_ELEVEN.setScale(0.3)

    PLATFORMS = [PLATFORM_ONE]

    for platform in PLATFORMS:
        platform.setScale(
            random.uniform(0.15, 0.30))  # Let's the scale have a random value between the two float values
        platform.setPos(
            (
                random.randrange(WINDOW.getWidth() - platform.getWidth()),
                random.randrange(WINDOW.getHeight() - platform.getHeight())
            )
        )
        SPEED = 1
    PLATFORM_ELEVEN.setPos((WINDOW.getWidth() // 2 - PLATFORM_ELEVEN.getWidth(), WINDOW.getHeight() // 2))

    PLAYER = Player()
    PLAYER.setScale(0.25)


    START = pygame.time.get_ticks()
    STARTLIST = []

    while True:
        # INPUTS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        KEY_PRESSED = pygame.key.get_pressed()

        if KEY_PRESSED[pygame.K_SPACE] == True and PLAYER.ONPLATFORM == True and PLAYER.DOUBLEJUMP == False:
                PLAYER.ONPLATFORM = False
                PLAYER.JUMPING = True
                PLAYER.FALLING = False
                PLAYER.HEIGHT = PLAYER.getY()

                PLAYER.setJumpHeight(150)
        elif KEY_PRESSED[pygame.K_SPACE] == True and PLAYER.ONPLATFORM == True and PLAYER.DOUBLEJUMP == True:
            PLAYER.ONPLATFORM = False
            PLAYER.JUMPING = True
            PLAYER.FALLING = False
            PLAYER.HEIGHT = PLAYER.getY()
            PLAYER.setJumpHeight(300)


        if KEY_PRESSED[pygame.K_u] == True and PLAYER.DOUBLEJUMP == False:
            PLAYER.DOUBLEJUMP = True


        if PLAYER.DOUBLEJUMP == True:
            START = PLAYER.getTime()
            STARTLIST.append(START)
            END = STARTLIST[0] + 10000
            if START < END:
                print(START)
            elif START > END:
                PLAYER.DOUBLEJUMP = False









        PLAYER.setSpeed(10)
        PLAYER.setGravity(3)



        PLAYER.checkBoundaries(WINDOW.getWidth()- 10, WINDOW.getHeight())
        for platform in PLATFORMS:
            if PLAYER.isSpriteColliding(platform.getPos(), platform.getDim()):
                PLAYER.determineSpriteDirection(platform.getPos(), platform.getDim())




        PLAYER.moveAD(KEY_PRESSED)
        PLAYER.Jump()
        PLAYER.Falling()
        for platform in PLATFORMS:
            SPEED+= 0.0005
            platform.scrollY(WINDOW.getHeight())
            platform.setSpeed(SPEED)
            platform.wrapBox(WINDOW.getWidth(), WINDOW.getHeight())

        WINDOW.clearScreen()
        for platform in PLATFORMS:
            WINDOW.getSurface().blit(platform.getSurface(), platform.getPos())
        WINDOW.getSurface().blit(PLAYER.getSurface(), PLAYER.getPos())

        WINDOW.updateFrame()









