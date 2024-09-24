import pygame


class GameSound(object):
    def __init__(self):
        pygame.mixer.init()
        pygame.mixer.music.load("./images/bg2.ogg")
        pygame.mixer.music.set_volume(0.5)

    def PlayMusic(self):
        pygame.mixer.music.play(-1)