import pygame
import os

WIDTH, HEIGHT = 900, 500
CENTER = (450, 250)
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60
PLAYER_IMG = pygame.image.load(os.path.join('Assets', 'UFo.png'))
PLAYER_IMG = pygame.transform.scale(PLAYER_IMG, (500, 500))
PLAYER_IMG = pygame.image.rotate(PLAYER_IMG, 0)
BULLET_IMG = pygame.image.load(os.path.join('Assets', 'UFo.png'))
BUG1_IMG = pygame.image.load(os.path.join('Assets', 'UFo.png'))
BUG2_IMG = pygame.image.load(os.path.join('Assets', 'UFo.png'))
BUG3_IMG = pygame.image.load(os.path.join('Assets', 'UFo.png'))
pygame.display.set_caption("Pearl Shooter")



def draw_window():
    WIN.fill((0, 0, 0))
    WIN.blit(PLAYER_IMG, CENTER)
    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    running = True;
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        draw_window()
            
    pygame.quit()

if __name__ == "__main__":
    main()