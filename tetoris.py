import pygame
import random

# Pygameの初期化
pygame.init()

# 画面サイズ
screen_width = 300
screen_height = 600
block_size = 30

# 色の定義
colors = [
    (0, 0, 0),
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255),
    (255, 255, 0),
    (255, 165, 0),
    (128, 0, 128),
    (0, 255, 255)
]

# テトリミノの形
shapes = [
    [[1, 1, 1, 1]],
    [[1, 1], 
     [1, 1]],
    [[0, 1, 0], 
     [1, 1, 1]],
    [[1, 0, 0], 
     [1, 1, 1]],
    [[0, 0, 1], 
     [1, 1, 1]],
    [[1, 1, 0], 
     [0, 1, 1]],
    [[0, 1, 1], 
     [1, 1, 0]]
]

class Tetrimino:
    def __init__(self, shape, color):
        self.shape = shape
        self.color = color
        self.rotation = 0
        self.x = screen_width // block_size // 2 - len(shape[0]) // 2
        self.y = 0

    def rotate(self):
        self.rotation = (self.rotation + 1) % 4
        self.shape = self.get_rotated_shape()

    def get_rotated_shape(self):
        if self.rotation == 1:
            return [list(row) for row in zip(*self.shape[::-1])]
        elif self.rotation == 2:
            return [row[::-1] for row in self.shape[::-1]]
        elif self.rotation == 3:
            return [list(row) for row in zip(*self.shape)][::-1]
        return self.shape

    def draw(self, screen):
        for y, row in enumerate(self.shape):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(screen, self.color, 
                                     (self.x * block_size + x * block_size, 
                                      self.y * block_size + y * block_size, 
                                      block_size, block_size))

class Tetris:
    def __init__(self):
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Tetris")
        self.clock = pygame.time.Clock()
        self.board = [[0] * (screen_width // block_size) for _ in range(screen_height // block_size)]
        self.current_tetrimino = self.get_new_tetrimino()
        self.next_tetrimino = self.get_new_tetrimino()
        self.game_over = False

    def get_new_tetrimino(self):
        shape = random.choice(shapes)
        color = random.choice(colors[1:])
        return Tetrimino(shape, color)

    def draw_board(self):
        for y, row in enumerate(self.board):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(self.screen, colors[cell], 
                                     (x * block_size, y * block_size, block_size, block_size))

    def check_collision(self):
        for y, row in enumerate(self.current_tetrimino.shape):
            for x, cell in enumerate(row):
                if cell:
                    if (self.current_tetrimino.y + y >= len(self.board) or
                        self.current_tetrimino.x + x < 0 or
                        self.current_tetrimino.x + x >= len(self.board[0]) or
                        self.board[self.current_tetrimino.y + y][self.current_tetrimino.x + x]):
                        return True
        return False

    def freeze_tetrimino(self):
        for y, row in enumerate(self.current_tetrimino.shape):
            for x, cell in enumerate(row):
                if cell:
                    self.board[self.current_tetrimino.y + y][self.current_tetrimino.x + x] = colors.index(self.current_tetrimino.color)
        self.clear_lines()
        self.current_tetrimino = self.next_tetrimino
        self.next_tetrimino = self.get_new_tetrimino()
        if self.check_collision():
            self.game_over = True

    def clear_lines(self):
        lines_to_clear = [i for i, row in enumerate(self.board) if all(row)]
        for i in lines_to_clear:
            del self.board[i]
            self.board.insert(0, [0] * (screen_width // block_size))

    def run(self):
        while not self.game_over:
            self.screen.fill((0, 0, 0))
            self.draw_board()
            self.current_tetrimino.draw(self.screen)
            pygame.display.flip()
            self.handle_events()
            self.update()
            self.clock.tick(10)
        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.current_tetrimino.x -= 1
                    if self.check_collision():
                        self.current_tetrimino.x += 1
                elif event.key == pygame.K_RIGHT:
                    self.current_tetrimino.x += 1
                    if self.check_collision():
                        self.current_tetrimino.x -= 1
                elif event.key == pygame.K_DOWN:
                    self.current_tetrimino.y += 1
                    if self.check_collision():
                        self.current_tetrimino.y -= 1
                elif event.key == pygame.K_UP:
                    self.current_tetrimino.rotate()
                    if self.check_collision():
                        self.current_tetrimino.rotate()
                        self.current_tetrimino.rotate()
                        self.current_tetrimino.rotate()

    def update(self):
        self.current_tetrimino.y += 1
        if self.check_collision():
            self.current_tetrimino.y -= 1
            self.freeze_tetrimino()

if __name__ == "__main__":
    game = Tetris()
    game.run()