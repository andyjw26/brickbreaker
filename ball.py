import pygame
from random import randint
BLACK = (0, 0, 0)

class Ball(pygame.sprite.Sprite):
    # This class represents the ball. It derives from the Sprite class in pygame.
   
   def __init__(self, color, width, height):
       # call the parent class (Sprite) constructor

       super().__init__()
       # pass the color, width and height of the ball.
       # set the background color as transparent.
       self.image = pygame.Surface([width, height])
       self.image.fill(BLACK)
       self.image.set_colorkey(BLACK)

       # draw the ball
       pygame.draw.rect(self.image, color, [0, 0, width, height])
       
       self.Velocity = [randint(4, 8), randint(-8, 8)]

       # fetch the rect object that has the dimensions of the image
       self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8, 8)