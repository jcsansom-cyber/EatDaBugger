import pygame
import os
import random
pygame.init()

WIDTH, HEIGHT = 1000, 700
PLAYER_WIDTH, PLAYER_HEIGHT = 70, 40
LADYBUG_WIDTH, LADYBUG_HEIGHT = 120, 90
BAD_BUG_WIDTH, BAD_BUG_HEIGHT = 30, 20
MAX_BUG_TRAVEL = 20
CENTER = [500, 350]
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
GRAY = (50, 50, 50)
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

pygame.display.set_caption("Eat Da Bugger")

def draw_window(player, ladybugs, bad_bugs, bad_bugs_eaten, bad_bugs_dist):
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render('Eat all the little buggers to win! Don\'t eat the ladybugs!', True, (255, 255, 255))
    textRect = text.get_rect()

    WINDOW.fill(GRAY)
    WINDOW.blit(BG, (0, 0))
    WINDOW.blit(text, textRect)
    for lady in ladybugs:
        WINDOW.blit(BUG1_IMG, (lady.x, lady.y))
    for bug in bad_bugs:
        new_x = random.randint(-MAX_BUG_TRAVEL, MAX_BUG_TRAVEL) + bug.x
        new_y = random.randint(-MAX_BUG_TRAVEL, MAX_BUG_TRAVEL) + bug.y
        if new_x < (WIDTH - BAD_BUG_WIDTH) and new_x > (BAD_BUG_WIDTH): 
            bug.x = new_x
        if new_y < (HEIGHT - BAD_BUG_HEIGHT) and new_y > (BAD_BUG_HEIGHT):
            bug.y = new_y
    for baddie in bad_bugs:
        if not bad_bugs_eaten[bad_bugs.index(baddie)]:
            WINDOW.blit(bad_bugs_dist[bad_bugs.index(baddie)], (baddie.x, baddie.y))
    WINDOW.blit(PLAYER_IMG, (player.x, player.y))
    pygame.display.update()

def all_bugs_eaten(bad_bugs_eaten):
    completed = True
    for condition in bad_bugs_eaten:
        if not condition:
            completed = False
    return completed

def main():
    success = False;
    print("\nEat all the little buggers to win! Don't eat the ladybugs!")
    # pygame.Rect(x, y, width, height of object)
    player = pygame.Rect(CENTER[0] - (PLAYER_WIDTH/2), CENTER[1] - (PLAYER_HEIGHT/2), PLAYER_WIDTH, PLAYER_HEIGHT)
    bad_bugs = [
        pygame.Rect(random.randrange(int(BAD_BUG_WIDTH/2), WIDTH-BAD_BUG_WIDTH), 40, BAD_BUG_WIDTH, BAD_BUG_HEIGHT),
        pygame.Rect(random.randrange(int(BAD_BUG_WIDTH/2), WIDTH-BAD_BUG_WIDTH), 110, BAD_BUG_WIDTH, BAD_BUG_HEIGHT),
        pygame.Rect(random.randrange(int(BAD_BUG_WIDTH/2), WIDTH-BAD_BUG_WIDTH), 180, BAD_BUG_WIDTH, BAD_BUG_HEIGHT),
        pygame.Rect(random.randrange(int(BAD_BUG_WIDTH/2), WIDTH-BAD_BUG_WIDTH), 250, BAD_BUG_WIDTH, BAD_BUG_HEIGHT),
        pygame.Rect(random.randrange(int(BAD_BUG_WIDTH/2), WIDTH-BAD_BUG_WIDTH), 430, BAD_BUG_WIDTH, BAD_BUG_HEIGHT),
        pygame.Rect(random.randrange(int(BAD_BUG_WIDTH/2), WIDTH-BAD_BUG_WIDTH), 500, BAD_BUG_WIDTH, BAD_BUG_HEIGHT),
        pygame.Rect(random.randrange(int(BAD_BUG_WIDTH/2), WIDTH-BAD_BUG_WIDTH), 570, BAD_BUG_WIDTH, BAD_BUG_HEIGHT),
        pygame.Rect(random.randrange(int(BAD_BUG_WIDTH/2), WIDTH-BAD_BUG_WIDTH), 640, BAD_BUG_WIDTH, BAD_BUG_HEIGHT),
    ]
    bad_bugs_eaten = [False, False, False, False, False, False, False, False]
    bad_bugs_dist = [BUG2_IMG, BUG3_IMG, BUG2_IMG, BUG3_IMG, BUG2_IMG, BUG3_IMG, BUG2_IMG, BUG3_IMG]
    ladybugs = [
        pygame.Rect(random.randrange(0, WIDTH-LADYBUG_WIDTH), 100, LADYBUG_WIDTH, LADYBUG_HEIGHT),
        pygame.Rect(random.randrange(0, WIDTH-LADYBUG_WIDTH), 200, LADYBUG_WIDTH, LADYBUG_HEIGHT),
        pygame.Rect(random.randrange(0, WIDTH-LADYBUG_WIDTH), 420, LADYBUG_WIDTH, LADYBUG_HEIGHT),
        pygame.Rect(random.randrange(0, WIDTH-LADYBUG_WIDTH), 550, LADYBUG_WIDTH, LADYBUG_HEIGHT),
    ]
    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                print("\nGame quit")
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
                running = False
                success = False
                print("\nOh no! You tried to eat a ladybug! :(")
        if all_bugs_eaten(bad_bugs_eaten):
            running = False
            success = True
            print("\nCongrats! You ate all the little bugs! ( Now your code works beautifully ;) )")
        draw_window(player, ladybugs, bad_bugs, bad_bugs_eaten, bad_bugs_dist)
    pygame.quit()
    if success: print("\nYou won!")
    else: print("\nYou lost")

if __name__ == "__main__":
    main()

