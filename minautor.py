import pygame
from actor import Actor

class Minautor(Actor):
    """ Minautor will be the "destination" point of the genomes/Theseus """
    def __init__(self, screen, settings):
        """ Initialize the Minautor's parameters """
        super().__init__(screen, settings, (settings.screen_width // 2, 50), image_path="assets/target.bmp")
        self.screen     = screen
        self.settings   = settings
        # self.image = pygame.transform.scale(self.image, (10 ,10))
        # self.rect = self.image.get_rect()
        
    def update(self):
        super().display()
