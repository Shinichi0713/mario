

import pygame
import pygame.display
import sys, os
import pygame.transform
from object import Block, Objects, Player
from character import Goomba


# gravity = 0.05
screen = pygame.display.set_mode((800, 600))
pygame.mixer.init()
pygame.mixer.music.load(f"{os.path.dirname(os.path.abspath(__file__))}/music/マリオ地上BGM.mp3")

def event_main():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


def read_stage(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            stage_data = file.readlines()
        return [line.strip() for line in stage_data]

def draw_stage(filename):
    stage_data = read_stage(filename)
    print(stage_data)
    blocks = []
    for y, row in enumerate(stage_data):
        for x, col in enumerate(row):
            if col == "#":
                block = Block(x*50, y*50)
                blocks.append(block)
    return blocks

# Function to draw everything  
def draw_window(player, objects):  
    screen.fill((0, 120, 120))
    camera_x = player.rect.x - screen.get_width() // 2 + player.size_image[0] // 2  
    camera_y = player.rect.y - screen.get_height() // 2 + player.size_image[1] // 2
    screen.blit(player.image, (player.rect.x - camera_x, player.rect.y - camera_y)) 
    for object_calc in objects:
        screen.blit(object_calc.image, (object_calc.rect.x - camera_x, object_calc.rect.y - camera_y))
    pygame.display.flip() 

dir_current = os.path.dirname(__file__)
player = Player(f"{dir_current}/image/mario")
objects_operator = Objects()
blocks = draw_stage(f"{dir_current}/stage/2-stage.txt")
pygame.mixer.music.play()
while True:
    screen.fill((0, 120, 120))
    event_main()
    objects_operator.detect_collision(player, blocks)
    player.update()
    draw_window(player, blocks)
    pygame.display.update()



