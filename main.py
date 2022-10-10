import pygame
import sys

pygame.init()
HEIGHT = 500
WIGHT = 500
BLACK = (0, 0, 0)
screen = pygame.display.set_mode((HEIGHT, WIGHT))
pygame.display.set_caption('Kill the birds')
pygame.display.set_icon(pygame.image.load('images/icon_for_the_game.png'))
clock = pygame.time.Clock()

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill(BLACK)
    pygame.display.update()
