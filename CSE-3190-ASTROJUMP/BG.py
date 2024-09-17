import pygame
from box import Box
from window import Window
from image_sprite import ImageSprite
import random
import time

class Bg:
    def __init__(self):
        self.__WINDOW = Window("Test")
        self.__STARS = []
        self.__FLARE = ImageSprite("Images/solar_flare-transformed.png")
        self.__FLARE.setScale(0.5)
        self.__FLARE.setPos((-50, self.__WINDOW.getHeight() + 10 - self.__FLARE.getHeight()))

    def jump(self, KEY_PRESSED):
        TIME_END = time.time() + 10
        if KEY_PRESSED[pygame.K_SPACE]:
            for star in self.__STARS:
                star.scrollY(self.__WINDOW.getHeight())



    def run(self):
        for i in range(300):
            STAR_SIZE = random.randrange(1, 6)
            self.__STARS.append(Box(STAR_SIZE, STAR_SIZE))
        for star in self.__STARS:
            star.setPos(
                (random.randint(0, self.__WINDOW.getWidth() - STAR_SIZE), random.randint(0, self.__WINDOW.getHeight() - STAR_SIZE)))
        self.__FLARE.setSpeed(5)
        PLATFORM = Box(10, 75)
        SPEED = 1

        while True:
            # INPUTS
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            PRESSED_KEYS = pygame.key.get_pressed()
            SPEED += 0.0005

            for star in self.__STARS:
                star.setSpeed(SPEED)
                star.wrapBox(self.__WINDOW.getWidth(), self.__WINDOW.getHeight())
                star.scrollY(self.__WINDOW.getHeight())

            self.__FLARE.shake(-5, -60)
            #self.jump(PRESSED_KEYS)
            PLATFORM.setSpeed(SPEED)
            PLATFORM.scrollY(self.__WINDOW.getHeight())

            self.__WINDOW.clearScreen()

            for star in self.__STARS:
                self.__WINDOW.getSurface().blit(star.getSurface(), star.getPos())
            self.__WINDOW.getSurface().blit(self.__FLARE.getSurface(), self.__FLARE.getPos())
            self.__WINDOW.getSurface().blit(PLATFORM.getSurface(), PLATFORM.getPos())

            self.__WINDOW.updateFrame()

if __name__ == "__main__":
    BG = Bg()
    BG.run()
