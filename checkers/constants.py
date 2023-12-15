import pygame

WIDTH, HEIGHT = 1000, 1000
ROWS, COLS = 10, 10
SQUARE_SIZE = WIDTH//COLS

RED = (0, 0, 0)
LIGHT_BROWN = (255, 207, 127)
WHITE = (255, 255, 255)
BLACK = (51, 31, 0)
GREEN = (0, 255, 0)
GREY = (128, 128, 128)

CROWN = pygame.transform.scale(pygame.image.load('assets\\crown.png'), (60, 50))
