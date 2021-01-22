import pygame
BLACK = (0, 0, 0)

class Brick(pygame.sprite.Sprite):
    # this class represents a brick and is derived from the sprite class.

    def __init__(self, color, width, height):
        # call the parent class (Sprite) constructor
        super().__init__()

        # pass in the color of the brick , it's x and y position, width and height 
        # set the background color to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        # draw a brick
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        # fetch the rect obj that has the dimensions of the image
        self.rect = self.image.get_rect()