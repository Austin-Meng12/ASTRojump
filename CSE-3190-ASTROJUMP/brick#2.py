'''
Title: Brick
Author: Dominic Khorrami-Arani
Date-created: 2023-05-11
'''
import pygame
from image_sprite import ImageSprite
from box import Box
import random
from window import Window

class Brick(ImageSprite):
    def __init__(self):
        super().__init__(self)
        self.__WINDOW = Window("Platform Test")


    def wait(self):
        pygame.time.delay(1000)



if __name__ == "__main__":
    from window import Window
    pygame.init()

    #for i in range(self.__PLATFORM_NUMBER)

    WINDOW = Window("Platform Test")
    PLATFORM_ONE = ImageSprite("Images/Unbreakable Platform.png")

    PLATFORM_TWO = ImageSprite("Images/Unbreakable Platform.png")
    #PLATFORM_TWO.setFlipX()

    PLATFORM_THREE = ImageSprite("Images/Unbreakable Platform.png")

    PLATFORM_FOUR = ImageSprite("Images/Unbreakable Platform.png")

    PLATFORM_FIVE = ImageSprite("Images/Unbreakable Platform.png")

    PLATFORM_SIX = ImageSprite("Images/Unbreakable Platform.png")
    #PLATFORM_SIX.setFlipX()

    PLATFORM_SEVEN = ImageSprite("Images/Unbreakable Platform.png")
    #PLATFORM_SEVEN.setFlipX()

    PLATFORM_EIGHT = ImageSprite("Images/Bounce Pad Platform.png")

    PLATFORM_NINE = ImageSprite("Images/Breakable Platform.png")

    PLATFORM_TEN = ImageSprite("Images/Spike Platform.png")

    PLATFORM_ELEVEN = ImageSprite("Images/pngwing.com.png")
    PLATFORM_ELEVEN.setScale(10)

    # 7 unbreakable, 1 breakable, 1 bounce, 1 spike
    PLATFORMS = [PLATFORM_ONE, PLATFORM_TWO, PLATFORM_THREE, PLATFORM_FOUR, PLATFORM_FIVE, PLATFORM_SIX, PLATFORM_SEVEN, PLATFORM_EIGHT, PLATFORM_NINE, PLATFORM_TEN]
    for platform in PLATFORMS:
        platform.setPos((WINDOW.getWidth(), WINDOW.getHeight()))
        platform.setSpeed(0)





    SPEED = 1

    while True:
        # INPUTS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        PRESSED_KEYS = pygame.key.get_pressed()





        # PROCESSING
        for platform in PLATFORMS:
            SPEED += 0.0005
            platform.scrollY(WINDOW.getHeight())
            platform.setSpeed(SPEED)
            platform.wrapBox(WINDOW.getWidth(), WINDOW.getHeight())

            # OUTPUTS
        WINDOW.clearScreen()
        for platform in PLATFORMS:
            WINDOW.getSurface().blit(platform.getSurface(), platform.getPos())
        WINDOW.getSurface().blit(PLATFORM_ELEVEN.getSurface(), PLATFORM_ELEVEN.getPos())
        # WINDOW.getSurface().blit(BOTTOM_RECTANGLE.getSurface(), BOTTOM_RECTANGLE.getPos())
        WINDOW.updateFrame()



