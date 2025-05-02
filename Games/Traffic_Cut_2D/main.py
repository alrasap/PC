

import pygame
import sys
import random

pygame.init()
WIDTH, HEIGHT = 480, 640
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Traffic Cut 2D - Advanced Edition")
clock = pygame.time.Clock()

player_skin_default = pygame.image.load('assets/images/player.png')
player_skin_unlocked = pygame.image.load('assets/images/player2.png')
enemy_img = pygame.image.load('assets/images/enemy.png')
road_img = pygame.image.load('assets/images/road.png')
explosion_img = pygame.image.load('assets/images/explosion.png')

pygame.mixer.music.load('assets/music/20191229.mp3')
pygame.mixer.music.set_volume(0.5)

font_big = pygame.font.SysFont(None, 60)
font_small = pygame.font.SysFont(None, 36)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.skin_locked = True
        self.image = player_skin_default
        self.rect = self.image.get_rect(center=(WIDTH//2, HEIGHT - 100))
        self.speed = 5
        self.base_speed = 5
        self.boost_speed = 10
        self.turbo = 100
        self.turbo_active = False
        self.turbo_timer = 0

    def update(self, keys):
        if keys[pygame.K_UP] and self.turbo >= 100 and not self.turbo_active:
            self.turbo_active = True
            self.speed = self.boost_speed
            self.turbo_timer = pygame.time.get_ticks()

        if self.turbo_active:
            if pygame.time.get_ticks() - self.turbo_timer > 2000:
                self.turbo_active = False
                self.speed = self.base_speed
                self.turbo = 0

        if not self.turbo_active and self.turbo < 100:
            self.turbo += 0.5

        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speed

    def unlock_skin(self):
        self.image = player_skin_unlocked

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemy_img
        self.rect = self.image.get_rect(center=(random.randint(50, WIDTH - 50), -100))
        self.speed = random.randint(4, 7)

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            self.kill()

class Explosion(pygame.sprite.Sprite):
    def __init__(self, center):
        super().__init__()
        self.image = explosion_img
        self.rect = self.image.get_rect(center=center)
        self.start_time = pygame.time.get_ticks()

    def update(self):
        if pygame.time.get_ticks() - self.start_time > 500:
            self.kill()

class Game:
    def __init__(self):
        self.running = True
        self.playing = False
        self.all_sprites = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.explosions = pygame.sprite.Group()
        self.player = Player()
        self.score = 0
        self.spawn_delay = 1000
        self.last_spawn = pygame.time.get_ticks()
        self.bg_scroll = 0

    def new(self):
        self.all_sprites = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.explosions = pygame.sprite.Group()
        self.player = Player()
        self.all_sprites.add(self.player)
        self.score = 0
        pygame.mixer.music.play(-1)

    def run(self):
        while self.running:
            clock.tick(FPS)
            self.events()
            if self.playing:
                self.update()
            self.draw()

    def update(self):
        keys = pygame.key.get_pressed()
        self.player.update(keys)
        self.enemies.update()
        self.explosions.update()  # Only if you have an explosions group
        self.explosions.update()

        now = pygame.time.get_ticks()
        if now - self.last_spawn > self.spawn_delay:
            enemy = Enemy()
            self.all_sprites.add(enemy)
            self.enemies.add(enemy)
            self.last_spawn = now

        if pygame.sprite.spritecollide(self.player, self.enemies, False):
            explosion = Explosion(self.player.rect.center)
            self.explosions.add(explosion)
            self.all_sprites.add(explosion)
            self.playing = False
            pygame.mixer.music.stop()

        self.score = (pygame.time.get_ticks() // 1000)

        if self.score >= 30 and self.player.skin_locked:
            self.player.unlock_skin()
            self.player.skin_locked = False

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if not self.playing:
                    self.new()
                    self.playing = True

    def draw(self):
        self.bg_scroll += 5
        rel_y = self.bg_scroll % road_img.get_height()
        screen.blit(road_img, (0, rel_y - road_img.get_height()))
        if rel_y < HEIGHT:
            screen.blit(road_img, (0, rel_y))

        self.all_sprites.draw(screen)
        self.explosions.draw(screen)

        if not self.playing:
            self.show_menu()
        else:
            pygame.draw.rect(screen, WHITE, (10, 10, 100, 10), 2)
            pygame.draw.rect(screen, (0, 200, 255), (10, 10, self.player.turbo, 10))

        pygame.display.update()

    def show_menu(self):
        if self.score == 0:
            self.draw_text("Traffic Cut 2D", font_big, WHITE, WIDTH // 2, HEIGHT // 3)
            self.draw_text("Press any key to start", font_small, WHITE, WIDTH // 2, HEIGHT // 2)
        else:
            self.draw_text("Game Over", font_big, WHITE, WIDTH // 2, HEIGHT // 3)
            self.draw_text(f"Score: {self.score}", font_small, WHITE, WIDTH // 2, HEIGHT // 2)
            self.draw_text("Press any key to restart", font_small, WHITE, WIDTH // 2, HEIGHT // 1.5)

    def draw_text(self, text, font, color, x, y):
        img = font.render(text, True, color)
        rect = img.get_rect(center=(x, y))
        screen.blit(img, rect)

g = Game()
g.run()
