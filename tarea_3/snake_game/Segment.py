import pygame
from snake_game import constants as c


class Segment(pygame.sprite.Sprite):

    """ Class to represent one segment of the snake. """
    # -- Methods
    # Constructor function
    def __init__(self, x, y):
        # Call the parent's constructor
        super().__init__()
        self.x = x
        self.y = y
        # Set height, width
        self.image = pygame.Surface([c.SEGMENT_SIZE, c.SEGMENT_SIZE])
        self.image.fill(c.WHITE)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x*(c.SEGMENT_SIZE+c.SEGMENT_MARGIN*2)+c.SEGMENT_MARGIN
        self.rect.y = y*(c.SEGMENT_SIZE+c.SEGMENT_MARGIN*2)+c.SEGMENT_MARGIN