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
    pygame.init()

    WINDOW = Window("Platform Test")
    PLATFORM_ONE = ImageSprite("Images/Unbreakable Platform.png")

    PLATFORM_TWO = ImageSprite("Images/Unbreakable Platform.png")

    PLATFORM_THREE = ImageSprite("Images/Unbreakable Platform.png")

    PLATFORM_FOUR = ImageSprite("Images/Unbreakable Platform.png")

    PLATFORM_FIVE = ImageSprite("Images/Unbreakable Platform.png")

    PLATFORM_SIX = ImageSprite("Images/Unbreakable Platform.png")

    PLATFORM_SEVEN = ImageSprite("Images/Unbreakable Platform.png")

    PLATFORM_EIGHT = ImageSprite("Images/Bounce Pad Platform.png")

    PLATFORM_NINE = ImageSprite("Images/Breakable Platform.png")

    PLATFORM_TEN = ImageSprite("Images/Spike Platform.png")

    PLATFORM_ELEVEN = ImageSprite("Images/Unbreakable Platform.png")

    PLATFORM_TWELVE = ImageSprite("Images/Unbreakable Platform.png")

    # 7 unbreakable, 1 breakable, 1 bounce, 1 spike
    PLATFORMS = [PLATFORM_ONE, PLATFORM_TWO, PLATFORM_THREE, PLATFORM_FOUR, PLATFORM_FIVE, PLATFORM_SIX, PLATFORM_SEVEN, PLATFORM_EIGHT, PLATFORM_NINE, PLATFORM_TEN, PLATFORM_ELEVEN, PLATFORM_TWELVE]

    SPEED = 1
    for platform in PLATFORMS:
        platform.setScale(4)

    PLATFORMS[11].setPos(
        (
            random.randrange(WINDOW.getWidth() - PLATFORMS[10].getWidth()),
            WINDOW.getHeight() - 700
        )
    )

    PLATFORMS[10].setPos(
        (
            random.randrange(WINDOW.getWidth() - PLATFORMS[10].getWidth()),
            WINDOW.getHeight() - 650
        )
    )

    PLATFORMS[0].setPos(
        (
            random.randrange(WINDOW.getWidth() - PLATFORMS[0].getWidth()),
            WINDOW.getHeight() - 600
        )
    )

    PLATFORMS[1].setPos(
        (
            random.randrange(WINDOW.getWidth() - PLATFORMS[1].getWidth()),
            WINDOW.getHeight() - 550
        )
    )

    PLATFORMS[2].setPos(
        (
            random.randrange(WINDOW.getWidth() - PLATFORMS[2].getWidth()),
            WINDOW.getHeight() - 500
        )
    )

    PLATFORMS[3].setPos(
        (
            random.randrange(WINDOW.getWidth() - PLATFORMS[3].getWidth()),
            WINDOW.getHeight() - 450
        )
    )

    PLATFORMS[4].setPos(
        (
            random.randrange(WINDOW.getWidth() - PLATFORMS[4].getWidth()),
            WINDOW.getHeight() - 400
        )
    )

    PLATFORMS[5].setPos(
        (
            random.randrange(WINDOW.getWidth() - PLATFORMS[5].getWidth()),
            WINDOW.getHeight() - 350
        )
    )

    PLATFORMS[6].setPos(
        (
            random.randrange(WINDOW.getWidth() - PLATFORMS[6].getWidth()),
            WINDOW.getHeight() - 300
        )
    )

    PLATFORMS[7].setPos(
        (
            random.randrange(WINDOW.getWidth() - PLATFORMS[7].getWidth()),
            WINDOW.getHeight() - 250
        )
    )

    PLATFORMS[8].setPos(
        (
            random.randrange(WINDOW.getWidth() - PLATFORMS[8].getWidth()),
            WINDOW.getHeight() - 200
        )
    )

    PLATFORMS[9].setPos(
        (
            random.randrange(WINDOW.getWidth() - PLATFORMS[9].getWidth()),
            WINDOW.getHeight() - 150
        )
    )

    '''
    BOTTOM_RECTANGLE = Box(1, WINDOW.getWidth())
    BOTTOM_RECTANGLE.setColor((255, 255, 255))
    BOTTOM_RECTANGLE.setPos(
        (
            WINDOW.getWidth() - BOTTOM_RECTANGLE.getWidth(),
            WINDOW.getHeight() - BOTTOM_RECTANGLE.getHeight()
        )
    )
    '''



    for platform in PLATFORMS:
        pass
        '''
        if platform.checkPlatFormBound(WINDOW.getWidth(), WINDOW.getHeight()):
            platform.setPos(
                (
                    random.randrange(WINDOW.getWidth() - platform.getWidth()),
                    0
                )
            )
            
        '''


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
            #platform.wrapBox(WINDOW.getWidth(), WINDOW.getHeight())

            platform.checkPlatFormBound(WINDOW.getWidth(), WINDOW.getHeight())





            '''
            if platform.checkPlatFormBound(WINDOW.getWidth(), WINDOW.getHeight()):
                platform.setPos(
                    (
                        random.randrange(WINDOW.getWidth() - platform.getWidth()),
                        0
                    )
                )
            '''
            #platform.setPos((random.randrange(WINDOW.getWidth() - platform.getWidth()), 0))


        '''
        for platform in PLATFORMS:
            if platform.isSpriteColliding(platform.getPos(), platform.getDim()):
                platform.setPos(
                    (
                        random.randrange(WINDOW.getWidth() - platform.getWidth()),
                        random.randrange(WINDOW.getHeight() - platform.getHeight())
                    )
                )
        '''






        '''
        for i in range(1, 10):
            if PLATFORMS[0].isSpriteColliding(PLATFORMS[i].getPos(), PLATFORMS[i].getDim()):
                PLATFORMS[0].setPos(
                    (
                        random.randrange(WINDOW.getWidth() - PLATFORMS[0].getWidth()),
                        random.randrange(WINDOW.getHeight() - PLATFORMS[0].getHeight())
                    )
                )
                PLATFORMS[i].setPos(
                    (
                        random.randrange(WINDOW.getWidth() - PLATFORMS[i].getWidth()),
                        random.randrange(WINDOW.getHeight() - PLATFORMS[i].getHeight())
                    )
                )

        for i in range(2, 10):
            if PLATFORMS[1].isSpriteColliding(PLATFORMS[i].getPos(), PLATFORMS[i].getDim()):
                PLATFORMS[1].setPos(
                    (
                        random.randrange(WINDOW.getWidth() - PLATFORMS[1].getWidth()),
                        random.randrange(WINDOW.getHeight() - PLATFORMS[1].getHeight())
                    )
                )
                PLATFORMS[i].setPos(
                    (
                        random.randrange(WINDOW.getWidth() - PLATFORMS[i].getWidth()),
                        random.randrange(WINDOW.getHeight() - PLATFORMS[i].getHeight())
                    )
                )

        for i in range(3, 10):
            if PLATFORMS[2].isSpriteColliding(PLATFORMS[i].getPos(), PLATFORMS[i].getDim()):
                PLATFORMS[2].setPos(
                    (
                        random.randrange(WINDOW.getWidth() - PLATFORMS[2].getWidth()),
                        random.randrange(WINDOW.getHeight() - PLATFORMS[2].getHeight())
                    )
                )
                PLATFORMS[i].setPos(
                    (
                        random.randrange(WINDOW.getWidth() - PLATFORMS[i].getWidth()),
                        random.randrange(WINDOW.getHeight() - PLATFORMS[i].getHeight())
                    )
                )

        for i in range(4, 10):
            if PLATFORMS[3].isSpriteColliding(PLATFORMS[i].getPos(), PLATFORMS[i].getDim()):
                PLATFORMS[3].setPos(
                    (
                        random.randrange(WINDOW.getWidth() - PLATFORMS[3].getWidth()),
                        random.randrange(WINDOW.getHeight() - PLATFORMS[3].getHeight())
                    )
                )
                PLATFORMS[i].setPos(
                    (
                        random.randrange(WINDOW.getWidth() - PLATFORMS[i].getWidth()),
                        random.randrange(WINDOW.getHeight() - PLATFORMS[i].getHeight())
                    )
                )

        for i in range(len(PLATFORMS)):
            if PLATFORMS[0].getX() == PLATFORMS[i].getX():
                PLATFORMS[0].setPos(
                    (
                        random.randrange(WINDOW.getWidth() - PLATFORMS[0].getWidth()),
                        random.randrange(WINDOW.getHeight() - PLATFORMS[0].getHeight())
                    )
                )
                PLATFORMS[i].setPos(
                    (
                        random.randrange(WINDOW.getWidth() - PLATFORMS[i].getWidth()),
                        random.randrange(WINDOW.getHeight() - PLATFORMS[i].getHeight())
                    )
                )
          
        
    
        for i in range(len(PLATFORMS)):
            if PLATFORMS[i].getHeight() > WINDOW.getHeight():
                print(WINDOW.getHeight())
                PLATFORMS[i].setPos(
                    (
                        random.randrange(WINDOW.getWidth() - PLATFORMS[i].getWidth()),
                        random.randrange(WINDOW.getHeight() - PLATFORMS[i].getHeight())
                    )
                )
        '''















        # OUTPUTS
        WINDOW.clearScreen()
        for platform in PLATFORMS:
            WINDOW.getSurface().blit(platform.getSurface(), platform.getPos())
        #WINDOW.getSurface().blit(PLATFORM_ELEVEN.getSurface(), PLATFORM_ELEVEN.getPos())
        #WINDOW.getSurface().blit(BOTTOM_RECTANGLE.getSurface(), BOTTOM_RECTANGLE.getPos())
        WINDOW.updateFrame()


