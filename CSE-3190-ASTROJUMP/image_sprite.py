# image_sprite.py

import pygame
from my_sprite import mySprite

class ImageSprite(mySprite):
    """
    Load and manipulate images
    """
    def __init__(self, IMAGE_FILE):
        mySprite.__init__(self)
        self.__FILE_LOC = IMAGE_FILE
        self._SURFACE = pygame.image.load(self.__FILE_LOC).convert_alpha()
        self.__X_FLIP = False
    # MODIFIER

    def moveWASD(self, KEYS_PRESSED):
        mySprite.moveWASD(self, KEYS_PRESSED)
        if KEYS_PRESSED[pygame.K_d]:
            if not self.__X_FLIP:
                self.setFlipX()
                self.__X_FLIP = True
        if KEYS_PRESSED[pygame.K_a]:
            if self.__X_FLIP:
                self.setFlipX()
                self.__X_FLIP = False


    def setScale(self, SCALE_X, SCALE_Y=0):
        """
        Resize the image based on a factor
        :param SCALE_X: float
        :param SCALE_Y: float
        :return: none
        """
        if SCALE_Y == 0:
            SCALE_Y = SCALE_X
        self._SURFACE = pygame.transform.scale(self._SURFACE, (self.getWidth()*SCALE_X, self.getHeight()*SCALE_Y))

    def setFlipX(self):
        """
        flip image on y axis
        :return:
        """
        self._SURFACE = pygame.transform.flip(self._SURFACE, True, False)

    def setFlipY(self):
        """
        flip image on y axis
        :return:
        """
        self._SURFACE = pygame.transform.flip(self._SURFACE, False, True)





if __name__ == "__main__":
    from window import Window
    pygame.init()

    WINDOW = Window("Test")
    BUNNY = ImageSprite("images/bunny.png")
    BUNNY.setScale(0.5)
    BUNNY.setSpeed(10)
    BUNNY.setFlipX()

    while True:
        # INPUTS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        PRESSED_KEYS = pygame.key.get_pressed()

        # PROCESSING
        BUNNY.moveWASD(PRESSED_KEYS)

        # OUTPUTS
        WINDOW.clearScreen()
        WINDOW.getSurface().blit(BUNNY.getSurface(), BUNNY.getPos())
        WINDOW.updateFrame()