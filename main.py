# import pygame library
import pygame
# import our Paddle class
from paddle import Paddle
from ball import Ball
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
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Brick Breaker')

# This will be a list containing all our sprites
all_sprites_list = pygame.sprite.Group()

# create the paddle
paddle = Paddle(LIGHTBLUE, 100, 10)
paddle.rect.x = 350
paddle.rect.y = 560

# create the ball
ball = Ball(WHITE, 10, 10)
ball.rect.xx = 345
ball.rect.y = 195

# add the paddle to the list of sprites
all_sprites_list.add(paddle)
all_sprites_list.add(ball)

# run bool game will run until quit
run = True

# clock is sed to determine the frame rate
clock = pygame.time.Clock()

# main program loop
while run == True:
    # main event loop
    for event in pygame.event.get(): # user did something
        if event.type == pygame.QUIT: # if user closes window
            run = False # exits loop
        elif event.type==pygame.K_x: # pressing x quits game
            run = False

    # moving the when the user presses the arrow key
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        Paddle.moveLeft(5)
    if keys[pygame.K_RIGHT]:
        paddle.moveRight(5)

    # game logic
    all_sprites_list.update()

    # check if the ball is bouncing against any of the walls
    if ball.rect.x>= 790:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x<= 0:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y>590:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y<40:
        ball.velocity[1] = -ball.velocity[1]

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

    # now we draw all the sprites
    all_sprites_list.draw(screen)

    # update screen
    pygame.display.flip()

    # limit to 60 fps
    clock.tick(60)

# after exiting the loop quit the game
pygame.quit()
    