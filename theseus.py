import pygame
# from pygame.sprite import Sprite
from random import choice
import math

class Theseus():
    """ Since Theseus killed the Minautor in its maze, the Genomes will be known as Theuseus """
    def __init__(self, screen, settings, destination):
        """ Initialize Theseus' parameters """
        # super().__init__()
        self.screen     = screen
        self.settings   = settings
        self.destination= destination
        self.is_dead    = False
        self.has_reached= False

        self.radius = 5
        self.color = [255, 255, 255]
        self.x = settings.screen_width // 2
        self.y = settings.screen_height // 2

        self.brain = []

    def get_pos(self):
        """ Returns the position as a tuple """
        return (self.x, self.y)

    def update_pos(self):
        """ Updates Theseus' coordinates """
        dir_x = choice([-1, 0, 1])
        dir_y = choice([-1, 0, 1])
        dx = choice(range(5, 10)) # Horizontal Velocity 
        dy = choice(range(5, 10)) # Vertical Velocity 
        self.x += dx * dir_x
        self.y += dy * dir_y

        self.brain.append((dx, dir_x, dy, dir_y))

    def check_reached(self):
        """ Checks if Theseus has reached the Minautor """
        m_x, m_y = self.destination.get_pos()
        m_radius = self.destination.radius
        distance_centre = math.sqrt((m_x - self.x)**2 + (m_y - self.y)**2)
        sum_radii = m_radius + self.radius
        if distance_centre < sum_radii:
            self.color = pygame.colordict.THECOLORS['green']
            self.has_reached = True

    def kill(self):
        """ Marks this instance as Dead"""
        self.is_dead = True
        self.color = (255, 0, 0)# Turn RED when dead
        self.aftermath()

    def update(self):
        if self.is_dead == False and self.has_reached == False:
            self.update_pos()
            self.check_reached()
            if self.x >= self.settings.boundary['right'] or self.x <= self.settings.boundary['left'] or self.y >= self.settings.boundary['bottom'] or self.y <= self.settings.boundary['top']: 
                    self.kill()
        pygame.draw.circle(self.screen, self.color, self.get_pos(), self.radius)

    def aftermath(self):
        print(len(self.brain))
    