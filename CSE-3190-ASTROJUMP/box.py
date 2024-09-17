import pygame
from my_sprite import mySprite
from window import Window

class Box(mySprite):
    def __init__(self, WIDTH=1, HEIGHT=1):
        mySprite.__init__(self, WIDTH, HEIGHT)
        self._SURFACE = pygame.Surface(self._DIM, pygame.SRCALPHA, 32)
        self._SURFACE.fill(self._COLOR)

    def setColor(self, TUPLE):
        # polymorphs the setColor class from mySprite
        mySprite.setColor(self, TUPLE)
        self._SURFACE.fill(self._COLOR)

    def setScale(self, SCALE):
        pass



if __name__ == "__main__":
    pygame.init()
    WINDOW = Window("Box Text")
    BOX = Box(100, 100)
    BOX.setSpeed(10)
    BOX.setColor((0,0,255))
    BOX2 = Box(50, 50)
    BOX2.setPos((300, 300))


    while True:
        # INPUTS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        PRESSED_KEYS = pygame.key.get_pressed()


        # PROCESSING
        #BOX.marqueeX(WINDOW.getWidth())
        BOX.moveWASD(PRESSED_KEYS)
        if BOX.isSpriteColliding(BOX2.getPos(), BOX2.getDim()):
            print("Hit")
            BOX2.setColor((255,0,0))
        else:
            BOX2.setColor((255, 255, 255))


        # OUTPUTS
        WINDOW.clearScreen()
        WINDOW.getSurface().blit(BOX.getSurface(), BOX.getPos())
        WINDOW.getSurface().blit(BOX2.getSurface(), BOX2.getPos())
        WINDOW.updateFrame()