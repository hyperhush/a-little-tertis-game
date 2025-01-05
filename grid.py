import pygame
from colors import Colors
from setting import Setting

class Grid:
    def __init__(self):
        self.setting = Setting()
        self.rows = self.setting.row_number
        self.columes = self.setting.columes_number
        self.cell_size = self.setting.cell_size
        self.grid =[[0 for j in range(self.columes)] for i in range(self.rows)]
        self.colors = Colors.get_cell_colors()

    def print_grid(self):
        for row in range(self.rows):
            for colume in range(self.columes):
                print(self.grid[row][colume], end = '')
            print()

    def draw(self, screen):
        for row in range(self.rows):
            for colume in range(self.columes):
                cell_value = self.grid[row][colume]
                cell_rect = pygame.Rect(colume * self.cell_size, row * self.cell_size, self.cell_size - 1, self.cell_size - 1)
                pygame.draw.rect(screen, self.colors[cell_value],cell_rect)