from pygame.sprite import Group
import math

from theseus import Theseus
from minautor import Minautor
from maze import Maze

class Brain:
    """ Class for carrying out the evolution process """
    def __init__(self, settings, screen, genome, target, population_size=25):
        self.settings = settings
        self.screen = screen
        self.genome = genome
        self.target = target

        self.population_size = population_size

    def produce_genome(self):
        return self.genome(self.screen, self.settings, self.target)

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
        