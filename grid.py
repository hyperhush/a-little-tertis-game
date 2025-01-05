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

    def is_inside(self, row, colume):
        if row >= 0 and row < self.rows and colume >= 0 and colume < self.columes:
            return True
        else:
            return False
        
    def is_empty(self, row, colume):
        if self.grid[row][colume] == 0:
            return True
        return False
    
    def is_row_full(self, row):
        for colume in range(self.columes):
            if self.grid[row][colume] == 0:
                return False
        return True
    
    def clear_row(self, row):
        for colume in range(self.columes):
            self.grid[row][colume] = 0

    def move_row_down(self, row, row_nums):
        for colume in range(self.columes):
            self.grid[row+row_nums][colume] = self.grid[row][colume]
            self.grid[row][colume] = 0

    def clear_full_rows(self):
        completed = 0
        for row in range(self.rows-1, 0, -1):
            if self.is_row_full(row):
                self.clear_row(row)
                completed += 1
            elif completed > 0:
                self.move_row_down(row, completed)

        return completed
    
    def clear_grid(self):
        for colume in range(self.columes):
            for row in range(self.rows):
                self.grid[row][colume] = 0

    def print_grid(self):
        for row in range(self.rows):
            for colume in range(self.columes):
                print(self.grid[row][colume], end = '')
            print()

    def draw(self, screen):
        for row in range(self.rows):
            for colume in range(self.columes):
                cell_value = self.grid[row][colume]
                cell_rect = pygame.Rect(colume * self.cell_size + 11, row * self.cell_size + 11, self.cell_size - 1, self.cell_size - 1)
                pygame.draw.rect(screen, self.colors[cell_value],cell_rect)