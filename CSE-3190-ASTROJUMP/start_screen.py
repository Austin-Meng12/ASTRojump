'''
Title:
Author: Dominic Khorrami-Arani
Date-created: 2023-06-04
'''
from window import Window
from text import Text
from box import Box
import random
import pygame

class StartScreen:
    def __init__(self):
        self.__WINDOW = Window("UI Test")
        self.__TITLE = Text('ASTROJUMP', 30)
        self.__PLAY_TEXT = Text('Play', 20)
        self.__QUIT_TEXT = Text('Quit', 20)
        self.__STARS = []
        #self.__UI_BG =

    def run(self):
        for i in range(300):
            STAR_SIZE = random.randrange(1, 6)
            self.__STARS.append(Box(STAR_SIZE, STAR_SIZE))
        for star in self.__STARS:
            star.setPos(
                (random.randint(0, self.__WINDOW.getWidth() - STAR_SIZE), random.randint(0, self.__WINDOW.getHeight() - STAR_SIZE)))

        self.__TITLE.setPos(
            (
                self.__WINDOW.getWidth()//2 - self.__TITLE.getWidth(),
                self.__WINDOW.getHeight()//2 - self.__TITLE.getHeight()
            )
        )

        while True:
            # INPUTS
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            self.__WINDOW.clearScreen()

            for star in self.__STARS:
                self.__WINDOW.getSurface().blit(star.getSurface(), star.getPos())
            self.__WINDOW.getSurface().blit(self.__TITLE.getSurface(), self.__TITLE.getPos())
            self.__WINDOW.getSurface().blit(self.__PLAY_TEXT.getSurface(), self.__PLAY_TEXT.getPos())
            self.__WINDOW.getSurface().blit(self.__QUIT_TEXT.getSurface(), self.__QUIT_TEXT.getPos())
            self.__WINDOW.updateFrame()

if __name__ == "__main__":
    pygame.init()
    START_SCREEN = StartScreen()
    START_SCREEN.run()