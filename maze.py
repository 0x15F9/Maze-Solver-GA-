import pygame
from pygame.sprite import Sprite

class Maze(Sprite):

    def __init__(self, screen, position, width=5, height=5):
        super().__init__()
        self.screen = screen

        self.color = [255, 255, 255]
        self.image = pygame.image.load('assets/wall.bmp')
        self.image = pygame.transform.scale(self.image,(width, height))
        self.rect = self.image.get_rect()

        self.x, self.y = position
        self.rect.x = self.x 
        self.rect.y = self.y

    def update(self):
        self.screen.blit(self.image, self.rect)