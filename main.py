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
FPS = 60


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('images/player_start.png')
        self.rect = self.image.get_rect()
        self.rect.x = 220
        self.rect.y = 400

    def movement_to_the_right(self):
        self.image = pygame.image.load('images/player_mov_R.png')

    def moving_to_the_left(self):
        self.image = pygame.image.load('images/player_mov_L.png')

    def shoot(self):
        self.image = pygame.image.load('Images/player.png')
        bullet = Bullet(self.rect.x, self.rect.y)
        all_sprites.add(bullet)
        bullets.add(bullet)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('images/bullet.png')
        self.image = pygame.transform.scale(self.image, (13, 20))
        self.rect = self.image.get_rect()
        self.rect.x = x + 26
        self.rect.y = y - 8
        self.speed = 5

    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()


player = Player()
all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()
all_sprites.add(player)

while True:
    clock.tick(FPS)
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()

    key = pygame.key.get_pressed()
    if key[pygame.K_d] and player.rect.x + 100 < WIGHT:
        player.movement_to_the_right()
        player.rect.x += 10
    elif key[pygame.K_a] and player.rect.x > 0:
        player.moving_to_the_left()
        player.rect.x -= 10

    all_sprites.update()
    all_sprites.draw(screen)
    pygame.display.update()
