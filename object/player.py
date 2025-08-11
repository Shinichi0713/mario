
import pygame

gravity = 0.05

class Player(pygame.sprite.Sprite):
    def __init__(self, dir_image):
        super(Player, self).__init__()
        self.image = pygame.image.load(dir_image + "/stand.png")
        self.size_image = (50, 50)  # マリオのサイズ
        self.image = pygame.transform.scale(self.image, self.size_image)
        self.rect = self.image.get_rect()

        self.rect.x = 100   # マリオのx座標
        self.rect.y = 100   # マリオのy座標
        
        self.index_status = 0
        self.orientation = 1    # 1: 右向き, -1: 左向き
        self.run_images = [pygame.image.load(f'{dir_image}/run{i+1}.png') for i in range(0, 2)]
        self.walk_images = [pygame.image.load(f'{dir_image}/walk{i+1}.png') for i in range(0, 2)]
        self.stand_images = [pygame.image.load(f'{dir_image}/stand.png') for i in range(0, 2)]
        self.jump_images = [pygame.image.load(f'{dir_image}/jump.png') for i in range(0, 2)]

        self.velocity_x = 0 # x方向の速度
        self.velocity_y = 0 # y方向の速度
        self.acceleration_x = 0 # x方向の加速度
        self.acceleration_y = 0 # y方向の加速度
        self.velocity_x_limit = 10
        self.scaffold = False   # 足場にいるかどうか

    def update(self):
        global screen
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.image = pygame.transform.scale(self.run_images[self.index_status] ,self.size_image)
            self.orientation = 1
            if self.scaffold is True:
                self.acceleration_x = 0.02
        elif keys[pygame.K_LEFT]:
            self.image = pygame.transform.scale(self.run_images[self.index_status] ,self.size_image)
            self.orientation = -1
            if self.scaffold is True:
                self.acceleration_x = -0.02
        else:
            self.image = pygame.transform.scale(self.stand_images[self.index_status] ,self.size_image)
            self.acceleration_x = 0
        if keys[pygame.K_SPACE]:
            if self.scaffold:
                self.velocity_y = -5
                self.scaffold = False
            self.image = pygame.transform.scale(self.jump_images[self.index_status] ,self.size_image)
        
        if self.index_status == 1:
            self.index_status = 0
        else:
            self.index_status = 1
        if self.orientation == -1:
            self.image = pygame.transform.flip(self.image, True, False)
        # self.rect = self.image.get_rect()
        self.__calculate_motion()
        # screen.blit(self.image, self.rect)
        

    def __calculate_motion(self):
        
        self.velocity_x += self.acceleration_x
        if self.velocity_x > self.velocity_x_limit:
            self.velocity_x = self.velocity_x_limit
        elif self.velocity_x < -self.velocity_x_limit:
            self.velocity_x = -self.velocity_x_limit
        if self.scaffold is True:
            self.velocity_x *= 0.99
        self.velocity_y += self.acceleration_y + gravity

        self.rect.x += int(self.velocity_x)
        self.rect.y += self.velocity_y


