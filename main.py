import pygame
import sys
import random
import pygame_menu

pygame.init()
HEIGHT = 550
WIGHT = 500
BLACK = (0, 0, 0)
GREEN = (0, 100, 0)
screen = pygame.display.set_mode((WIGHT, HEIGHT))
pygame.display.set_caption('Kill the birds')
pygame.display.set_icon(pygame.image.load('images/icon_for_the_game.png'))
clock = pygame.time.Clock()
FPS = 90
my_font = pygame.font.SysFont('Arial', 36)
font_bullet = pygame.font.SysFont('Arial', 20)
count = 0
count_bullets = 3
list_Bullet = []
SPACE = True


def start_the_game():
    global count_bullets
    global count
    global list_Bullet
    global SPACE

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

    images = ["images/bird_1.png", "images/bird_2.png"]

    class Duck(pygame.sprite.Sprite):

        def __init__(self, image):
            super().__init__()

            self.image = pygame.image.load(image)
            self.image = pygame.transform.scale(self.image, (50, 50))
            self.rect = self.image.get_rect()
            self.rect.y = random.randint(0, 200)
            self.rect.x = random.randint(-1000, -300)
            self.speed = random.randint(3, 5)

        def update(self):
            self.rect.x += self.speed
            if self.rect.x > 50:
                self.image = pygame.image.load(images[1])
                self.image = pygame.transform.scale(self.image, (50, 50))
            if self.rect.x > 200:
                self.image = pygame.image.load(images[0])
                self.image = pygame.transform.scale(self.image, (50, 50))
            if self.rect.x > 500:
                self.image = pygame.image.load(images[0])
                self.image = pygame.transform.scale(self.image, (50, 50))
                self.rect.y = random.randint(0, 300)
                self.rect.x = random.randint(-1000, -500)
                self.speed = random.randint(3, 5)

        @staticmethod
        def add():
            duck = Duck(images[0])
            all_sprites.add(duck)
            ducks.add(duck)

    class Recharge(pygame.sprite.Sprite):

        def __init__(self):
            super().__init__()
            self.image = pygame.Surface((10, 10))
            self.image.fill(GREEN)
            self.rect = self.image.get_rect()
            self.rect.x = 250
            self.rect.y = 300

        def update(self):
            text_3 = my_font.render('Recharge:', False, (0, 0, 0))

            if count_bullets == 2:
                self.rect.x += 2

                pygame.draw.rect(screen, BLACK, (250, 300, 110, 10))
                screen.blit(text_3, (240, 250))
                if self.rect.x > 350:
                    self.kill()
                    self.rect.x = 250
                    self.rect.y = 300
                    reloading_weapons()

            elif count_bullets < 2:
                self.rect.x += 1
                screen.blit(text_3, (240, 250))
                pygame.draw.rect(screen, BLACK, (250, 300, 110, 10))

                if self.rect.x > 350:
                    self.kill()
                    self.rect.x = 250
                    self.rect.y = 300
                    reloading_weapons()

    player = Player()
    all_sprites = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    all_sprites.add(player)
    ducks = pygame.sprite.Group()
    update_bullet = Recharge()

    for duck in range(3):
        Duck.add()

    def draw_bullet():
        bullet_fly = pygame.image.load('Images/bullet.png')
        bullet_fly = pygame.transform.scale(bullet_fly, (15, 20))
        bullet_afk = pygame.image.load('Images/bullet_afk.png')
        bullet_afk = pygame.transform.scale(bullet_afk, (15, 20))
        text_3 = font_bullet.render('Bullets: ', False, (255, 0, 0))
        pygame.draw.rect(screen, BLACK, (300, 500, 500, 300))
        screen.blit(text_3, (300, 505))
        if count_bullets == 3:
            screen.blit(bullet_fly, (390, 510))
            screen.blit(bullet_fly, (415, 510))
            screen.blit(bullet_fly, (440, 510))
        elif count_bullets == 2:
            screen.blit(bullet_afk, (390, 510))
            screen.blit(bullet_fly, (415, 510))
            screen.blit(bullet_fly, (440, 510))
        elif count_bullets == 1:
            screen.blit(bullet_afk, (390, 510))
            screen.blit(bullet_afk, (415, 510))
            screen.blit(bullet_fly, (440, 510))
        elif count_bullets == 0:
            screen.blit(bullet_afk, (390, 510))
            screen.blit(bullet_afk, (415, 510))
            screen.blit(bullet_afk, (440, 510))

    while True:
        clock.tick(FPS)
        text_1 = my_font.render(f'Count: {count}', False, (0, 0, 0))
        text_2 = my_font.render('Press R to recharge!', False, (0, 0, 0))
        screen.fill(BLACK)
        screen.blit(pygame.image.load('images/my_font.png'), (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and SPACE is True:
                    if len(list_Bullet) < 3:
                        count_bullets -= 1
                        player.shoot()
                        list_Bullet.append('1')

        if len(list_Bullet) == 3 and SPACE is True:
            screen.blit(text_2, (150, 300))

        key = pygame.key.get_pressed()
        if key[pygame.K_d] and player.rect.x + 100 < WIGHT:
            player.movement_to_the_right()
            player.rect.x += 10
        elif key[pygame.K_a] and player.rect.x > 0:
            player.moving_to_the_left()
            player.rect.x -= 10
        elif key[pygame.K_ESCAPE]:
            my_menu()
        if count_bullets < 3:
            if key[pygame.K_r]:
                all_sprites.add(update_bullet)
                SPACE = False

                def reloading_weapons():
                    global count_bullets
                    global SPACE
                    list_Bullet.clear()
                    count_bullets = 3
                    SPACE = True

        all_sprites.update()
        hits = pygame.sprite.groupcollide(bullets, ducks, True, True)
        for hit in hits:
            count += 1
            Duck.add()

        all_sprites.draw(screen)
        pygame.draw.rect(screen, GREEN, (0, 500, 500, 50))
        screen.blit(text_1, (0, 500))
        draw_bullet()

        pygame.display.update()


def my_menu():
    menu = pygame_menu.Menu('Welcome', 200, 200,
                            theme=pygame_menu.themes.THEME_DARK)

    menu.add.button('Play', start_the_game)
    menu.add.button('Quit', pygame_menu.events.EXIT)

    menu.mainloop(screen)


my_menu()
