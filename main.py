# import pygame library
import pygame
pygame.init()

# define colors used
WHITE = (255, 255, 255)
DARKBLUE = (36, 90, 190)
LIGHTBLUE = (0, 176, 240)
RED = (255, 0, 0)
ORANGE = (255, 100, 0)
YELLOW = (255, 255, 0)

# set variables
score = 0
lives = 3 

# define a game window
size(800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Brick Breaker')

# run bool game will run until quit
run = True

# clock is sed to determine the frame rate
clock = pygame.time.Clock()

# main program loop
while run:
    # main event loop
    for event in pygame.event.get(): # user did something
        if event.type == pygame.QUIT: # if user closes window
            run = False # exits loop

    # game logic

    # drawing code
    # first clear screen
    screen.fill(DARKBLUE)
    pygame.draw.line(screen, WHITE, [0, 38], [800, 38], 2)

    # display score and number of lives at top of screen
    font = pygame.font.Font(None, 34)
    text = font.render('Score: ' + str(score), 1, WHITE)
    screen.blit(text, (20, 10))
    text = font.render('Lives: ' +str(lives), 1, WHITE)
    screen.blit(text, (650, 10))

    # update screen
    pygame.display.flip()

    # limit to 60 fps
    clock.tick(60)

# after exiting the loop quit the game
pygame.quit()
    