
import pygame
import pygame.display
import sys, os



class Player(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        dir_current = os.path.dirname(__file__)