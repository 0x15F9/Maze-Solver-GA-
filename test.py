import pygame
from pygame.sprite import Group
import time
from functions import event_check, update_screen
from settings import Settings
from theseus import Theseus
from minautor import Minautor
from ga import Brain
from maze import Maze

def make_maze(screen):
    return [
        Maze(screen, (10, 10), width=220), #Top
        Maze(screen, (10, 10), height=340), # Left
        Maze(screen, (10, 350), width=225), # Bottom
        Maze(screen, (230, 10), height=340) # Right
    ]

def check_collide(theseus, maze, target):
    collide_maze = pygame.sprite.spritecollide(theseus, maze, False)
    reach_minautor = pygame.sprite.collide_rect(theseus, target)
    if len(collide_maze) == True:
        theseus.kill()
    if reach_minautor:
        theseus.reach_target()

def main():
    pygame.init()
    ms_settings = Settings()
    ms_screen   = pygame.display.set_mode(ms_settings.screen_size())
    pygame.display.set_caption(ms_settings.caption)
    ms_clock = pygame.time.Clock()

    a = Theseus(ms_screen, ms_settings)
    # b = [Theseus(ms_screen, ms_settings) for i in range(25)]
    m = Minautor(ms_screen, ms_settings)
    maze = Group()
    maze.add(make_maze(ms_screen))

    while True:
        ms_clock.tick(ms_settings.FPS)
        event_check()
        check_collide(a, maze, m)
        
        # for z in b:
        #     check_collide(z, maze, m)
            
        update_screen(ms_screen, ms_settings, characters=[maze, m, a, ])

main()