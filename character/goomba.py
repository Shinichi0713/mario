
import pygame
import pygame.display
import sys, os



class Goomba(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Goomba, self).__init__()
        self.images = []
        dir_current = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.images.append(pygame.image.load(f'{dir_current}/image/goomba/walk1.png'))
        self.images.append(pygame.image.load(f'{dir_current}/image/goomba/walk2.png'))
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocity = 2
        self.direction = -1  # -1: 左, 1: 右
        self.animation_time = 0.1
        self.current_time = 0

    def update(self, dt):
        self.rect.x += self.velocity * self.direction
        self.current_time += dt

        # アニメーションの更新
        if self.current_time >= self.animation_time:
            self.current_time = 0
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
            self.image = self.images[self.index]

        # 画面の端で方向を変える
        if self.rect.left <= 0 or self.rect.right >= 800:
            self.direction *= -1

    def draw(self, screen):
        screen.blit(self.image, self.rect)