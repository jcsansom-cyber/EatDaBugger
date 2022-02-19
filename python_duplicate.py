import pygame
import os

WIDTH, HEIGHT = 900, 500
CENTER = (450, 250)
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60
VELOCITY = 7;
PLAYER_IMG = pygame.image.load(os.path.join('Assets', 'UFo.png'))
PLAYER_IMG = pygame.transform.scale(PLAYER_IMG, (200, 200))
PLAYER_IMG = pygame.transform.rotate(PLAYER_IMG, 0)
BULLET_IMG = pygame.image.load(os.path.join('Assets', 'UFo.png'))
BUG1_IMG = pygame.image.load(os.path.join('Assets', 'UFo.png'))
BUG2_IMG = pygame.image.load(os.path.join('Assets', 'UFo.png'))
BUG3_IMG = pygame.image.load(os.path.join('Assets', 'UFo.png'))
pygame.display.set_caption("Pearl Shooter")



def draw_window(player):
    WIN.fill((0, 0, 0))
    WIN.blit(PLAYER_IMG, (player.x, player.y))
    pygame.display.update()


def main():
    player = pygame.Rect(CENTER[0], CENTER[1], 500, 500)

    clock = pygame.time.Clock()
    running = True;
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # player.x += 1
        keys_pressed = pygame.key.get_pressed() # checks what keys are currently being pressed
        if keys_pressed[pygame.K_LEFT] and player.x - VELOCITY > 0:
            player.x -= VELOCITY;
        if keys_pressed[pygame.K_RIGHT] and player.x + VELOCITY < WIDTH - 100:
            player.x += VELOCITY;
        if keys_pressed[pygame.K_UP] and player.y - VELOCITY > 0:
            player.y -= VELOCITY;
        if keys_pressed[pygame.K_DOWN] and player.y + VELOCITY < HEIGHT:
            player.y += VELOCITY;
        draw_window(player)
            
    pygame.quit()

if __name__ == "__main__":
    main()