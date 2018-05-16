import pygame
import time
from functions import event_check, update_screen
from settings import Settings
from theseus import Theseus
from minautor import Minautor
import time

def main():
    pygame.init()
    ms_settings = Settings()
    ms_screen   = pygame.display.set_mode(ms_settings.screen_size())
    pygame.display.set_caption(ms_settings.caption)
    ms_clock = pygame.time.Clock()

    ms_minautor = Minautor(ms_screen, ms_settings)
    ms_swarm = [Theseus(ms_screen, ms_settings, ms_minautor) for i in range(25)]
    while True:
        ms_clock.tick(ms_settings.FPS)
        event_check()
        update_screen(ms_screen, ms_settings, characters=[*ms_swarm, ms_minautor])

main()