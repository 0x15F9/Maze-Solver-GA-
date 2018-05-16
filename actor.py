import pygame
from pygame.sprite import Sprite

class Actor(Sprite):
    def __init__(self, screen, settings, pos, image_path="assets/alive.bmp"):
        super().__init__()
        self.screen     = screen
        self.settings   = settings

        self.image  = pygame.image.load(image_path)
        self.rect   = self.image.get_rect()
        self.x , self.y = pos
        self.rect.x = self.x 
        self.rect.y = self.y

    def get_pos(self):
        """ Returns the position as a tuple """
        return (self.x, self.y)

    def display(self):
        self.screen.blit(self.image, self.rect)
        
    