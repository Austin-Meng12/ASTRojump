import pygame.time



pygame.init()
START = pygame.time.get_ticks()
END = START + 4000
while True:
    START = pygame.time.get_ticks()
    print(START)
    if START > END:
        exit()
