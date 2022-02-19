import pygame
import os

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60
player_img = pygame.image.load(os.path.join('Assets', ''))
pygame.display.set_caption("Pearl Shooter")



def draw_window():
    WIN.fill((0, 0, 0))
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