import pygame
from box import Box
from window import Window
from image_sprite import ImageSprite
import random
import time

class Cutscene:
    def __init__(self):
        self.__WINDOW = Window("Test")
        self.__STARS = []
        self.__FLARE1 = ImageSprite("Images/solar_flare-transformed.png")
        self.__FLARE2 = ImageSprite("Images/solar_flare-transformed.png")
        self.__FLARE2.setFlipY()
        self.__FLARE1.setScale(0.5)
        self.__FLARE1.setPos((-50, self.__WINDOW.getHeight() + 10 - self.__FLARE1.getHeight()))
        self.__FLARE2.setScale(0.5)
        self.__FLARE2.setPos((-50, self.__WINDOW.getHeight() + 290 - self.__FLARE2.getHeight()))
        self.__STATION = ImageSprite("Images/Space Station (2).png")
        self.__STATION.setScale(0.25)
        self.__STATION.setSpeed(5)
        self.__STATION.setPos((self.__WINDOW.getWidth(), 200))
        self.__EXPLOSION = ImageSprite("Images/Explosion.png")
        self.__EXPLOSION.setScale(0.25)
        self.__EXPLOSION.setPos((self.__WINDOW.getWidth(), self.__WINDOW.getHeight()))
        self.__EXPLOSION2 = ImageSprite("Images/Explosion.png")
        self.__EXPLOSION2.setScale(0.4)
        self.__EXPLOSION2.setPos((self.__WINDOW.getWidth(), self.__WINDOW.getHeight()))
        self.__FRAGMENTS = [
            ImageSprite("Images/Broken Fragment.png"),
            ImageSprite("Images/Broken Fragment.png"),
            ImageSprite("Images/Broken Fragment.png"),
            ImageSprite("Images/Broken Fragment.png")
        ]
        for fragment in self.__FRAGMENTS:
            fragment.setScale(0.75)
            fragment.setPos((self.__WINDOW.getWidth(), self.__WINDOW.getHeight()))
        self.__ASTRONAUT = ImageSprite("Images/Front Astronaut.png")
        self.__ASTRONAUT.setScale(0.25)
        self.__ASTRONAUT.setPos((self.__WINDOW.getWidth(), self.__WINDOW.getHeight()))
        self.__COLLISION = False

    def wait(self):
        pygame.time.delay(1000)


    def run(self):
        for i in range(300):
            STAR_SIZE = random.randrange(1, 6)
            self.__STARS.append(Box(STAR_SIZE, STAR_SIZE))

        for star in self.__STARS:
            star.setPos(
                (random.randint(0, self.__WINDOW.getWidth() - STAR_SIZE),
                 random.randint(0, self.__WINDOW.getHeight() - STAR_SIZE)))

        self.__FLARE1.setSpeed(5)
        self.__FLARE2.setSpeed(5)
        for fragment in self.__FRAGMENTS:
            fragment.setSpeed(5)
        self.__ASTRONAUT.setSpeed(4)
        SPEED = 1

        while True:
            # INPUTS
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            PRESSED_KEYS = pygame.key.get_pressed()
            SPEED += 0.0005

            self.__FLARE1.shake(-5, -60)
            self.__FLARE1.scrollY(self.__WINDOW.getHeight() // 2, -1000000, -1)
            self.__FLARE2.shake(-5, -60)
            self.__FLARE2.scrollY(self.__WINDOW.getHeight() // 2, -100000000, -1)

            if self.__COLLISION == False:
                for star in self.__STARS:
                    star.setSpeed(SPEED)
                    star.wrapBox(self.__WINDOW.getWidth(), self.__WINDOW.getHeight())
                    star.scrollY(self.__WINDOW.getHeight(), 0, 1)
                self.__STATION.scrollX(self.__WINDOW.getWidth(), -1, -1)

            if self.__FLARE2.isSpriteColliding(self.__STATION.getPos(), self.__STATION.getDim()):
                print(self.__FLARE2.getPos())
                self.__COLLISION = True
                self.__EXPLOSION.setPos(self.__STATION.getPos())
                self.__EXPLOSION2.setPos(self.__STATION.getPos())

            if self.__FLARE2.getPos() == (-50, 400):
                self.wait()

            if self.__FLARE2.getPos() == (-10, -100):
                self.wait()
                self.__STATION.setPos((self.__WINDOW.getWidth(), self.__WINDOW.getHeight()))
                for fragment in self.__FRAGMENTS:
                    fragment.setPos(self.__EXPLOSION.getPos())
                self.__ASTRONAUT.setPos(self.__EXPLOSION.getPos())
                self.wait()
                self.__EXPLOSION.setPos(self.__STATION.getPos())
                self.__EXPLOSION2.setPos(self.__STATION.getPos())

            self.__FRAGMENTS[0].scrollY(self.__WINDOW.getHeight())
            self.__FRAGMENTS[1].scrollY(1000000, -10000000, -1)
            self.__FRAGMENTS[2].scrollX(1000000000)
            self.__FRAGMENTS[3].scrollX(self.__WINDOW.getWidth(), -10000000,-1)

            self.__ASTRONAUT.scrollY(1000000, -10000000, -1)

            self.__WINDOW.clearScreen()

            for star in self.__STARS:
                self.__WINDOW.getSurface().blit(star.getSurface(), star.getPos())
            self.__WINDOW.getSurface().blit(self.__FLARE1.getSurface(), self.__FLARE1.getPos())
            self.__WINDOW.getSurface().blit(self.__FLARE2.getSurface(), self.__FLARE2.getPos())
            self.__WINDOW.getSurface().blit(self.__STATION.getSurface(), self.__STATION.getPos())
            for fragment in self.__FRAGMENTS:
                self.__WINDOW.getSurface().blit(fragment.getSurface(), fragment.getPos())
            self.__WINDOW.getSurface().blit(self.__EXPLOSION.getSurface(), self.__EXPLOSION.getPos())
            self.__WINDOW.getSurface().blit(self.__EXPLOSION2.getSurface(), self.__EXPLOSION2.getPos())
            self.__WINDOW.getSurface().blit(self.__ASTRONAUT.getSurface(), self.__ASTRONAUT.getPos())

            self.__WINDOW.updateFrame()

if __name__ == "__main__":
    CUTSCENE = Cutscene()
    CUTSCENE.run()
