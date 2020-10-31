import pygame
Black = (0, 0, 0)

class Paddle(pygame.sprite.Sprite):
    # This class represents a paddle and is derived from the Sprite class in pygame.

    def __init__(self, color, width, height):
        # call the parent class (Sprite) constructor
        super().__init__()

        # pass in the color of the paddle and its x and y position, width and height.
        # set the background color and make it transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        # draw the paddle
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        # fetch the rectangle object that has the dimensions of the image
        self.rect = self.image.get_rect()

    def moveLeft(self, pixels):
        self.rect.x -= pixels
        # check you are not moving of screen
        if self.rect.x < 0:
            self.rect.x = 0

    def moveRight(self, pixels):
        self.rect.x =+ pixels
        # check you are not moving off screen
        if self.rect.x > 700:
            self.rect.x =700
