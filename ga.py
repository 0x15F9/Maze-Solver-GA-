import pygame
from pygame.sprite import Group
import math

from theseus import Theseus
from minautor import Minautor
from maze import Maze

class Brain:
    """ Class for carrying out the evolution process """
    def __init__(self, settings, screen, population_size=25):
        self.settings = settings
        self.screen = screen

        self.population_size = population_size

        self.target = Minautor(screen, settings)
        self.maze = self.make_maze(screen)
        self.population = self.produce_population()

    def make_maze(self, screen):
        # TODO: Review the Maze class to allow creation of mazes and walls
        return Group(         [
            Maze(screen, (10, 10), width=220),  #Top
            Maze(screen, (10, 10), height=340), # Left
            Maze(screen, (10, 350), width=225), # Bottom
            Maze(screen, (230, 10), height=340) # Right
        ])

    def check_collide(self, genome, maze, target):
        collide_maze = pygame.sprite.spritecollide(genome, maze, False)
        reach_minautor = pygame.sprite.collide_rect(genome, target)
        if len(collide_maze) == True:
            genome.kill()
        if reach_minautor:
            genome.reach_target()

    def get_for_update(self):
        for genome in self.population:
            if genome.is_considered:
                self.check_collide(genome, self.maze, self.target)
        l = []
        l.append(self.maze)
        l.append(self.target)
        l.extend(self.population)
        return l

    def produce_genome(self):
        return Theseus(self.screen, self.settings)

    def produce_population(self):
        return [self.produce_genome() for i in range(self.population_size)]

    def get_fitness(self):
        x_target, y_target = self.target.get_pos() 
        x_genome, y_genome = self.genome.get_pos()
        distance_centre = math.sqrt((x_target - x_genome)**2 + (y_target - y_genome)**2)
        is_dead, num_steps = self.genome.is_dead, self.genome.num_steps
        if is_dead:
            fitness = 1 / (distance_centre * 10 + num_steps * 10)
        else:
            fitness = 1 / (distance_centre +num_steps * 10)
        return fitness
        