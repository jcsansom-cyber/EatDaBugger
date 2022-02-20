from tkinter import PhotoImage
import pygame
import os
import random

# Tutorial starts working on bullets at 52:54
# Link to tutorial: https://www.youtube.com/watch?v=jO6qQDNa2UY

WIDTH, HEIGHT = 1000, 700
PLAYER_WIDTH, PLAYER_HEIGHT = 70, 50
LADYBUG_WIDTH, LADYBUG_HEIGHT = 100, 70
BAD_BUG_WIDTH, BAD_BUG_HEIGHT = 30, 20
CENTER = [500, 350]
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60
VELOCITY = 5;
PLAYER_IMG = pygame.image.load(os.path.join('ufo.png'))
PLAYER_IMG = pygame.transform.scale(PLAYER_IMG, (PLAYER_WIDTH, PLAYER_HEIGHT))
# PLAYER_IMG = pygame.transform.rotate(PLAYER_IMG, 0)
BULLET_IMG = pygame.image.load(os.path.join('Shot.png'))
BUG1_IMG = pygame.image.load(os.path.join('Bug1.png'))
BUG1_IMG = pygame.transform.scale(BUG1_IMG, (LADYBUG_WIDTH, LADYBUG_HEIGHT))
BUG2_IMG = pygame.image.load(os.path.join('Bug2.png'))
BUG2_IMG = pygame.transform.scale(BUG2_IMG, (BAD_BUG_WIDTH, BAD_BUG_HEIGHT))
BUG3_IMG = pygame.image.load(os.path.join('Bug3.png'))
BUG3_IMG = pygame.transform.scale(BUG3_IMG, (BAD_BUG_WIDTH, BAD_BUG_HEIGHT))
BG = pygame.image.load("Shoocharu_botw_fanart_resized2.jpg")

PLAYER_HIT = pygame.USEREVENT + 1
pygame.display.set_caption("Eat Da Bugger")

def draw_window(player, ladybugs, bad_bugs, bad_bugs_eaten, bad_bugs_dist):
    WIN.fill((50, 50, 50))
    # WIN.fill(PhotoImage('photo-1465101162946-4377e57745c3.jpeg'))
    WIN.blit(BG, (0, 0))
    # WIN.blit(, (player.x, player.y))
    for lady in ladybugs:
        WIN.blit(BUG1_IMG, (lady.x, lady.y))
            
    for bug in bad_bugs:
        new_x = random.randint(-10,10) + bug.x
        new_y = random.randint(-10,10) + bug.y
        if new_x < (WIDTH - BAD_BUG_WIDTH) and new_x > (BAD_BUG_WIDTH): 
            bug.x = new_x
        # else:
        #     bug.x -= new_x
        if new_y < (HEIGHT - BAD_BUG_HEIGHT) and new_y > (BAD_BUG_HEIGHT):
            bug.y = new_y
        # else:
        #     bug.y -= new_y

    for baddie in bad_bugs:
        if not bad_bugs_eaten[bad_bugs.index(baddie)]:
            WIN.blit(bad_bugs_dist[bad_bugs.index(baddie)], (baddie.x, baddie.y))
    WIN.blit(PLAYER_IMG, (player.x, player.y))
    # WIN.blit("Points", (player.x, player.y))

    pygame.display.update()

def all_bugs_eaten(bad_bugs_eaten):
    completed = True
    for condition in bad_bugs_eaten:
        if not condition:
            completed = False
    return completed

