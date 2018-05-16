import sys, pygame
import json, time
path = {}
def event_check():
    """ Check if a key is pressed and respond accordingly """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()

def update_screen(screen, settings, **kwargs):
    """ Updates the screen in the <While True> loop in main """
    screen.fill(settings.bg_color)

    for key, value in kwargs.items():
        if key == "characters":
            for character in value:
                character.update()
    pygame.display.flip()