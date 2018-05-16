import pygame
from random import choice
from actor import Actor

class Theseus(Actor):
    """ Since Theseus killed the Minautor in its maze, the Genomes will be known as Theuseus """
    def __init__(self, screen, settings):
        super().__init__(screen, settings, (settings.screen_width // 2, settings.screen_height // 2))
        self.screen     = screen
        self.settings   = settings
        self.is_dead     = False
        self.has_reached = False

    def move(self):
        """ Updates Theseus' coordinates """
        dir_x = choice([-1, 0, 1])
        dir_y = choice([-1, 0, 1])
        dx = choice(range(5, 10)) # Horizontal Velocity 
        dy = choice(range(5, 10)) # Vertical Velocity 
        self.x += dx * dir_x
        self.y += dy * dir_y
        self.rect.x = self.x 
        self.rect.y = self.y

    def kill(self):
        """ Marks this instance as Dead"""
        self.is_dead = True
        self.image = pygame.image.load("assets/dead.bmp")

    def reach_target(self):
        """ Marks this instance as successful """
        self.has_reached = True
        self.image = pygame.image.load("assets/reached.bmp")

    def update(self):
        if self.is_dead == False and self.has_reached == False:
            self.move()
        super().display()