def main():
    # pygame.Rect(x, y, width, height of object)
    player = pygame.Rect(CENTER[0] - (PLAYER_WIDTH/2), CENTER[1] - (PLAYER_HEIGHT/2), PLAYER_WIDTH, PLAYER_HEIGHT)
    bad_bugs = [
        pygame.Rect(random.randrange(int(BAD_BUG_WIDTH/2), WIDTH-int(BAD_BUG_WIDTH/2)), 90, BAD_BUG_WIDTH, BAD_BUG_HEIGHT),
        pygame.Rect(random.randrange(int(BAD_BUG_WIDTH/2), WIDTH-int(BAD_BUG_WIDTH/2)), 90, BAD_BUG_WIDTH, BAD_BUG_HEIGHT),
        pygame.Rect(random.randrange(int(BAD_BUG_WIDTH/2), WIDTH-int(BAD_BUG_WIDTH/2)), 160, BAD_BUG_WIDTH, BAD_BUG_HEIGHT),
        pygame.Rect(random.randrange(int(BAD_BUG_WIDTH/2), WIDTH-int(BAD_BUG_WIDTH/2)), 160, BAD_BUG_WIDTH, BAD_BUG_HEIGHT),
        pygame.Rect(random.randrange(int(BAD_BUG_WIDTH/2), WIDTH-int(BAD_BUG_WIDTH/2)), 300, BAD_BUG_WIDTH, BAD_BUG_HEIGHT),
        pygame.Rect(random.randrange(int(BAD_BUG_WIDTH/2), WIDTH-int(BAD_BUG_WIDTH/2)), 300, BAD_BUG_WIDTH, BAD_BUG_HEIGHT),
        pygame.Rect(random.randrange(int(BAD_BUG_WIDTH/2), WIDTH-int(BAD_BUG_WIDTH/2)), 370, BAD_BUG_WIDTH, BAD_BUG_HEIGHT),
        pygame.Rect(random.randrange(int(BAD_BUG_WIDTH/2), WIDTH-int(BAD_BUG_WIDTH/2)), 370, BAD_BUG_WIDTH, BAD_BUG_HEIGHT),
    ]
    bad_bugs_eaten = [False, False, False, False, False, False, False, False]
    bad_bugs_dist = [BUG2_IMG, BUG3_IMG, BUG2_IMG, BUG3_IMG, BUG2_IMG, BUG3_IMG, BUG2_IMG, BUG3_IMG]
    ladybugs = [
        pygame.Rect(random.randrange(int(LADYBUG_WIDTH/2), WIDTH-int(LADYBUG_WIDTH/2)), 100, LADYBUG_WIDTH, LADYBUG_HEIGHT),
        pygame.Rect(random.randrange(int(LADYBUG_WIDTH/2), WIDTH-int(LADYBUG_WIDTH/2)), 200, LADYBUG_WIDTH, LADYBUG_HEIGHT),
        pygame.Rect(random.randrange(int(LADYBUG_WIDTH/2), WIDTH-int(LADYBUG_WIDTH/2)), 500, LADYBUG_WIDTH, LADYBUG_HEIGHT),
        pygame.Rect(random.randrange(int(LADYBUG_WIDTH/2), WIDTH-int(LADYBUG_WIDTH/2)), 600, LADYBUG_WIDTH, LADYBUG_HEIGHT),
    ]
    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        keys_pressed = pygame.key.get_pressed() # checks what keys are currently being pressed
        if (keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_a]) and player.x - VELOCITY > 0:
            player.x -= VELOCITY;
        if (keys_pressed[pygame.K_RIGHT] or keys_pressed[pygame.K_d]) and player.x + VELOCITY + PLAYER_WIDTH < WIDTH:
            player.x += VELOCITY;
        if (keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_w]) and player.y - VELOCITY > 0:
            player.y -= VELOCITY;
        if (keys_pressed[pygame.K_DOWN] or keys_pressed[pygame.K_s]) and player.y + VELOCITY + PLAYER_HEIGHT < HEIGHT:
            player.y += VELOCITY;
        for bug in bad_bugs:
            if player.colliderect(bug):
                x = bad_bugs.index(bug)
                bad_bugs_eaten[x] = True
        for lady in ladybugs:
            if player.colliderect(lady):
                running = False;
        if all_bugs_eaten(bad_bugs_eaten):
            running = False;
        draw_window(player, ladybugs, bad_bugs, bad_bugs_eaten, bad_bugs_dist)
    pygame.quit()

if __name__ == "__main__":
    main()