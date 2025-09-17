
import pygame
import os
import sys
dir_current = os.path.dirname(__file__)
dir_parent = os.path.dirname(dir_current)
sys.path.append(dir_parent)
import object

def demo_main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    objects = []
    player = object.Player()
    objects.append(player)
    for i in range(10):
        block = object.Block(100 + i * 50, 100)
        objects.append(block)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        for obj in objects:
            obj.update(screen)
        pygame.display.flip()
        clock.tick(60)



if __name__ == "__main__":
    demo_main()
