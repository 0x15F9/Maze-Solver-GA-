import pygame
from random import choice
from actor import Actor
from path import Path
#TODO: use collide and has reach in a game function
class Theseus(Actor):
    """ Since Theseus killed the Minautor in its maze, the Genomes will be known as Theuseus """
    def __init__(self, screen, settings):
        super().__init__(screen, settings, (settings.screen_width // 2, settings.screen_height // 2))
        self.screen     = screen
        self.settings   = settings

        self.is_dead     = False
        self.has_reached = False
        self.is_considered=True
        
        self.path = []
        self.steps = 0

    def get_coord(self):
        dir_x = choice([-1, 0, 1])
        dir_y = choice([-1, 0, 1])
        dx = choice(range(5, 10)) # Horizontal Velocity 
        dy = choice(range(5, 10)) # Vertical Velocity 
        return (dx * dir_x, dy * dir_y)

    def move(self, coord):
        """ Updates Theseus' coordinates """
        x_coord, y_coord = coord
        self.x += x_coord
        self.y += y_coord
        self.rect.x = self.x 
        self.rect.y = self.y
        self.steps += 1
        self.path.append((self.x, self.y))

    def retrace(self):
        return {'steps': self.steps, 'path': self.path}

    def set_path(self, path):
        self.path = Path

    def kill(self):
        """ Marks this instance as Dead"""
        self.is_dead = True
        self.is_considered = False
        self.image = pygame.image.load("assets/dead.bmp")

    def reach_target(self):
        """ Marks this instance as successful """
        self.has_reached = True
        self.is_considered = False
        self.image = pygame.image.load("assets/reached.bmp")

    def update(self):
        if self.is_considered:
            self.move(self.get_coord())
        super().display()