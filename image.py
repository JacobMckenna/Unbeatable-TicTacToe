import pygame


X     = pygame.image.load("images/xMini.png")
O     = pygame.image.load("images/oMini.png")

EMPTY = pygame.image.load("images/emptyMini.png")
HOVER = pygame.image.load("images/hoverMini.png")

ICON  = pygame.image.load("images/icon.png")

BUTTON_IMAGE = [EMPTY,HOVER]

#mapping
IMAGE_KEY = {
    1:X,
    2:O
}
IMAGE_SIZE = 64