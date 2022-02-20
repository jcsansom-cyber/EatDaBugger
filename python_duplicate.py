import pygame
import os
import random

# Tutorial starts working on bullets at 52:54
# Link to tutorial: https://www.youtube.com/watch?v=jO6qQDNa2UY

points = 0
WIDTH, HEIGHT = 900, 500
PLAYER_WIDTH, PLAYER_HEIGHT = 70, 50
LADYBUG_WIDTH, LADYBUG_HEIGHT = 100, 70
BAD_BUG_WIDTH, BAD_BUG_HEIGHT = 30, 20
CENTER = [450, 250]
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

PLAYER_HIT = pygame.USEREVENT + 1
pygame.display.set_caption("Eat Da Bugger")

def draw_window(player, ladybugs, bad_bugs, bad_bugs_eaten, bad_bugs_dist):
    WIN.fill((50, 50, 50))
    # WIN.blit(, (player.x, player.y))
    for lady in ladybugs:
        WIN.blit(BUG1_IMG, (lady.x, lady.y))
    for z in bad_bugs:
            z.x+=random.randint(-5,5)
            z.y+=random.randint(-5,5)
    for baddie in bad_bugs:
        if not bad_bugs_eaten[bad_bugs.index(baddie)]:
            WIN.blit(bad_bugs_dist[bad_bugs.index(baddie)], (baddie.x, baddie.y))
    WIN.blit(PLAYER_IMG, (player.x, player.y))
    # WIN.blit("Points", (player.x, player.y))

    pygame.display.update()

# def gets_hit() {

# }


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
    for baddie in bad_bugs_dist:
        a = random.choice("12");
        if a == "2":
            baddie = BUG3_IMG;
    ladybugs = [
        pygame.Rect(random.randrange(int(LADYBUG_WIDTH/2), WIDTH-int(LADYBUG_WIDTH/2)), 90, LADYBUG_WIDTH, LADYBUG_HEIGHT),
        pygame.Rect(random.randrange(int(LADYBUG_WIDTH/2), WIDTH-int(LADYBUG_WIDTH/2)), 160, LADYBUG_WIDTH, LADYBUG_HEIGHT),
        pygame.Rect(random.randrange(int(LADYBUG_WIDTH/2), WIDTH-int(LADYBUG_WIDTH/2)), 300, LADYBUG_WIDTH, LADYBUG_HEIGHT),
        pygame.Rect(random.randrange(int(LADYBUG_WIDTH/2), WIDTH-int(LADYBUG_WIDTH/2)), 370, LADYBUG_WIDTH, LADYBUG_HEIGHT),
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
                # points+=1
        #running = False # Made false only to be made true again as long as there are still uneaten bugs
        #for condition in bad_bugs_eaten:
         #   if not condition:
          #      running = True;
        draw_window(player, ladybugs, bad_bugs, bad_bugs_eaten, bad_bugs_dist)
            
    pygame.quit()

if __name__ == "__main__":
    main()