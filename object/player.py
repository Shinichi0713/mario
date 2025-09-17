# マリオのクラス
import pygame
import os


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        dir_current = os.path.dirname(os.path.abspath(__file__))
        dir_image = os.path.join(os.path.dirname(dir_current), "image/mario")
        self.size_image = (50, 50)

        self.image = pygame.image.load(dir_image + "/stand.png")
        self.rect = self.image.get_rect()
        self.rect.x = 100   # マリオのx座標
        self.rect.y = 200   # マリオのy座標

        self.run_images = [pygame.image.load(f'{dir_image}/run{i+1}.png') for i in range(0, 2)]
        self.walk_images = [pygame.image.load(f'{dir_image}/walk{i+1}.png') for i in range(0, 2)]
        self.stand_images = [pygame.image.load(f'{dir_image}/stand.png') for i in range(0, 2)]
        self.jump_images = [pygame.image.load(f'{dir_image}/jump.png') for i in range(0, 2)]

        self.index_status = 0
        self.orientation = 1    # 1: 右向き, -1: 左向き


    def update(self, screen):
        self.__draw_image()
        screen.blit(self.image, self.rect)


    def __draw_image(self):
        status_group = self.index_status // 10
        index_group = self.index_status % 10

        if status_group == 0:
            self.image = self.stand_images[index_group]

        self.image = pygame.transform.scale(self.image, self.size_image)

        index_group = (index_group + 1) % 2

        if self.orientation == -1:
            self.image = pygame.transform.flip(self.image, True, False)

        self.index_status = 10 * status_group + index_group
