import pygame
import sys
import random

# --- Setup ---
pygame.init()
WIDTH, HEIGHT = 480, 640
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font_big = pygame.font.SysFont(None, 60)
font_small = pygame.font.SysFont(None, 36)

WHITE = (255, 255, 255)
GREY = (100, 100, 100)
BLUE = (50, 150, 255)
FPS = 120

# --- Classes ---
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT - 60))
        self.speed = 5

    def update(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speed

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill((200, 0, 0))
        self.rect = self.image.get_rect(center=(random.randint(40, WIDTH - 40), -40))
        self.speed = random.randint(4, 8)

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            self.kill()

class Explosion(pygame.sprite.Sprite):
    def __init__(self, center):
        super().__init__()
        self.image = pygame.Surface((60, 60))
        self.image.fill((255, 255, 0))
        self.rect = self.image.get_rect(center=center)
        self.timer = pygame.time.get_ticks()

    def update(self):
        if pygame.time.get_ticks() - self.timer > 300:
            self.kill()

# --- Menu GUI Button ---
class Button:
    def __init__(self, text, y, callback):
        self.text = text
        self.rect = pygame.Rect(WIDTH//2 - 150, y, 300, 50)
        self.callback = callback

    def draw(self, surface, mouse_pos):
        color = BLUE if self.rect.collidepoint(mouse_pos) else GREY
        pygame.draw.rect(surface, color, self.rect, border_radius=10)
        text_surf = font_small.render(self.text, True, WHITE)
        surface.blit(text_surf, text_surf.get_rect(center=self.rect.center))

    def handle_event(self, event, mouse_pos):
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(mouse_pos):
            self.callback()

# --- Main Game ---
def run_game():
    def fade_in():
        fade_surface = pygame.Surface((WIDTH, HEIGHT))
        fade_surface.fill((0, 0, 0))
        for alpha in range(255, -1, -5):
            fade_surface.set_alpha(alpha)
            screen.fill((0, 0, 0))
            screen.blit(fade_surface, (0, 0))
            pygame.display.flip()
            pygame.time.delay(10)

    fade_in()

    player = Player()
    enemies = pygame.sprite.Group()
    explosions = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group(player)

    score = 0
    font_score = pygame.font.SysFont(None, 30)
    spawn_timer = pygame.time.get_ticks()

    running = True
    while running:
        clock.tick(FPS)
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if pygame.time.get_ticks() - spawn_timer > 800:
            enemy = Enemy()
            enemies.add(enemy)
            all_sprites.add(enemy)
            spawn_timer = pygame.time.get_ticks()

        player.update(keys)
        enemies.update()
        explosions.update()

        hits = pygame.sprite.spritecollide(player, enemies, True)
        for hit in hits:
            explosion = Explosion(hit.rect.center)
            explosions.add(explosion)
            all_sprites.add(explosion)
            score += 1

        screen.fill((0, 0, 0))
        all_sprites.draw(screen)

        score_surf = font_score.render(f"Score: {score}", True, WHITE)
        screen.blit(score_surf, (10, 10))

        pygame.display.flip()

# --- Main Menu ---
def main_menu():
    pygame.display.set_caption("Traffic Cut 2D - Menu")

    def start_game():
        run_game()

    def upgrades():
        print("Upgrades clicked")

    def options():
        print("Options clicked")

    def quit_game():
        pygame.quit()
        sys.exit()

    buttons = [
        Button("Start Game", 200, start_game),
        Button("Upgrades", 270, upgrades),
        Button("Options", 340, options),
        Button("Quit", 410, quit_game)
    ]

    while True:
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            for button in buttons:
                button.handle_event(event, mouse_pos)

        screen.fill((20, 20, 30))
        title = font_big.render("Hit Them All", True, WHITE)
        screen.blit(title, title.get_rect(center=(WIDTH//2, 100)))

        for button in buttons:
            button.draw(screen, mouse_pos)

        pygame.display.flip()
        clock.tick(FPS)

# --- Start the Menu ---
main_menu()
