import pygame
pygame.init()

#Global Variables
WIDTH = 500
HEIGHT = 500

FPS = 20

RED = (255, 0, 0)
WHITE = (255,255,255)
x, y = WIDTH // 2 , HEIGHT // 2
step = 20
RAD = 25
#Initializing 
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("BALL")

clock = pygame.time.Clock()

finished = False
while not finished:
    clock.tick(FPS)
    # pygame.draw.circle(screen, BLACK, (WIDTH // 2, HEIGHT // 2), 25)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, (x, y), RAD)


    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP] and y - RAD  - 15  >= 0: 
           y -= step
    if pressed[pygame.K_DOWN] and y + RAD + 15 <= HEIGHT:
           y += step
    if pressed[pygame.K_LEFT] and x - RAD - 15 >= 0:
           x -= step
    if pressed[pygame.K_RIGHT] and x + RAD + 15 <= WIDTH:
           x += step
    
            
    pygame.display.flip()
pygame.quit()
