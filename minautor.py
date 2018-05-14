import pygame

class Minautor:
    """ Minautor will be the "destination" point of the genomes/Theseus """
    def __init__(self, screen, settings):
        """ Initialize the Minautor's parameters """
        self.screen     = screen
        self.settings   = settings
        
        self.color  = [0, 0, 255]
        self.radius = 20
        self.stroke = 2

        self.x      = settings.screen_width // 2
        self.y      = self.radius + 10

    def get_pos(self):
        """ Returns the position as a tuple """
        return (self.x, self.y)

    def update(self):
        pygame.draw.circle(self.screen, self.color, self.get_pos(), self.radius, self.stroke)
