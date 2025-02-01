import pygame
import os

class Block(pygame.sprite.Sprite):
    def __init__(self, x, y, width=50, height=50, color=(255,255,0)):
        super().__init__()
        dir_current = os.path.dirname(os.path.dirname(__file__)) + "/image/objects"
        self.image = pygame.image.load(f"{dir_current}/block.png")
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def update(self, screen):
        screen.blit(self.image, self.rect)

