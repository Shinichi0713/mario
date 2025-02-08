# 物体関係の処理
import pygame



class Objects:
    def __init__(self):
        pass
    
    # 衝突判定
    def detect_collision(self, player, objects):
        for object_calc in objects:
            if pygame.sprite.collide_rect(player, object_calc):
                self.calculate_motion_collision(player, object_calc)
        return False
    
    # 方向に応じた計算
    def calculate_motion_collision(self, player, object_calc):
        collision_rect = player.rect.clip(object_calc.rect)
        if collision_rect.width >= collision_rect.height:
            # 足場となる場合
            if collision_rect.top == object_calc.rect.top:
                player.rect.bottom = object_calc.rect.top
                player.scaffold = True  # 足場にいる
                player.velocity_y = 0
            # 天井となる場合
            elif collision_rect.bottom == object_calc.rect.bottom:
                player.rect.top = object_calc.rect.bottom
                player.velocity_y = 0
        else:
            # 左側となる場合
            if collision_rect.right == object_calc.rect.right:
                player.rect.left = object_calc.rect.right
                player.velocity_x = 0
            # 右側となる場合
            elif collision_rect.left == object_calc.rect.left:
                player.rect.right = object_calc.rect.left
                player.velocity_x = 0