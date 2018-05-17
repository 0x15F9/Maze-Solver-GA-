import pygame
from pygame.sprite import Group
import time
from functions import event_check, update_screen
from settings import Settings
from theseus import Theseus
from minautor import Minautor
from ga import Brain
from maze import Maze

def follow_path(t):
    path = [(113, 180), (104, 180), (99, 188), (93, 179), (85, 184), (78, 184), (86, 184), (80, 177), (74, 183), (68, 178), (60, 170), (60, 178), (53, 183), (53, 174), (47, 180), (47, 185), (53, 194), (53, 189), (46, 180), (51, 174), (51, 174), (58, 174), (63, 181), (68, 181), (76, 189), (71, 189), (71, 198), (64, 189), (64, 180), (55, 180), (55, 172), (49, 172), (49, 172), (55, 178), (48, 178), (54, 178), (45, 187), (45, 179), (39, 179), (32, 179), (25, 187), (31, 178), (31, 172), (24, 178), (30, 173), (23, 164), (23, 171), (23, 171), (16, 166), (24, 166), (15, 172), (15, 163), (15, 158), (8, 152)]
    for x_coord, y_coord in path:
        t.move
def main():
    pygame.init()
    ms_settings = Settings()
    ms_screen   = pygame.display.set_mode(ms_settings.screen_size())
    pygame.display.set_caption(ms_settings.caption)
    ms_clock = pygame.time.Clock()

    brain = Brain(ms_settings, ms_screen, population_size=25)
    theseus = Theseus(ms_screen, ms_settings)

    while True:
        ms_clock.tick(ms_settings.FPS)
        event_check()
        update_screen(ms_screen, ms_settings, characters=list(brain.get_for_update()))
        # update_screen(ms_screen, ms_settings, characters=[theseus])

main()