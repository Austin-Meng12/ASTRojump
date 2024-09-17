from box import Box
from text import Text
from window import Window
import pygame
from image_sprite import ImageSprite
import random

from pygame import mixer
pygame.init()

class Engine:
    def __init__(self):
        self.__WINDOW = Window("Astrojump")
        # Start Screen
        self.__STARTSCREEN = True

        # Cutscene
        self.__CUTSCENE = False
        self.__FIRST_RUN = True
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
        #BG
        self.__BG = False
        self.__FLARE_POS = True
        self.__LIFE_VALUE = 3
        self.__LIFE_LOST = False
        self.__LIFE = Text(f"LIVES: {self.__LIFE_VALUE}")
        self.__LIFE.setPos((self.__WINDOW.getWidth(), self.__WINDOW.getHeight()))
        self.__SCORE_VALUE = 0
        self.__SCORE = Text(f"LIVES: {self.__SCORE_VALUE}")
        self.__SCORE.setPos((self.__WINDOW.getWidth(), self.__WINDOW.getHeight()))
        #Platforms
        self.__PLATFORMS = [

            ImageSprite("Images/Unbreakable Platform.png"),

            ImageSprite("Images/Unbreakable Platform.png"),

            ImageSprite("Images/Unbreakable Platform.png"),

            ImageSprite("Images/Unbreakable Platform.png"),

            ImageSprite("Images/Unbreakable Platform.png"),

            ImageSprite("Images/Unbreakable Platform.png"),

            ImageSprite("Images/Unbreakable Platform.png"),

            ImageSprite("Images/Bounce Pad Platform.png"),

            ImageSprite("Images/Breakable Platform.png"),

            ImageSprite("Images/Breakable Platform.png"),

            ImageSprite("Images/Unbreakable Platform.png"),

            ImageSprite("Images/Unbreakable Platform.png")

        ]
        for platform in self.__PLATFORMS:
            platform.setScale(4)
            platform.setPos((self.__WINDOW.getWidth(), self.__WINDOW.getHeight()))

        self.__PLATFORM_SET = True




    def wait(self):
        pygame.time.delay(1000)

    def getTime(self):
        return pygame.time.get_ticks()

    def specialPlatforms(self):

        if self.__ASTRONAUT.determineSpriteDirection1(self.__PLATFORMS[7].getPos(), self.__PLATFORMS[7].getDim()):
            self.__ASTRONAUT.DOUBLEJUMP = True


        if self.__LIFE_LOST == True:
            self.__LIFE_VALUE -= 1
            self.__LIFE_LOST = False
            self.__LIFE = Text(f"LIVES: {self.__LIFE_VALUE}")
            self.__LIFE.setPos((5, 0))
            self.__ASTRONAUT.setPos((self.__WINDOW.getWidth()//2, -300))



    def run(self):
        SPEED = 1
        START = pygame.time.get_ticks()
        STARTLIST = []

        if self.__FIRST_RUN == True:
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
            self.__FIRST_RUN = False


        while True:
            # INPUTS
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            PRESSED_KEYS = pygame.key.get_pressed()
            SPEED += 0.005

            if self.__STARTSCREEN == True:
                self.__START_SCREEN()
            if PRESSED_KEYS[pygame.K_u]:
                self.__STARTSCREEN = False
                self.__CUTSCENE = True
            #PROCESSING
            if self.__STARTSCREEN == False:
            # cutscene

                if self.__CUTSCENE == True:
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
                    self.__FRAGMENTS[3].scrollX(self.__WINDOW.getWidth(), -10000000, -1)

                    self.__ASTRONAUT.scrollY(1000000, -10000000, -1)
                    if self.__ASTRONAUT.getY() < -250:
                        print(self.__ASTRONAUT.getPos())
                        self.wait()
                        self.__CUTSCENE = False
                        self.__BG = True



                # Background
                if self.__BG == True:
                    #mixer.init()
                    #mixer.music.load('')
                    if self.__FLARE_POS == True:
                        self.__FLARE1.setPos((-50, self.__WINDOW.getHeight() + 10 - self.__FLARE1.getHeight()))
                        self.__FLARE_POS = False
                    self.__FLARE1.shake(-5, -60)
                    for star in self.__STARS:
                        star.setSpeed(SPEED)
                        star.wrapBox(self.__WINDOW.getWidth(), self.__WINDOW.getHeight())
                        star.scrollY(self.__WINDOW.getHeight())

                    self.__LIFE = Text(f"LIVES: {round(self.__LIFE_VALUE, 0)}")
                    self.__LIFE.setPos((5, 0))
                    self.__SCORE_VALUE += 1
                    self.__SCORE = Text(f"SCORE: {self.__SCORE_VALUE}")
                    self.__SCORE.setPos((self.__WINDOW.getWidth() - self.__SCORE.getWidth() - 5 , 0))

                # Gameplay Starts
                    if PRESSED_KEYS[pygame.K_SPACE] == True and self.__ASTRONAUT.ONPLATFORM == True and self.__ASTRONAUT.DOUBLEJUMP == False:
                        self.__ASTRONAUT.ONPLATFORM = False
                        self.__ASTRONAUT.JUMPING = True
                        self.__ASTRONAUT.FALLING = False
                        self.__ASTRONAUT.HEIGHT = self.__ASTRONAUT.getY()

                        self.__ASTRONAUT.setJumpHeight(150)
                    elif PRESSED_KEYS[pygame.K_SPACE] == True and self.__ASTRONAUT.ONPLATFORM == True and self.__ASTRONAUT.DOUBLEJUMP == True:
                        self.__ASTRONAUT.ONPLATFORM = False
                        self.__ASTRONAUT.JUMPING = True
                        self.__ASTRONAUT.FALLING = False
                        self.__ASTRONAUT.HEIGHT = self.__ASTRONAUT.getY()
                        self.__ASTRONAUT.setJumpHeight(250)

                    self.specialPlatforms()


                    if self.__ASTRONAUT.DOUBLEJUMP == True:
                        START = self.getTime()
                        STARTLIST.append(START)
                        END = STARTLIST[0] + 4000
                        if START < END:
                            print(START)
                        elif START > END:
                            self.__ASTRONAUT.DOUBLEJUMP = False
                            for i in range(len(STARTLIST)-1, -1, -1):
                                STARTLIST.pop(i)

                    self.__ASTRONAUT.setSpeed(10)
                    self.__ASTRONAUT.setGravity(3)

                    self.__ASTRONAUT.checkBoundaries(self.__WINDOW.getWidth() - 10, self.__WINDOW.getHeight())
                    self.__ASTRONAUT.moveAD(PRESSED_KEYS)
                    self.__ASTRONAUT.Jump()
                    self.__ASTRONAUT.Falling()
                    if self.__ASTRONAUT.getY() > self.__WINDOW.getHeight():
                        self.__LIFE_LOST = True
                    for platform in self.__PLATFORMS:
                        if self.__ASTRONAUT.isSpriteColliding(platform.getPos(), platform.getDim()):
                            self.__ASTRONAUT.determineSpriteDirection(platform.getPos(), platform.getDim())

                    #platforms
                    if self.__PLATFORM_SET == True:
                        self.__PLATFORMS[11].setPos(
                            (
                                random.randrange(self.__WINDOW.getWidth() - self.__PLATFORMS[11].getWidth()),
                                self.__WINDOW.getHeight() - 1200
                            )
                        )

                        self.__PLATFORMS[10].setPos(
                            (
                                random.randrange(self.__WINDOW.getWidth() - self.__PLATFORMS[10].getWidth()),
                                self.__WINDOW.getHeight() - 1100
                            )
                        )

                        self.__PLATFORMS[0].setPos(
                            (
                                random.randrange(self.__WINDOW.getWidth() - self.__PLATFORMS[0].getWidth()),
                                self.__WINDOW.getHeight() - 1000
                            )
                        )

                        self.__PLATFORMS[1].setPos(
                            (
                                random.randrange(self.__WINDOW.getWidth() - self.__PLATFORMS[1].getWidth()),
                                self.__WINDOW.getHeight() - 900
                            )
                        )

                        self.__PLATFORMS[2].setPos(
                            (
                                random.randrange(self.__WINDOW.getWidth() - self.__PLATFORMS[2].getWidth()),
                                self.__WINDOW.getHeight() - 800
                            )
                        )

                        self.__PLATFORMS[3].setPos(
                            (
                                random.randrange(self.__WINDOW.getWidth() - self.__PLATFORMS[3].getWidth()),
                                self.__WINDOW.getHeight() - 700
                            )
                        )

                        self.__PLATFORMS[4].setPos(
                            (
                                random.randrange(self.__WINDOW.getWidth() - self.__PLATFORMS[4].getWidth()),
                                self.__WINDOW.getHeight() - 600
                            )
                        )

                        self.__PLATFORMS[5].setPos(
                            (
                                random.randrange(self.__WINDOW.getWidth() - self.__PLATFORMS[5].getWidth()),
                                self.__WINDOW.getHeight() - 500
                            )
                        )

                        self.__PLATFORMS[6].setPos(
                            (
                                random.randrange(self.__WINDOW.getWidth() - self.__PLATFORMS[6].getWidth()),
                                self.__WINDOW.getHeight() - 400
                            )
                        )

                        self.__PLATFORMS[7].setPos(
                            (
                                random.randrange(self.__WINDOW.getWidth() - self.__PLATFORMS[7].getWidth()),
                                self.__WINDOW.getHeight() - 300
                            )
                        )

                        self.__PLATFORMS[8].setPos(
                            (
                                random.randrange(self.__WINDOW.getWidth() - self.__PLATFORMS[8].getWidth()),
                                self.__WINDOW.getHeight() - 200
                            )
                        )

                        self.__PLATFORMS[9].setPos(
                            (
                                random.randrange(self.__WINDOW.getWidth() - self.__PLATFORMS[9].getWidth()),
                                self.__WINDOW.getHeight() - 100
                            )
                        )
                        self.__PLATFORM_SET = False
                    for platform in self.__PLATFORMS:
                        platform.scrollY(self.__WINDOW.getHeight())
                        platform.setSpeed(SPEED)
                        platform.checkPlatFormBound(self.__WINDOW.getWidth(), self.__WINDOW.getHeight())

                    if self.__LIFE_VALUE <= 0:
                        self.__LOSING_SCREEN()




                #OUTPUTS
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
                for platform in self.__PLATFORMS:
                    self.__WINDOW.getSurface().blit(platform.getSurface(), platform.getPos())
                self.__WINDOW.getSurface().blit(self.__ASTRONAUT.getSurface(), self.__ASTRONAUT.getPos())
                self.__WINDOW.getSurface().blit(self.__LIFE.getSurface(), self.__LIFE.getPos())
                self.__WINDOW.getSurface().blit(self.__SCORE.getSurface(), self.__SCORE.getPos())

                self.__WINDOW.updateFrame()

    def __LOSING_SCREEN(self):
        while True:
            ### inputs
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            self.__LOSING_TITLE = Text("UNLUCKY, YOU SUCK")
            self.__LOSING_TITLE.setColor((220,20,60))
            self.__LOSING_TITLE.setPos((self.__WINDOW.getWidth() // 2 - self.__LOSING_TITLE.getWidth() // 2,
                                        self.__WINDOW.getHeight() // 2 - self.__LOSING_TITLE.getHeight() // 2))

            self.__RECTANGLE = pygame.Rect(self.__WINDOW.getWidth()//3 - 60,self.__WINDOW.getHeight()//2 + 50,100,50)
            self.__PLAYAGAIN = pygame.draw.rect(self.__WINDOW.getSurface(),(255,64,64), self.__RECTANGLE)
            self.__PLAYAGAIN_TEXT = Text("Play Again")
            self.__PLAYAGAIN_TEXT.setPos((self.__PLAYAGAIN.x + 5, self.__PLAYAGAIN.y + 10))
            self.__PLAYAGAIN_TEXT.setFontSize(24)
            if pygame.mouse.get_pressed()[0] and self.__PLAYAGAIN.collidepoint(pygame.mouse.get_pos()):
                self.reset()



            self.__RECTANGLE_2 = pygame.Rect(self.__PLAYAGAIN.x + 190, self.__PLAYAGAIN.y , 100, 50)
            self.__QUIT = pygame.draw.rect(self.__WINDOW.getSurface(), (255,64,64), self.__RECTANGLE_2)
            self.__TEXT_QUIT = Text("Quit")
            self.__TEXT_QUIT.setPos((self.__QUIT.x + 30, self.__QUIT.y + 10))
            self.__TEXT_QUIT.setFontSize(24)
            self.__LOSING_BACKGROUND = ImageSprite("Images/DEAD.png")
            self.__LOSING_BACKGROUND.setScale(2.8)
            self.__LOSING_BACKGROUND.setPos((0,0))
            if pygame.mouse.get_pressed()[0] and self.__QUIT.collidepoint(pygame.mouse.get_pos()):
                pygame.quit()
                exit()

            self.__WINDOW.clearScreen()
            self.__WINDOW.getSurface().blit(self.__LOSING_BACKGROUND.getSurface(), self.__LOSING_BACKGROUND.getPos())
            self.__WINDOW.getSurface().blit(self.__LOSING_TITLE.getSurface(), self.__LOSING_TITLE.getPos())
            self.__QUIT = pygame.draw.rect(self.__WINDOW.getSurface(), (255,64,64), self.__RECTANGLE_2)
            self.__PLAYAGAIN = pygame.draw.rect(self.__WINDOW.getSurface(), (255, 64, 64), self.__RECTANGLE)
            self.__WINDOW.getSurface().blit(self.__TEXT_QUIT.getSurface(), self.__TEXT_QUIT.getPos())
            self.__WINDOW.getSurface().blit(self.__PLAYAGAIN_TEXT.getSurface(), self.__PLAYAGAIN_TEXT.getPos())
            self.__WINDOW.updateFrame()

    def __START_SCREEN(self):
        self.__START_TITLE = Text("Welcome to AstroJump")
        self.__START_TITLE.setPos((self.__WINDOW.getWidth() // 2 - self.__START_TITLE.getWidth() // 2 -40,
                                        self.__WINDOW.getHeight() // 2 - self.__START_TITLE.getHeight() // 2 -150))
        self.__START_TITLE.setColor((255,20,147))
        self.__START_TITLE.setFontSize(48)
        self.__START_BUTTON = Text("Press U to start")
        self.__START_BUTTON.setPos((self.__WINDOW.getWidth() // 2 - self.__START_BUTTON.getWidth() // 2 + 50,
                                        self.__WINDOW.getHeight() // 2 - self.__START_BUTTON.getHeight() // 2 - 60))
        self.__SHIP = ImageSprite("Images/ship.png")
        self.__SHIP.setPos((75,50))
        self.__SHIP.setScale(1)

        self.__ASTROID = ImageSprite("Images/astroid.png")
        self.__ASTROID.setPos((10,10))
        self.__ASTROID.setScale(0.3)
        self.__ASTROID.setFlipY()
        self.__ASTROID.setFlipX()
        self.__ROCK = ImageSprite("Images/rock.png")
        self.__ROCK.setPos((300,20))
        self.__ROCK.setScale(0.1)
        self.__START_BUTTON.setColor((255,255,255))
        self.__START_BUTTON.setFontSize(24)

        self.__BACKGROUND = ImageSprite("Images/startbackground.png")
        self.__BACKGROUND.setPos((0,0))
        self.__BACKGROUND.setScale(0.6)
        self.__WINDOW.clearScreen()
        self.__WINDOW.getSurface().blit(self.__BACKGROUND.getSurface(), self.__BACKGROUND.getPos())
        self.__WINDOW.getSurface().blit(self.__SHIP.getSurface(), self.__SHIP.getPos())
        self.__WINDOW.getSurface().blit(self.__START_TITLE.getSurface(), self.__START_TITLE.getPos())
        self.__WINDOW.getSurface().blit(self.__START_BUTTON.getSurface(), self.__START_BUTTON.getPos())
        self.__WINDOW.getSurface().blit(self.__ASTROID.getSurface(), self.__ASTROID.getPos())
        self.__WINDOW.getSurface().blit(self.__ROCK.getSurface(), self.__ROCK.getPos())

        self.__WINDOW.updateFrame()

    def reset(self):

       self.__init__()
       self.run()








if __name__ == "__main__":
    GAME = Engine()
    GAME.run()
